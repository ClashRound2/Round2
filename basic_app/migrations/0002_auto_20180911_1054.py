# Generated by Django 2.1.1 on 2018-09-11 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='option',
            field=models.CharField(default='c', max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 10, 54, 36, 792203)),
        ),
    ]