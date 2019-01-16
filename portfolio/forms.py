from django import forms


class Add_MiniFuture(forms.form):
    start_date_1 = forms.DateField()
    start_time_1 = forms.TimeField()
    exposure_1 = forms.DecimalField()

    ticker_1 = forms.CharField()
    ul_open_1 = forms.DecimalField()
    mf_open_1 = forms.DecimalField()
    mf_finlevel_1 = forms.DecimalField()
    quantity_1 = forms.IntegerField()
    commission_1 = forms.BooleanField()

    ticker_2 = forms.CharField()
    ul_open_2 = forms.DecimalField()
    mf_open_2 = forms.DecimalField()
    mf_finlevel_2 = forms.DecimalField()
    quantity_2 = forms.IntegerField()
    commission_2 = forms.BooleanField()

