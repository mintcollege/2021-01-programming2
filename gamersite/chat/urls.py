from django.urls import path
from .views import home, create_user, create_message, read_messages, read_users


urlpatterns = [
    path('', home),
    path('createuser/', create_user),
    path('createmessage/', create_message),
    path('messages/', read_messages),
    path('users/', read_users)
]