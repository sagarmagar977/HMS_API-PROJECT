from django.urls import path,include
from .views import *

from rest_framework.routers import DefaultRouter

routers=DefaultRouter()

routers.register('menu',menuview)
routers.register('food',foodview)

urlpatterns = [
    path('restaurent/',include(routers.urls))
]
