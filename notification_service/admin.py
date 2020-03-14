from django.contrib import admin

# Register your models here.
from notification_service.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
