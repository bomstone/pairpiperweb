from django import forms

class PairsdataForm(forms.Form):
    start_date = forms.CharField()
    end_date = forms.CharField()