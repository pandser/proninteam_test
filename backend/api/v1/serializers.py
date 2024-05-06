import base64

from django.core.files.base import ContentFile
from djoser.serializers import UserSerializer
from rest_framework import serializers

from collect.models import Collect, Payment


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class PaymentSerialiser(serializers.ModelSerializer):

    date_pay = serializers.DateTimeField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = (
            'id',
            'user',
            'collect',
            'amount_pay',
            'date_pay',
        )


class CollectSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    current_result = serializers.IntegerField(read_only=True)
    participant = serializers.SerializerMethodField(read_only=True)
    image = Base64ImageField()
    collection_feed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Collect
        fields = (
            'id',
            'author',
            'name',
            'motive',
            'description',
            'total',
            'current_result',
            'participant',
            'image',
            'end_date',
            'collection_feed',
        )
    
    def get_collection_feed(self, collect):
        return collect.collect.values(
            'user__first_name',
            'user__last_name',
            'amount_pay',
            'date_pay'
        )
    
    def get_participant(self, collect):
        return collect.collect.values('user').distinct().count()
