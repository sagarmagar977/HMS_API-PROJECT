from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

routers=DefaultRouter()
routers.register('bills',billsview)
routers.register('payment',paymentview)

urlpatterns = [
    path('accounting/',include(routers.urls)),

]
