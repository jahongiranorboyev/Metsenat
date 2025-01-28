from decimal import Decimal
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum, F
from apps.sponsors.models import StudentSponsor
from apps.appeals.models import Appeal


@receiver(post_save, sender=StudentSponsor)
def update_balances_on_save(sender, instance, created, **kwargs):
    """
    Update balances when a StudentSponsor is created or updated.
    """
    # Deduct sponsorship amount from student's necessary balance
    instance.student.necessary_balance = F('necessary_balance') - instance.amount
    instance.student.save(update_fields=['necessary_balance'])
    instance.student.refresh_from_db()  # Ensure fresh data

    # Deduct sponsorship amount from appeal's available balance
    instance.appeal.available_balance = F('available_balance') - instance.amount
    instance.appeal.save(update_fields=['available_balance'])

    # Ensure fresh data
    instance.appeal.refresh_from_db()

    # Update sponsor's available_balance
    sponsor = instance.appeal.sponsor
    sponsor.available_balance = Appeal.objects.filter(
        sponsor=sponsor,
        status=Appeal.AppealStatus.Approved
    ).aggregate(total_balance=Sum('available_balance'))['total_balance'] or Decimal('0')
    sponsor.save(update_fields=['available_balance'])


@receiver(post_delete, sender=StudentSponsor)
def revert_balances_on_delete(sender, instance, **kwargs):
    """
    Revert balances when a StudentSponsor is deleted.
    """
    # Add back sponsorship amount to student's necessary balance
    instance.student.necessary_balance = F('necessary_balance') + instance.amount
    instance.student.save(update_fields=['necessary_balance'])
    instance.student.refresh_from_db()  # Ensure fresh data

    # Add back sponsorship amount to appeal's available balance
    instance.appeal.available_balance = F('available_balance') + instance.amount
    instance.appeal.save(update_fields=['available_balance'])
    instance.appeal.refresh_from_db()  # Ensure fresh data

    # Update sponsor's available_balance
    sponsor = instance.appeal.sponsor
    sponsor.available_balance = Appeal.objects.filter(
        sponsor=sponsor,
        status=Appeal.AppealStatus.Approved
    ).aggregate(total_balance=Sum('available_balance'))['total_balance'] or Decimal('0')
    sponsor.save(update_fields=['available_balance'])
