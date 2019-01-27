from django import forms
from django.forms import modelformset_factory
from portfolio.models import PortfolioModel
from django.db.models import Max


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

    # Override save-funktion och lägger till ytterligare metadata till positionen som ej fylls i genom formulär
    def save(self):
        instance = super(AddSubpositionForm, self).save(commit=False)

        check_tradeid = PortfolioModel.objects.all().aggregate(Max('trade_id'))
        if not check_tradeid.get('trade_id__max'):
            trade_id = 1
        else:
            trade_id = check_tradeid.get('trade_id__max') + 1

        insert_type = 'subposition'
        open_price = self.cleaned_data['open_price']
        ul_open = self.cleaned_data['ul_open']
        quantity = self.cleaned_data['quantity']
        currency = 'SEK'

        instance.trade_id = trade_id
        instance.insert_type = insert_type
        instance.net_open_sek = open_price * quantity
        instance.true_exposure = (open_price * quantity) * (ul_open / open_price)
        instance.currency = currency

        instance.save()
        return instance

class AddMainpositionForm(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = [
            'user',
            'strategy',
        ]
