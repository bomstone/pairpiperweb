from django import forms

class AddPositionform(forms.Form):
    trade_id = forms.IntegerField(required=False)
    strategy = forms.CharField(required=False)
    product_type = forms.CharField(required=False)

    open_date = forms.CharField(required=False)
    open_time = forms.CharField(required=False)
    true_exposure = forms.DecimalField(required=False)

    asset = forms.CharField(required=False)
    ul_open = forms.DecimalField(required=False)
    open_price = forms.DecimalField(required=False)
    mf_finlevel = forms.DecimalField(required=False)
    quantity = forms.IntegerField(required=False)
    commission = forms.DecimalField(required=False)


