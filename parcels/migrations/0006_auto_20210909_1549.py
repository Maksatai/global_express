# Generated by Django 3.1.5 on 2021-09-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0005_auto_20210909_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcels',
            name='comment',
            field=models.TextField(max_length=320, null=True),
        ),
    ]
