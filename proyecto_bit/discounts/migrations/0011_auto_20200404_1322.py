# Generated by Django 3.0.4 on 2020-04-04 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0010_auto_20200403_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datediscount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 4, 13, 22, 41, 1746)),
        ),
    ]
