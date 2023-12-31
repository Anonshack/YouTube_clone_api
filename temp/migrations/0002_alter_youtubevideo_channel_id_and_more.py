# Generated by Django 4.2.6 on 2023-10-07 06:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideo',
            name='channel_id',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='video_id',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
