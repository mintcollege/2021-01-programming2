from django.shortcuts import render
from django.http import HttpResponse

"""
M: Models - Database
T: Templates - HTML
V: Views - Business Logic
"""


# Your first view
def homex(request):
    # return HttpResponse('Hello world')
    username = 'Earl'
    context = {
        'user': username,
        'title': 'Welcome to the site!',
        'date_posted': 'March 4, 2021'
    }
    return render(request, 'home.html', context)


def contact(request):
    # return HttpResponse('Contact page')
    return render(request, 'contact.html')


def portfolio(request):
    return HttpResponse('Portfolio page')


def login(request):
    return HttpResponse('User login here')