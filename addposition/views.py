from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddMainpositionForm, AddSubpositionForm_FormSet
from portfolio.models import PortfolioModel

def AddPositionView(request):

    if request.method == "POST":

        add = PortfolioModel(
            strategy = form.cleaned_data['strategy'],
            #trade_id = form.cleaned_data['trade_id'],
            product_type = form.cleaned_data['product_type'],
            open_date = form.cleaned_data['open_date'],
            open_time = form.cleaned_data['open_time'],
            #true_exposure = form.cleaned_data['true_exposure'],
            asset = form.cleaned_data['asset'],
            ul_open = form.cleaned_data['ul_open'],
            open_price = form.cleaned_data['open_price'],
            mf_finlevel = form.cleaned_data['mf_finlevel'],
            quantity = form.cleaned_data['quantity'],
            commission = form.cleaned_data['commission'],
            user = form.cleaned_data['user'],
        )
        add.save()

        context = {
            'mainform': AddMainpositionForm(),
            'subform': AddSubpositionForm_FormSet()
        }
        return render(request, 'addposition/addposition.html', context)


    context = {
        'mainform': AddMainpositionForm,
        'subform': AddSubpositionForm_FormSet
        }
    return render(request, 'addposition/addposition.html', context)




