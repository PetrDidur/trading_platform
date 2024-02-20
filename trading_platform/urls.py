from trading_platform.apps import TradingPlatformConfig
from rest_framework.routers import DefaultRouter

from trading_platform.views import NetworkNodeViewSet

app_name = TradingPlatformConfig.name

router = DefaultRouter()
router.register(r'NetworkNode', NetworkNodeViewSet, basename='NetworkNode')

urlpatterns = [

] + router.urls
