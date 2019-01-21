from django.db import models

class AddPositionmodel(models.Model):
    trade_id = models.IntegerField()
    strategy = models.CharField(max_length=30)
    product_type = models.CharField(max_length=30)
    open_date = models.CharField(max_length=30)
    open_time = models.CharField(max_length=30)
    true_exposure = models.DecimalField(max_digits=10, decimal_places=3)

    asset = models.CharField(max_length=30)
    ul_open = models.DecimalField(max_digits=10, decimal_places=3)
    open_price = models.DecimalField(max_digits=10, decimal_places=3)
    mf_finlevel = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField()
    commission = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta():
        db_table = 'portfolio'

