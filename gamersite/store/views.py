from django.shortcuts import render
from django.http import HttpResponse


def thestore(request):
    # return HttpResponse('Buy games from the store.')
    context = {
        'sitename': 'Chat',
        'username': 'jeff120',
        'title': 'Buy some games',
    }
    return render(request, 'store/home.html', context)
