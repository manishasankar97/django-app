# Generated by Django 3.1.1 on 2020-09-22 12:02

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dapi', '0008_remove_user_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='end_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='start_time',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2020, 9, 22, 12, 2, 12, 178294, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
