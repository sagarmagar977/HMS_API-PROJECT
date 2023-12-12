from .models import *
from rest_framework import serializers

class userSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['id','email','password','groups']