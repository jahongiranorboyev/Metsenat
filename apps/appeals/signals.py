from decimal import Decimal
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from apps.appeals.models import Appeal


@receiver([post_save,post_delete], sender=Appeal)
def update_sponsor_total_balance_on_save(sender, instance, **kwargs):
    """
    `Appeal` updates `sponsor`s total_balance value when saved.
    """
    sponsor_appeals = Appeal.objects.filter(
        sponsor=instance.sponsor,
        status=Appeal.AppealStatus.Approved
    )
    total_balance = sponsor_appeals.aggregate(
        total_balance=Sum('amount')
    )['total_balance'] or Decimal('0')
    instance.sponsor.total_balance = total_balance
    instance.sponsor.save(update_fields=['total_balance'])


    sponsor = instance.sponsor
    sponsor.available_balance = Appeal.objects.filter(
        sponsor=sponsor,
        status=Appeal.AppealStatus.Approved
    ).aggregate(total_balance=Sum('available_balance'))['total_balance'] or Decimal('0')
    sponsor.save(update_fields=['available_balance'])