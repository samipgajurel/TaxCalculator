# Generated by Django 3.1.7 on 2022-03-29 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='dateApproved',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 17, 43, 10, 951773, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='news',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 17, 43, 10, 951773, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='news',
            name='headline',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
