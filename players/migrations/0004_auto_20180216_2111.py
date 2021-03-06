# Generated by Django 2.0.2 on 2018-02-16 21:11

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20180210_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 1, 1, 1, 1, 1, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameturnplay',
            name='played_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 1, 1, 1, 1, 1, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
