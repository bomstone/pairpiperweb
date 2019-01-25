from django import forms
from django.forms import formset_factory


class AddPositionForm(forms.Form):
    trade_id = forms.IntegerField(required=False)

    strategy = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )

    user = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )


class AddSubpositionForm(forms.Form):
    open_date = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )

    open_time = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )

    target_exposure = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    asset = forms.CharField(
        required=False,
        max_length=12,
        widget=forms.TextInput(attrs={'size': 8})
    )

    ul_open = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    open_price = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    mf_finlevel = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    quantity = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

    commission = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'size': 8})
    )

AddSubpositionForm_FormSet = formset_factory(AddSubpositionForm)
