# Generated by Django 3.1.5 on 2021-09-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0002_auto_20210909_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcelsmodel',
            name='treck',
            field=models.CharField(default=False, max_length=50, unique=True),
        ),
    ]
