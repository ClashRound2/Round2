# Generated by Django 2.1.1 on 2018-09-11 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20180911_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 16, 6, 27, 215004)),
        ),
    ]
