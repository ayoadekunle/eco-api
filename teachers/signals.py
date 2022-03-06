from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Teacher


@receiver(post_save, sender=User)
def create_teacher(sender, instance, created, **kwargs):
    if created:
        Teacher.objects.create(user=instance)
