from django.db import models

class PiperDatabase(models.Model):
    date = models.CharField(max_length=30, null=False)
    asset = models.CharField(max_length=30, null=False)
    open_price = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    high_price = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    low_price = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    close_price = models.DecimalField(max_digits=10, decimal_places=3, null=False)

    class Meta():
        db_table = 'piperdb'