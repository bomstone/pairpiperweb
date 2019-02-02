from django import forms
from portfolio.models import PortfolioModel
from django.db.models import Max
from django.forms import modelformset_factory


class MainpositionModelForm(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = ('user', 'product_type', 'strategy')
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

SubpositionFormset = modelformset_factory(
    PortfolioModel,
    fields=('product_type', 'open_date', 'open_time', 'asset', 'ul_open', 'open_price', 'mf_finlevel', 'quantity'),
    extra=2,
)

'''
    check_tradeid = PortfolioModel.objects.all().aggregate(Max('trade_id'))
    if not check_tradeid.get('trade_id__max'):
        trade_id = 1
    else:
        trade_id = check_tradeid.get('trade_id__max')
'''