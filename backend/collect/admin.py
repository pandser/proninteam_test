from django.contrib import admin

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
        'image',
        'end_date',
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'collect',
        'amount_pay',
        'date_pay',
    )
