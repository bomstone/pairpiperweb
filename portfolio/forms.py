from django import forms
from .models import PortfolioModel
from django.forms import modelformset_factory

class PortfoliopositionModelForm(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = [
            'trade_id',
            'insert_type',
            'strategy',
            'product_type',
            'open_date',
            'open_time',
            'asset',
            'ul_open',
            'open_price',
            'quantity',
            'close_date',
            'close_time',
            'ul_close',
            'close_price',
            'commission',
            'user',
        ]
        widgets = {
            'trade_id': forms.HiddenInput(),
            'insert_type': forms.HiddenInput(),
            'strategy': forms.TextInput(attrs={'size': 6}),
            'product_type': forms.TextInput(attrs={'size': 6}),
            'open_date': forms.TextInput(attrs={'size': 7}),
            'open_time': forms.TextInput(attrs={'size': 6}),
            'asset': forms.TextInput(attrs={'size': 10}),
            'ul_open': forms.TextInput(attrs={'size': 5}),
            'open_price': forms.TextInput(attrs={'size': 5}),
            'quantity': forms.TextInput(attrs={'size': 4}),
            'close_date': forms.TextInput(attrs={'size': 7}),
            'close_time': forms.TextInput(attrs={'size': 6}),
            'ul_close': forms.TextInput(attrs={'size': 6}),
            'close_price': forms.TextInput(attrs={'size': 6}),
            'commission': forms.TextInput(attrs={'size': 6}),
            'user': forms.TextInput(attrs={'size': 6}),

        }

    def save(self):
        instance = super(PortfoliopositionModelForm, self).save(commit=False)

        close_price = self.cleaned_data['close_price']
        quantity = self.cleaned_data['quantity']

        instance.net_close_sek = close_price * quantity

        instance.save()
        return instance

    def get_subpositions(self):
        return PortfolioModel.objects.filter(insert_type='subposition')

PortfoliopositionFormset = modelformset_factory(
    PortfolioModel,
    form=PortfoliopositionModelForm,
    extra=0,
)