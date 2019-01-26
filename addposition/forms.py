from django import forms
from django.forms import modelformset_factory
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
    def save(self):
        instance = super(AddSubpositionForm, self).save(commit=False)
        instance.insert_type = 'subposition'
        instance.save()
        return instance

class AddMainpositionForm(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = [
            'user',
            'strategy',
        ]
