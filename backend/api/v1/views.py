from datetime import datetime

from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.v1.permissions import IsAdminAuthorOrReadOnly
from api.v1.serializers import CollectSerializer, PaymentSerialiser
from api.v1.tasks import send_email
from collect.models import Collect


class CollectViewSet(ModelViewSet):
    queryset = Collect.objects.annotate(
        current_result=Sum('collect__amount_pay'),
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
            sender='example@example.com',
            recipient=[request.data.get('email')],
        )
        return super().create(request, *args, **kwargs)


class PaymentView(views.APIView):
    
    def post(self, request):
        serializer = PaymentSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            date_pay=datetime.now(),
            user=request.user,
        )
        send_email.delay(
            theme='Платеж принят',
            body='Платеж прошел успешно',
            sender='example@example.com',
            recipient=[request.data.get('email')],
        )
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        