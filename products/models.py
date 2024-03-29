from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120) # max_length is required
    descriptions = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    summary = models.TextField(blank=False, null=True)
    featured = models.BooleanField(default=True)
