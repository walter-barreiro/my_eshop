# Generated by Django 3.0 on 2020-04-02 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0004_auto_20200402_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datediscount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 10, 52, 32, 141524)),
        ),
    ]
