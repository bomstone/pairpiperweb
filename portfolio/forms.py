from django import forms
from .models import PortfolioModel
from django.forms import modelformset_factory

class PortfoliopositionModelForm(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = [
            'product_type',
            'strategy',
            'open_date',
            'open_time',
            'asset',
            'ul_open',
            'open_price',
            'mf_finlevel',
            'quantity',
            'close_date',
            'close_time',
            'ul_close',
            'close_price',
            'commission',
        ]
        widgets = {
            'strategy': forms.TextInput(attrs={'size': 6}),
            'product_type': forms.TextInput(attrs={'size': 6}),
            'open_date': forms.TextInput(attrs={'size': 7}),
            'open_time': forms.TextInput(attrs={'size': 6}),
            'asset': forms.TextInput(attrs={'size': 6}),
            'ul_open': forms.TextInput(attrs={'size': 5}),
            'open_price': forms.TextInput(attrs={'size': 5}),
            'mf_finlevel': forms.TextInput(attrs={'size': 5}),
            'quantity': forms.TextInput(attrs={'size': 4}),
            'close_date': forms.TextInput(attrs={'size': 7}),
            'close_time': forms.TextInput(attrs={'size': 6}),
            'ul_close': forms.TextInput(attrs={'size': 6}),
            'close_price': forms.TextInput(attrs={'size': 6}),
            'commission': forms.TextInput(attrs={'size': 6}),

        }

PortfoliopositionFormset = modelformset_factory(
    PortfolioModel,
    form=PortfoliopositionModelForm,
)