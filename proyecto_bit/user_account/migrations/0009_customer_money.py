# Generated by Django 3.0 on 2020-03-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0008_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='money',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
