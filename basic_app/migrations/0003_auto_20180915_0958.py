# Generated by Django 2.1.1 on 2018-09-15 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20180913_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='totalScore',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 15, 9, 58, 9, 499777)),
        ),
    ]
