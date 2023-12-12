from django.shortcuts import render
from .views import *
from .serializers import *
from rest_framework import viewsets
from core.permission import CustomModelPermission


class billsview(viewsets.ModelViewSet):
    queryset=bills.objects.all()
    serializer_class=billsSerializer
    permission_classes=[CustomModelPermission]

# Create your views here.
class paymentview(viewsets.ModelViewSet):
    queryset=payment.objects.all()
    serializer_class=paymentSerializer
    permission_classes=[CustomModelPermission]