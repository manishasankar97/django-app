# Generated by Django 3.1.1 on 2020-09-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapi', '0003_auto_20200921_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tz',
        ),
        migrations.AlterField(
            model_name='user',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
