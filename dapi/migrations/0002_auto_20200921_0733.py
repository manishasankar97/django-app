# Generated by Django 3.1.1 on 2020-09-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
