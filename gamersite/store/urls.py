from django.urls import path
from .views import thestore


urlpatterns = [
    path('', thestore)
]


