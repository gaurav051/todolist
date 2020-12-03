from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    first_name = models.CharField(max_length = 200, null = True, blank = True)
    middle_name = models.CharField(max_length = 200, null = True, blank = True)
    last_name = models.CharField(max_length = 200, null = True, blank = True)
    contact = models.CharField(max_length = 200, null = True, blank = True)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

