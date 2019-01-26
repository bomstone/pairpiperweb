from django import forms
from portfolio.models import PortfolioModel


class AddSubpositionForm(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = [
            'product_type',
            'open_date',
            'open_time',
            'asset',
            'ul_open',
            'open_price',
            'mf_finlevel',
            'quantity',
        ]
        """
        widgets = {
            'open_date': Textarea(attrs={'cols': 120, 'rows': 20}),
        }
        """


class AddMainpositionForm(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = [
            'user',
            'strategy',
        ]
