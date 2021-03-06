# Generated by Django 3.1.1 on 2020-09-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbid', models.CharField(max_length=60)),
                ('real_name', models.CharField(max_length=60)),
                ('tz', models.CharField(max_length=60)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
