# Generated by Django 3.1.7 on 2022-05-15 02:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20220509_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='dateApproved',
        ),
        migrations.RemoveField(
            model_name='news',
            name='isApproved',
        ),
        migrations.AddField(
            model_name='news',
            name='lastModified',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 2, 53, 22, 970669, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 2, 53, 22, 970669, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
