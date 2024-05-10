from django.contrib import admin
from django.db.models import Count, Sum

from collect.models import Collect, Payment


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = (
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
    )

    def current_result(self, obj):
        return obj.payment.aggregate(Sum('amount_pay')).get('amount_pay__sum')

    def participant(self, obj):
        return obj.payment.aggregate(
            Count('user', distinct=True)
        ).get('user__count')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'collect',
        'amount_pay',
        'date_pay',
    )
