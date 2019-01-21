from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddPosition
from addposition.models import AddPositionmodel

def AddpositionView(request):
    '''add = AddPositionmodel(strategy='test', product_type='product')
    add.save(using='piperdb')
    return render(request, 'addposition/addposition.html')'''


    if request.method == "POST":
        form = AddPosition(request, POST)

        add = AddPositionmodel(
            strategy = form.cleaned_data['strategy'],
            id = form.cleaned_data['id'],
            product_type = form.cleaned_data['product_type'],

            start_date = form.cleaned_data['start_date'],
            start_time = form.cleaned_data['start_time'],
            exposure = form.cleaned_data['exposure'],

            ticker = form.cleaned_data['ticker'],
            ul_open = form.cleaned_data['ul_open'],
            mf_open = form.cleaned_data['mf_open'],
            mf_finlevel = form.cleaned_data['mf_finlevel'],
            quantity = form.cleaned_data['quantity'],
            commission = form.cleaned_data['commission']
        )

        add.save(using='piperdb')
        return render(request, 'addposition/addposition.html')

    form = AddPosition()
    return render(request, 'addposition/addposition.html', {'form': form})




