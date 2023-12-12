from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('guestinfo', guestinfoview)
routers.register('roomtype',roomtypeview)
routers.register('room',roomview)
routers.register('guestroom',guestroomview)

urlpatterns = [
    path('frontdesk/', include(routers.urls)),
    path('group/all/',GroupAPIView.as_view(),name='group')
    
]
