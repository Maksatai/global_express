from django.db import models
from datetime import datetime

class ParcelsModel(models.Model):
    date = models.DateTimeField(default = datetime.now, blank = True)
    number = models.PositiveIntegerField(null = False)
    recipient = models.CharField(null = False, max_length = 100)
    parcels_name = models.CharField(null = False, max_length = 100)
    amount = models.PositiveIntegerField(null = True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    country = models.CharField(null = False, max_length =100)
    status = models.BooleanField(default = False)

