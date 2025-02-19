from decimal import Decimal

from django.db.models import Sum, F
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete, pre_save

from apps.appeals.models import Appeal
from apps.sponsors.models import StudentSponsor

previous_amounts = {}

@receiver(pre_save, sender=StudentSponsor)
def store_previous_amount(sender, instance, **kwargs):
    """
    Store previous amount before updating StudentSponsor.
    """

    if instance.pk:
        try:
            previous_amounts[instance.pk] = StudentSponsor.objects.get(pk=instance.pk).amount
        except StudentSponsor.DoesNotExist:
            previous_amounts[instance.pk] = Decimal('0')
    else:
        previous_amounts[instance.pk] = Decimal('0')

    previous_amount = previous_amounts.pop(instance.pk, Decimal('0'))
    instance.student.necessary_balance = F('necessary_balance') + previous_amount
    instance.student.save(update_fields=['necessary_balance'])
    instance.student.refresh_from_db()

    instance.appeal.available_balance = F('available_balance') + previous_amount
    instance.appeal.save(update_fields=['available_balance'])
    instance.appeal.refresh_from_db()

    if instance.amount > instance.appeal.available_balance:
        raise ValidationError({'message': 'Amount cannot be greater than the appeal available balance.'})
    if instance.amount > instance.student.necessary_balance:
        raise ValidationError({'message': 'Amount cannot be greater than the student\'s necessary balance.'})

    # Update sponsor's available_balance
    sponsor = instance.appeal.sponsor
    sponsor.available_balance = Appeal.objects.filter(
        sponsor=sponsor,
        status=Appeal.AppealStatus.Approved
    ).aggregate(total_balance=Sum('available_balance'))['total_balance'] or Decimal('0')
    sponsor.save(update_fields=['available_balance'])

@receiver(post_save, sender=StudentSponsor)
def update_balances_on_save(sender, instance, created, **kwargs):
    """
    Update balances when a StudentSponsor is created or updated.
    """   
    instance.student.necessary_balance = F('necessary_balance') - instance.amount
    instance.student.save(update_fields=['necessary_balance'])
    instance.student.refresh_from_db()

    instance.appeal.available_balance = F('available_balance') - instance.amount
    instance.appeal.save(update_fields=['available_balance'])
    instance.appeal.refresh_from_db()


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
    instance.student.refresh_from_db()

    # Add back sponsorship amount to appeal's available balance
    instance.appeal.available_balance = F('available_balance') + instance.amount
    instance.appeal.save(update_fields=['available_balance'])

    # Update sponsor's available_balance
    sponsor = instance.appeal.sponsor
    sponsor.available_balance = Appeal.objects.filter(
        sponsor=sponsor,
        status=Appeal.AppealStatus.Approved
    ).aggregate(total_balance=Sum('available_balance'))['total_balance'] or Decimal('0')
    sponsor.save(update_fields=['available_balance'])


