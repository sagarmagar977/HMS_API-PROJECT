from rest_framework import serializers
from .models import *


class billsSerializer(serializers.ModelSerializer):
    class Meta:
        model=bills
        fields='__all__'


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=payment
        fields='__all__'
