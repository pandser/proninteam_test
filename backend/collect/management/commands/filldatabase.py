import random

from django.core.management.base import BaseCommand
from mixer.backend.django import mixer


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        user = mixer.cycle(200).blend('auth.user')
        collect = mixer.cycle(400).blend(
            'collect.collect',
            author=mixer.SELECT,
            total=mixer.RANDOM(
                i for i in [random.randint(10, 1000000) for _ in range(400)]
            ),
        )
        payment = mixer.cycle(1000).blend(
            'collect.payment',
            user=mixer.SELECT,
            collect=mixer.SELECT
        )