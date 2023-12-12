from django.shortcuts import render
from .views import *
from .serializers import *

from rest_framework import viewsets
from core.permission import CustomModelPermission

class menuview(viewsets.ModelViewSet):
    queryset=menu.objects.all()
    serializer_class=menuSerializer
    permission_classes=[CustomModelPermission]


class foodview(viewsets.ModelViewSet):
    queryset=food.objects.all()
    serializer_class=foodSerializer
    permission_classes=[CustomModelPermission]
# Create your views here.
