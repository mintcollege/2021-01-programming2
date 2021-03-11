from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import ObjectDoesNotExist
from icecream import ic

from .models import User, Message
from .forms import CreateMessage


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
    
    # message = 'Today is the day.'
    
    # Method 1: create and save at the same time
    # Message.objects.create(username='jeff321', message=message, userage=22)
    
    # Method 2: uses ** which "extracts" the contents of the data variable
    # data = {
    #     'message': message,
    #     'username': 'Jennifer',
    #     'userage': 22,
    # }
    # Message.objects.create(**data)
    # Using **data is equivalent to:
    # Message.objects.create(username='jeff321', message=message, userage=22)
    
    # Method 3: manually save the message instead of automatically (Method 1)
    # row = Message(**data)
    # row.save()
    
    # Save the form data sent by the user
    if request.method == 'POST':
        # Save the form
        form = CreateMessage(request.POST)
        if form.is_valid():
            # Save the data here
            data = {
                'message': form.cleaned_data['message'],
                'username': form.cleaned_data['username'],
                'userage': form.cleaned_data.get('userage', 0),
            }
            # Creates the object and saves at the same time
            Message.objects.create(**data)
            # Same as above except you save it manually
            # msg = Message(**data)
            # msg.save()
            return render(request, 'chat/message_created.html', data)
    else:
        # Create the form to show to the user
        form = CreateMessage()
        
        context = {
            'form': form
        }
        return render(request, 'chat/create-message.html', context)


def read_messages(request):
    messages = Message.objects.filter(userage=22)
    context = {
        'allmessages': messages
    }
    return render(request, 'chat/messages.html', context)


def read_message(request, pk):
    try:
        # SQL
        # SELECT id, username FROM chat_message WHERE id = 8;
        msg = Message.objects.get(id=pk)
        context = {
            'message': msg,
        }
        return render(request, 'chat/message-detail.html', context)
    except ObjectDoesNotExist:
        return render(request, 'chat/does-not-exist.html')


def delete_message(request, pk):
    try:
        # hard delete
        # SQL
        # SELECT * FROM chat_message WHERE id = 8;
        msg = Message.objects.get(id=pk)
        # SQL
        # DELETE FROM chat_message WHERE id = 8;
        msg.delete()
        return render(request, 'chat/message-deleted.html')
    except ObjectDoesNotExist:
        return render(request, 'chat/does-not-exist.html')
    
    
def update_message(request, pk):
    try:
        msg = Message.objects.get(id=pk)
        ic(vars(msg))
        msg.username = 'Sophie'
        msg.message = 'This is a new message'
        msg.save()
        ic(vars(msg))
        return render(request, 'chat/message-updated.html')
    except ObjectDoesNotExist:
        return render(request, 'chat/does-not-exist.html')
    
