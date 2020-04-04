# Generated by Django 3.0 on 2020-04-03 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0018_auto_20200403_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='buy_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='pay_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 18, 43, 18, 900816), null=True),
        ),
    ]
