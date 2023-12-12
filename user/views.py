from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import *
from django.contrib.auth.hashers import make_password

from core.permission import CustomModelPermission

from django.contrib.auth.models import Group

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.generics import  GenericAPIView
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)

    if user is not None and user.is_authenticated:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Invalid email or password!'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    
    password = request.data.get('password')
    request.data['password']= make_password(password)
    serializer=userSerilaizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('User Created')
    else:
        return Response(serializer.errors)
    


class UserAPI(GenericAPIView):
    queryset=user.objects.all()
    serializer_class=userSerilaizer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['groups']
    permission_classes=[CustomModelPermission]

    def get(self,request):
        queryset=self.get_queryset()
        filter_queryset=self.filter_queryset(queryset)
        serializer=self.serializer_class(filter_queryset,many=True)
        return Response(serializer.data)
