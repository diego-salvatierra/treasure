# Generated by Django 2.0.2 on 2018-02-16 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20180216_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.IntegerField(choices=[(0, 'waiting for players'), (1, 'playing'), (2, 'complete'), (3, 'cancelled')]),
        ),
        migrations.AlterField(
            model_name='gameturnplay',
            name='played_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
