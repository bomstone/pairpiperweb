from django import forms
from django.forms import ModelForm

from portfolio.models import PortfolioModel

class AddSubpositionForm(ModelForm):
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
            'commission',
        ]
        """widgets = {
            'open_date': Textarea(attrs={'cols': 120, 'rows': 20}),
        }"""



"""
class AddMainpositionForm(forms.Form):
    trade_id = forms.IntegerField(required=False)

    strategy = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )

    user = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )


class AddSubpositionForm(forms.Form):
    open_date = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )

    open_time = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )

    target_exposure = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    asset = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )

    ul_open = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    open_price = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    mf_finlevel = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    quantity = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    commission = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

"""
