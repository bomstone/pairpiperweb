from django import forms

class AddPosition(forms.Form):
    id = forms.IntegerField(required=False)
    strategy = forms.CharField(required=False)
    product_type = forms.CharField(required=False)

    start_date = forms.DateField(required=False)
    start_time = forms.TimeField(required=False)
    exposure = forms.DecimalField(required=False)

    ticker = forms.CharField(required=False)
    ul_open = forms.DecimalField(required=False)
    mf_open = forms.DecimalField(required=False)
    mf_finlevel = forms.DecimalField(required=False)
    quantity = forms.IntegerField(required=False)
    commission = forms.DecimalField(required=False)


