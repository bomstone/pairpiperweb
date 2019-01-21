from django.db import models

# Create your models here.
class PortfolioPart(models.Model):
    trade_id = models.IntegerField(default=None, null=True)
    trade_type = models.CharField(max_length=30, default=None, null=True)
    strategy = models.CharField(max_length=30, default=None, null=True)
    product_type = models.CharField(max_length=30, default=None, null=True)
    asset = models.CharField(max_length=30, default=None, null=True)
    currency = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    open_date = models.CharField(max_length=30, default=None, null=True)
    open_time = models.CharField(max_length=30, default=None, null=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    ul_open = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    true_exposure = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    fx_open = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    net_open_sek = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    quantity = models.IntegerField(default=None, null=True)
    close_date = models.CharField(max_length=30, default=None, null=True)
    close_time = models.CharField(max_length=30, default=None, null=True)
    ul_close = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    fx_close = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    net_close_sek = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    commission = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    net_result_sek = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    mf_finlevel = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    opt_type = models.CharField(max_length=30, default=None, null=True)
    opt_date = models.CharField(max_length=30, default=None, null=True)
    opt_strie = models.DecimalField(max_digits=10, decimal_places=3, default=None, null=True)
    user = models.CharField(max_length=30, default=None, null=True)

    class Meta():
        db_table = 'portfolio'


