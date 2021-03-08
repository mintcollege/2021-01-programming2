from django.db import models

# Create your models here.

class Message(models.Model):
    username = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)
    userage = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message
    
    
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Admin(models.Model):
    username = models.CharField(max_length=20)