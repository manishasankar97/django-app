# Generated by Django 3.1.1 on 2020-09-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapi', '0002_auto_20200921_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='end_time',
            field=models.DateTimeField(),
        ),
    ]
