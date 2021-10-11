from django.db import models

class update_price(models.Model):
    name = models.CharField(max_length=50, null=False)
    rate = models.IntegerField(null=False)
