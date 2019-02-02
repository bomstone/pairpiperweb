from django.contrib import admin
from .models import PortfolioModel


class portfolioAdmin(admin.ModelAdmin):
    list_display = (
        'trade_id',
        'insert_type',
        'strategy',
        'product_type',
        'asset',
        'open_date'
    )

admin.site.register(PortfolioModel, portfolioAdmin)

