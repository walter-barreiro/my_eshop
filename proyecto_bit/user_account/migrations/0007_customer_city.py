# Generated by Django 3.0 on 2020-03-14 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0006_customer_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
