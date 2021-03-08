from django.shortcuts import render
from django.http import HttpResponse
from icecream import ic

from .models import User, Message


def home(request):
    # return HttpResponse('This is the gamersite chat page.')
    context = {
        'sitename': 'Chat',
        'username': 'jeff120',
        'title': 'Meet new friends!',
    }
    return render(request, 'chat/home.html', context)


def create_user(request):
    User.objects.create(username='jeff321', email='jeff321@gmail.com', bio='To follow')
    return HttpResponse('New user created!')


def read_users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'chat/users.html', context)


def create_message(request):
    """3 ways to add content to your database"""
    
    message = 'Food is good.'
    
    # Method 1: create and save at the same time
    # Message.objects.create(username='jeff321', message=message, userage=22)
    
    # Method 2: uses ** which "extracts" the contents of the data variable
    data = {
        'message': message,
        'username': 'martin',
        'userage': 99,
        # 'timezone': '+08:00'
    }
    Message.objects.create(**data)
    # Using **data is equivalent to:
    # Message.objects.create(username='jeff321', message=message, userage=22)
    
    # Method 3: manually save the message instead of automatically (Method 1)
    # row = Message(**data)
    # row.save()
    return render(request, 'chat/message_created.html', data)


def read_messages(request):
    messages = Message.objects.filter(userage=22)
    context = {
        'allmessages': messages
    }
    return render(request, 'chat/messages.html', context)