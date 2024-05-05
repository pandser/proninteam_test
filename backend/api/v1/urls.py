from django.urls import include, path
from rest_framework import routers

from api.v1.views import CollectViewSet, PaymentView


router = routers.DefaultRouter()

router.register(
    'collects',
    CollectViewSet,
    basename='collect',
)

urlpatterns = [
    path('payments/', PaymentView.as_view()),
    path('', include(router.urls)),
]
