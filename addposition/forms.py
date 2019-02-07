from django import forms
from portfolio.models import PortfolioModel
from django.db.models import Max
from django.forms import modelformset_factory


class MainpositionModelForm(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = [
            'user',
            'product_type',
            'strategy',
            'asset',
            'currency',
            'open_date',
            'open_time',
            'ul_open',
            'fx_open',
            'open_price',
            'quantity',
            'mf_finlevel',
            'opt_date',
            'opt_strike',
        ]

        widgets = {
            'user': forms.Select,
            'product_type': forms.Select,
            'strategy': forms.Select,
            'asset': forms.TextInput(attrs={'size': 8}),
            'currency': forms.TextInput(attrs={'size': 5}),
            'open_date': forms.TextInput(attrs={'size': 8}),
            'open_time': forms.TextInput(attrs={'size': 8}),
            'ul_open': forms.TextInput(attrs={'size': 8}),
            'fx_open': forms.TextInput(attrs={'size': 5}),
            'open_price': forms.TextInput(attrs={'size': 8}),
            'mf_finlevel': forms.TextInput(attrs={'size': 5}),
            'quantity': forms.TextInput(attrs={'size': 2}),
            'opt_date': forms.TextInput(attrs={'size': 6}),
            'opt_strike': forms.TextInput(attrs={'size': 4}),
        }

    def save(self):
        instance = super(MainpositionModelForm, self).save(commit=False)

        check_tradeid = PortfolioModel.objects.all().aggregate(Max('trade_id'))
        if not check_tradeid.get('trade_id__max'):
            trade_id = 1
        else:
            trade_id = check_tradeid.get('trade_id__max') + 1

        instance.trade_id = trade_id
        instance.insert_type = 'position'

        instance.save()
        return instance


class SubpositionModelForm(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = [
            'product_type',
            'asset',
            'currency',
            'open_date',
            'open_time',
            'ul_open',
            'fx_open',
            'quantity',
            'open_price',
            'mf_finlevel',
            'opt_date',
            'opt_strike',
        ]
        widgets = {
            'product_type': forms.Select,
            'asset': forms.TextInput(attrs={'size': 8}),
            'currency': forms.TextInput(attrs={'size': 5}),
            'open_date': forms.TextInput(attrs={'size': 8}),
            'open_time': forms.TextInput(attrs={'size': 8}),
            'ul_open': forms.TextInput(attrs={'size': 8}),
            'fx_open': forms.TextInput(attrs={'size': 5}),
            'open_price': forms.TextInput(attrs={'size': 8}),
            'mf_finlevel': forms.TextInput(attrs={'size': 5}),
            'quantity': forms.TextInput(attrs={'size': 2}),
            'opt_date': forms.TextInput(attrs={'size': 6}),
            'opt_strike': forms.TextInput(attrs={'size': 4}),

        }

    def save(self, **kwargs):
        instance = super(SubpositionModelForm, self).save(commit=False)

        check_tradeid = PortfolioModel.objects.all().aggregate(Max('trade_id'))
        trade_id = check_tradeid.get('trade_id__max')
        insert_type = 'subposition'
        open_price = self.cleaned_data['open_price']
        ul_open = self.cleaned_data['ul_open']
        quantity = self.cleaned_data['quantity']
        strategy = kwargs['strategy_val']
        user = kwargs['user_val']

        instance.trade_id = trade_id
        instance.insert_type = insert_type
        instance.net_open_sek = 0 - (open_price * quantity)
        instance.true_exposure = (open_price * quantity) * (ul_open / open_price)
        instance.strategy = strategy
        instance.user = user

        instance.save()
        return instance



SubpositionFormset = modelformset_factory(
    PortfolioModel,
    form=SubpositionModelForm,
    extra=2,
)