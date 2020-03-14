from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Message(models.Model):
    class MessageType(models.TextChoices):
        CRITICAL = 'CRT', _('Critical')
        INFO = 'INF', _('Info')
        WARNING = 'WAR', _('Warning')

    title = models.CharField(max_length=80)
    message = models.TextField()
    type = models.CharField(
        max_length=3,
        choices=MessageType.choices,
        default=MessageType.INFO,
    )
    broadcast_time = models.DateTimeField(default=now)
    is_valid = models.BooleanField(default=True)
