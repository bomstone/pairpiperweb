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
            'strategy'
        ]
        labels = {
            'user': 'User',
            'product_type': 'Product type',
            'strategy': 'Strategy',
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
            'open_date',
            'open_time',
            'asset',
            'ul_open',
            'open_price',
            'mf_finlevel',
            'quantity',
        ]

    def save(self, **kwargs):
        instance = super(SubpositionModelForm, self).save(commit=False)

        check_tradeid = PortfolioModel.objects.all().aggregate(Max('trade_id'))
        trade_id = check_tradeid.get('trade_id__max')
        insert_type = 'subposition'
        open_price = self.cleaned_data['open_price']
        ul_open = self.cleaned_data['ul_open']
        quantity = self.cleaned_data['quantity']
        currency = 'SEK'
        strategy = kwargs['strategy_val']
        user = kwargs['user_val']

        instance.trade_id = trade_id
        instance.insert_type = insert_type
        instance.net_open_sek = 0 - (open_price * quantity)
        instance.true_exposure = (open_price * quantity) * (ul_open / open_price)
        instance.currency = currency
        instance.strategy = strategy
        instance.user = user

        instance.save()
        return instance



SubpositionFormset = modelformset_factory(
    PortfolioModel,
    form=SubpositionModelForm,
    extra=2,
)