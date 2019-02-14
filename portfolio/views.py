from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import PortfolioModel
from .forms import PortfoliopositionFormset
from .transfer import transfer_tolog
from itertools import chain
from django.db.models import Max


def PortfolioView(request):
    template_name = 'portfolio/portfolio.html'

    if request.method == "GET":

        portfolio_position = PortfoliopositionFormset(queryset=PortfolioModel.objects.filter(insert_type='position'))
        portfolio_object = PortfoliopositionFormset(queryset=PortfolioModel.objects.filter(insert_type='position'))

        context = {
            'portfolio_position': portfolio_position,
            'portfolio_object': portfolio_object,
        }

        return render(request, template_name, context)

    elif request.method == "POST":

        portfolio_object = PortfoliopositionFormset(request.POST)

        if portfolio_object.is_valid():

            for form in portfolio_object:

                form.save()

            trade_id_val = form.cleaned_data['trade_id']
            transfer_tolog(trade_id_val)
            return HttpResponseRedirect('/portfolio/')

        else:
            print(portfolio_object.errors)

