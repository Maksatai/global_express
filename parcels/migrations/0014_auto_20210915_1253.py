# Generated by Django 3.1.5 on 2021-09-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0013_auto_20210910_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcels',
            name='status',
            field=models.CharField(choices=[['unregistered_order', 'незарегистрированный заказ'], ['during', 'в процессе'], ['sorting', 'сортировка'], ['processed', 'обработан1'], ['processed1', 'обработан2'], ['processed2', 'обработан3'], ['In_stock_in_KG', 'на складе в Kg1'], ['In_stock_in_KG', 'на складе в Kg2'], ['In_stock_in_KG', 'на складе в Kg3']], default='unregistered_order', max_length=50),
        ),
    ]
