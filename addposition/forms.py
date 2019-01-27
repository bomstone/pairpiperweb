from django import forms
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
    def save(self, strategy_in, user_in):
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
        strategy = strategy_in
        user = user_in

        instance.trade_id = trade_id
        instance.insert_type = insert_type
        instance.net_open_sek = open_price * quantity
        instance.true_exposure = (open_price * quantity) * (ul_open / open_price)
        instance.currency = currency
        instance.strategy = strategy
        instance.user = user

        instance.save()
        return instance


class GeneralPositionForm(forms.Form): #formulär för generell data som skrivs till både AddMainPosition och AddSubPosition
    user = forms.ChoiceField(choices=(('jesper', 'jesper'), ('mikael', 'mikael')))
    product_type = forms.ChoiceField(choices=(
        ('mini future', 'mini future'),
        ('stock', 'stock'),
        ('option', 'option'),
        ('ETF', 'ETF'),
        ('mixed', 'mixed')
    ))
    strategy = forms.CharField()

def AddMainPosition(strategy_in, user_in, open_date_in): #kallas i veiws och tar argument från GeneralPositionForm och AddSubpositionForm
    check_tradeid = PortfolioModel.objects.all().aggregate(Max('trade_id'))
    if not check_tradeid.get('trade_id__max'):
        trade_id = 1
    else:
        trade_id = check_tradeid.get('trade_id__max')


    instance = PortfolioModel.objects.create(

        trade_id=trade_id,
        insert_type='position',
        strategy=strategy_in,
        open_date=open_date_in,
        user=user_in,

    )
    instance.save()

