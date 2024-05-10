from django.urls import include, path
from rest_framework import routers

from api.v1.views import CollectViewSet, PaymentViewSet


router = routers.DefaultRouter()

router.register(
    'collects',
    CollectViewSet,
    basename='collect',
)

router.register(
    'payments',
    PaymentViewSet,
    basename='payment'
)

urlpatterns = [
    path('', include(router.urls)),
]
