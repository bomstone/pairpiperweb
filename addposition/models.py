from django.db import models

class AddPositionmodel(models.Model):
    trade_id = models.IntegerField()
    trade_type = models.CharField(max_length=30)
    strategy = models.CharField(max_length=30)
    product_type = models.CharField(max_length=30)
    asset = models.CharField(max_length=30)
    currency = models.DecimalField(max_digits=10, decimal_places=3)
    open_date = models.CharField(max_length=30)
    open_time = models.CharField(max_length=30)
    open_price = models.DecimalField(max_digits=10, decimal_places=3)
    ul_open = models.DecimalField(max_digits=10, decimal_places=3)
    true_exposure = models.DecimalField(max_digits=10, decimal_places=3)
    fx_open = models.DecimalField(max_digits=10, decimal_places=3)
    net_open_sek = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField()
    close_date = models.CharField(max_length=30)
    close_time = models.CharField(max_length=30)
    ul_close = models.DecimalField(max_digits=10, decimal_places=3)
    fx_close = models.DecimalField(max_digits=10, decimal_places=3)
    net_close_sek = models.DecimalField(max_digits=10, decimal_places=3)
    commission = models.DecimalField(max_digits=10, decimal_places=3)
    net_result_sek = models.DecimalField(max_digits=10, decimal_places=3)
    mf_finlevel = models.DecimalField(max_digits=10, decimal_places=3)
    opt_type = models.CharField(max_length=30)
    opt_date = models.CharField(max_length=30)
    opt_strie = models.DecimalField(max_digits=10, decimal_places=3)
    user = models.CharField(max_length=30)

    class Meta():
        db_table = 'portfolio'

