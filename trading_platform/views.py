from rest_framework import viewsets

from trading_platform.models import NetworkNode
from trading_platform.serializers import NetworkNodeSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer

