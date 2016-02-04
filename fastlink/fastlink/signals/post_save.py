from django.db.models.signals import post_save
from django.dispatch import receiver

from fastlink.models import Resource


@receiver(post_save, sender=Resource)
def post_save_resource(sender, instance, created, **kwargs):
    if created:
        instance._create_hash_id()
