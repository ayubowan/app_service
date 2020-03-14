from django.http import JsonResponse

# Create your views here.
from notification_service.models import Message


def get_latest_messages(request, limit, offset):
    messages = Message.objects.filter(is_valid=True).order_by("-broadcast_time").all()[offset:offset + limit]
    messages = messages if messages else []
    return JsonResponse(
        data=[{
            "title": msg.title,
            "message": msg.message,
            "broadcast_time": msg.broadcast_time.timestamp(),
            "is_valid": msg.is_valid
        } for msg in messages]
        , safe=False
    )
