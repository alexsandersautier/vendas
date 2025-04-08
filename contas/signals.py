from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, is_password_usable

@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    if not instance.password.startswith('pbkdf2_') and is_password_usable(instance.password):
        instance.password = make_password(instance.password)