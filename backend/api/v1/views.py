from datetime import datetime

from django.db.models import Count, Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.v1.permissions import IsAdminAuthorOrReadOnly
from api.v1.serializers import CollectSerializer, PaymentSerialiser
from api.v1.tasks import send_email
from collect.models import Collect, Payment



class CreateModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


class CollectViewSet(ModelViewSet):
    queryset = Collect.objects.annotate(
        current_result=Sum('payment__amount_pay'),
        participant=Count('payment__user', distinct=True),
    )
    serializer_class = CollectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminAuthorOrReadOnly)

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        send_email.delay(
            theme='Сбор создан',
            body='Сбор успешно создан',
            recipient=[request.user.email],
        )
        return super().create(request, *args, **kwargs)


class PaymentViewSet(CreateModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerialiser

    def perform_create(self, serializer):
        serializer.save(
            date_pay=datetime.now(),
            user=self.request.user,
        )

    def create(self, request, *args, **kwargs):
        send_email.delay(
            theme='Платеж принят',
            body='Платеж прошел успешно',
            recipient=[request.user.email],
        )
        return super().create(request, *args, **kwargs)
 