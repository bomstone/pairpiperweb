from django.contrib import admin
from .models import PortfolioModel


class portfolioAdmin(admin.ModelAdmin):
    list_display = (
        'trade_id',
        'insert_type',
        'strategy',
        'open_date',
        'open_time',
        'product_type',
        'asset',
        'currency',
        'open_price',
        'net_open_sek',
        'user',
    )

admin.site.register(PortfolioModel, portfolioAdmin)

