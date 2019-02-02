from django.contrib import admin
from .models import PiperDatabase


class piperdbAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'symbol',
        'opening_price',
        'high_price',
        'low_price',
        'closing_price',
        'timestamp'
    )

admin.site.register(PiperDatabase, piperdbAdmin)