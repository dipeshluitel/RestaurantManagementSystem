from django.db.models.signals import post_migrate,post_save
from django.contrib.auth.models import Group,User
from django.dispatch import receiver
from .models import Profile

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    groups = ['Admin', 'Waiter', 'Kitchen']
    for group in groups:
        Group.objects.get_or_create(name=group)

@receiver(post_save, sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)