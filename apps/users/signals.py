from django.contrib.auth.models import Group, Permission
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import UserModel

@receiver(post_save, sender=UserModel)
def post_save_user(sender, instance,created, **kwargs):
    """

    """
    #========================== permissions connect every user whey they are created ======4
    if created:
        instance.add_group()