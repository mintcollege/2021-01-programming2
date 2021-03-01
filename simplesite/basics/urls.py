from django.urls import path
from .views import homex, contact, portfolio, login


urlpatterns = [
    path('home/', homex),
    path('contact/', contact),
    path('portfolio/', portfolio),
    path('signin/', login),
]