from djoser.serializers import UserSerializer
from rest_framework import serializers

from collect.models import Collect, Payment


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
