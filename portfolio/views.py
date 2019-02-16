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

        id_list = []
        queryset = PortfolioModel.objects.filter(insert_type='position')
        for obj in queryset:
            id_list.append(obj.trade_id)

        portfolio_object = PortfoliopositionFormset(queryset=PortfolioModel.objects.all())
        context = {
            'portfolio_object': portfolio_object,
            'id_list': id_list,
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

