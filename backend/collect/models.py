from django.db import models
from django.contrib.auth import get_user_model

from collect.constants import MOTIVE


User = get_user_model()


class Collect(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
    )
    name = models.CharField(max_length=240)
    motive = models.CharField(
        max_length=3,
        choices=MOTIVE,
    )
    description = models.TextField()
    total = models.PositiveBigIntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    end_date = models.DateTimeField()


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
    )
    collect = models.ForeignKey(
        Collect,
        on_delete=models.CASCADE,
        related_name='payment',
    )
    amount_pay = models.PositiveIntegerField()
    date_pay = models.DateTimeField()
