from rest_framework import serializers
from .models import Order, OrderType, Status


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class OrderTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
