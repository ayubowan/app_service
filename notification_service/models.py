from django.db import models


# Create your models here.

class Message(models.Model):
    class MessageType(models.TextChoices):
        CRITICAL = 'CRT', _('Critical')
        INFO = 'INF', _('Info')
        WARNING = 'WAR', _('Warning')

    title = models.CharField()
    message = models.TextField()
    type = models.CharField(
        max_length=2,
        choices=MessageType.choices,
        default=MessageType.INFO,
    )
