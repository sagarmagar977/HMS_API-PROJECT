from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group

class guestinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=GuestInfo
        fields='__all__'

#custom serilaizer for only f_name 
class guest_f_name_serializer(serializers.ModelSerializer):
    class Meta:
        model=GuestInfo
        fields=['f_name','l_name']

class roomtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=roomtype
        fields='__all__'

class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model=room
        fields='__all__'

class room_no_Serializer(serializers.ModelSerializer):
    class Meta:
        model=room
        fields=['room_no']
class guestroomSerializer(serializers.ModelSerializer):
    
    guest = guest_f_name_serializer() # for guest field
    room_no = room_no_Serializer() #for room no field
    class Meta:
        model=guestroom
        fields='__all__'

class Groupserializers(serializers.ModelSerializer):

    
    class Meta:
        model= Group
        fields= ['id','name']