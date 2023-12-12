from rest_framework import serializers
from .models import *


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model=menu
        fields='__all__'


class foodSerializer(serializers.ModelSerializer):
    class Meta:
        model=food
        fields='__all__'

