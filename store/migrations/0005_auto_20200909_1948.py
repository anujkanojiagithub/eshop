# Generated by Django 3.1 on 2020-09-09 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]
