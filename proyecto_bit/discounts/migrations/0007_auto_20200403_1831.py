# Generated by Django 3.0 on 2020-04-03 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0006_auto_20200403_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datediscount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 18, 31, 48, 769213)),
        ),
    ]
