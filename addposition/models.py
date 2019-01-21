from django.db import models

class AddPositionmodel(models.Model):
    strategy = models.CharField(max_length=30)
    product_type = models.CharField(max_length=30)

    class Meta():
        db_table = 'portfolio'

