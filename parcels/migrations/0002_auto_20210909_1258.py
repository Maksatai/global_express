# Generated by Django 3.1.5 on 2021-09-09 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parcels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcelsmodel',
            name='number',
        ),
        migrations.AddField(
            model_name='parcelsmodel',
            name='order',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parcelsmodel',
            name='country',
            field=models.CharField(choices=[['korea', 'Корея'], ['turkey', 'Турция'], ['chine', 'Китай']], default='korea', max_length=100, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='parcelsmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='parcelsmodel',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10),
        ),
        migrations.AlterField(
            model_name='parcelsmodel',
            name='weight',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10),
        ),
    ]
