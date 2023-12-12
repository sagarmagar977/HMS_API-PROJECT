from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from core.permission import CustomModelPermission
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class guestinfoview(viewsets.ModelViewSet):
    queryset=GuestInfo.objects.all()
    serializer_class=guestinfoSerializer
    permission_classes=[CustomModelPermission]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    #gives matching result (it is not case sensetive)
    search_fields = ['f_name', 'l_name']
    #give only if give search words fully matched (it is case sensetive)
    filterset_fields = ['f_name']
    
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Check if the queryset is empty
        if not queryset.exists():
            return Response({"detail": "No results found."}, status=200) 

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class roomtypeview(viewsets.ModelViewSet):
    queryset=roomtype.objects.all()
    serializer_class=roomtypeSerializer
    permission_classes=[CustomModelPermission]

    ##### for filter and search
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    
    search_fields = ['name']
    
    filterset_fields = ['name']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Check if the queryset is empty
        if not queryset.exists():
            return Response({"detail": "No results found."}, status=200) 

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class roomview(viewsets.ModelViewSet):
    queryset=room.objects.all()
    serializer_class=roomSerializer
    permission_classes=[CustomModelPermission]
    ########## For  searhing and Filtering ###############
    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    
    search_fields = ['room_no']
    
    filterset_fields = ['status']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Check if the queryset is empty
        if not queryset.exists():
            return Response({"detail": "No results found."}, status=200) 

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class guestroomview(viewsets.ModelViewSet):
    queryset=guestroom.objects.all()
    serializer_class=guestroomSerializer
    permission_classes=[CustomModelPermission]

    filter_backends = [DjangoFilterBackend,filters.SearchFilter]

    
    search_fields = ['guest__f_name'] # for getting f_name of guest
    # filterset_fields = ['room_no__room_no']
    filterset_fields = ['room_no__room_no']
    
    # filterset_fields = ['status']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Check if the queryset is empty
        if not queryset.exists():
            return Response({"detail": "No results found."}, status=200) 

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


   




class GroupAPIView(GenericAPIView):
    queryset=Group.objects.all()
    serializer_class=Groupserializers
    permission_classes=[CustomModelPermission]
    def get(self,request):
        queryset=self.get_queryset()
        serializer=self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    

    
# class GroupAPIView(generics.GenericAPIView,ListModelMixin):
#     queryset=Group.objects.all()
#     serializer_class=Groupserializers
  
       