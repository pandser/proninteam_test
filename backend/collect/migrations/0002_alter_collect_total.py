# Generated by Django 4.2.11 on 2024-05-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='total',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
