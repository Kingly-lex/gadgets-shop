# Generated by Django 5.0.1 on 2024-02-17 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_deliveryaddress'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeliveryAddress',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
