# Generated by Django 3.1.5 on 2021-09-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0006_auto_20210909_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcels',
            name='comment',
            field=models.TextField(max_length=324, null=True),
        ),
    ]