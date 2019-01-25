from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddSubpositionForm
from portfolio.models import PortfolioModel
from django.forms import modelformset_factory

def AddPositionView(request):
    AddSubpositionFormset = modelformset_factory(PortfolioModel, form=AddSubpositionForm, extra=2)
    formset = AddSubpositionFormset(request.POST)
    if request.method == "POST":

        if formset.is_valid():
            formset.save()
            """add = PortfolioModel(
                #strategy = request.POST.get['strategy'],
                #trade_id = form.cleaned_data['trade_id'],
                product_type = formset.cleaned_data['product_type'],
                open_date = formset.cleaned_data['open_date'],
                open_time = formset.cleaned_data['open_time'],
                #true_exposure = form.cleaned_data['true_exposure'],
                asset = formset.cleaned_data['asset'],
                ul_open = formset.cleaned_data['ul_open'],
                open_price = formset.cleaned_data['open_price'],
                mf_finlevel = formset.cleaned_data['mf_finlevel'],
                quantity = formset.cleaned_data['quantity'],
                commission = formset.cleaned_data['commission'],
               # user = request.POST.get['user'],
            )
            add.save()"""


    else:
        formset = AddSubpositionFormset()
    return render(request, 'addposition/addposition.html', {'formset': formset})





