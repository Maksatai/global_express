from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

class Parcels(models.Model):
    order = ForeignKey(User, on_delete=models.CASCADE, default=True)
    date = models.DateField(blank=False, auto_now=True)
    recipient = models.CharField(max_length = 100)
    parcels_name = models.CharField(null = False, max_length = 100)
    amount = models.PositiveIntegerField(null = True)
    price = models.DecimalField(default = 0.00, max_digits=10, decimal_places=2)
    weight = models.DecimalField(default = 0.00, max_digits=10, decimal_places=2)
    country = models.CharField(max_length=100, verbose_name=u"Страна")
    treck = models.CharField(max_length=50, null=False, unique=True, default=False)
    status = models.BooleanField(default = False)
    category = models.CharField(max_length=100,null=False,default=False)
    web_site = models.URLField(max_length=200,null=False,default=False)
    comment = models.TextField(max_length=324,null=True)

    def __str__(self):
        return self.parcels_name