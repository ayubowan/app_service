from django.urls import path

from . import views

urlpatterns = [
    # Without Login Views
    path('latest_messages/<int:offset>/<int:limit>', views.get_latest_messages, name='get_latest_messages'),

]
