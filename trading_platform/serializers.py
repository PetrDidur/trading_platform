from rest_framework import serializers

from trading_platform.models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'
        searching_fields = ['country']




