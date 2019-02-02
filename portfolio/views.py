from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import PortfolioModel


def PortfolioView(request):
    template_name = 'portfolio/portfolio.html'

    if request.method == "GET":
        queryset = PortfolioModel.objects.filter(trade_id=2)

        context = {
            'object_list': queryset,
        }

        return render(request, template_name, context)

    elif request.method == "POST":

        queryset = PortfolioModel.objects.filter(trade_id=2)

        context = {
            'object_list': queryset,
        }

        return render(request, template_name, context)

