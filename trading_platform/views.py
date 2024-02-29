from rest_framework import viewsets

from trading_platform.models import NetworkNode
from trading_platform.permissions import IsActiveEmployee
from trading_platform.serializers import NetworkNodeSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('country',)



