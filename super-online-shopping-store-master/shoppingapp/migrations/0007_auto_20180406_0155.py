# Generated by Django 2.0.1 on 2018-04-05 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0006_buy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='address',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='city',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='date',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='mno',
        ),
    ]
