from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    username=models.CharField(max_length=100,default='user',null=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    
    #overirde of username by email to login
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']