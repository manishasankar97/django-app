# Generated by Django 3.1.1 on 2020-09-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapi', '0011_auto_20200922_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='start_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
