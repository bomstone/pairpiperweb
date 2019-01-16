from django import forms

class AddTradeBasic(forms.Form):
    strategy = forms.ChoiceField()
    legs = forms.IntegerField()

class AddMiniFuture(forms.Form):
    start_date = forms.DateField()
    start_time = forms.TimeField()
    exposure = forms.DecimalField()

    ticker = forms.CharField()
    ul_open = forms.DecimalField()
    mf_open = forms.DecimalField()
    mf_finlevel = forms.DecimalField()
    quantity = forms.IntegerField()
    commission = forms.BooleanField()


