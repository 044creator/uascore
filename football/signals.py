from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Matches
from .utils import rebuild_table_from_matches

@receiver(post_save, sender=Matches)
def rebuild_table_on_match_save(sender, instance, **kwargs):
    if instance.status == 'finished':
        rebuild_table_from_matches(instance.league)
