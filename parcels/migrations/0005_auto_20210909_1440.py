# Generated by Django 3.1.5 on 2021-09-09 08:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parcels', '0004_auto_20210909_1431'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ParcelsModel',
            new_name='Parcels',
        ),
    ]
