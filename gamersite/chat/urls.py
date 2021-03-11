from django.urls import path
from .views import home, create_user, create_message, read_messages, read_users, read_message, \
    delete_message, update_message


urlpatterns = [
    path('', home),
    path('createuser/', create_user),
    path('createmessage/', create_message),
    
    path('messages/', read_messages),
    path('message/<int:pk>', read_message),   # pk: primary key
    path('message/<int:pk>/update', update_message),
    path('message/<int:pk>/delete', delete_message),
    
    path('users/', read_users),
]