# Generated by Django 2.1.1 on 2018-09-13 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20180912_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='subtime',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 13, 14, 25, 46, 646681)),
        ),
    ]
