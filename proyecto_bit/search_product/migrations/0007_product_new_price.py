# Generated by Django 3.0 on 2020-03-22 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_product', '0006_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
