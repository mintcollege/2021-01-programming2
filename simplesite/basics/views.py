from django.shortcuts import render
from django.http import HttpResponse


# Your first view
def homex(request):
    return HttpResponse('Hello world')


def contact(request):
    return HttpResponse('Contact page')


def portfolio(request):
    return HttpResponse('Portfolio page')


def login(request):
    return HttpResponse('User login here')