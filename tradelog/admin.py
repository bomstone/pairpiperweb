from django.contrib import admin
from .models import TradelogModel


class tradelogAdmin(admin.ModelAdmin):
    list_display = (
        'trade_id',
        'insert_type',
        'strategy',
        'open_date',
        'product_type',
        'asset',
        'close_date',
        'net_result_sek',
        'user',
    )

admin.site.register(TradelogModel, tradelogAdmin)

