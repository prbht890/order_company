from django.db import models

from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length = 100)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    