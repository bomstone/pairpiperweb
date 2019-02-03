from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import PortfolioModel
from .forms import PortfoliopositionFormset


def PortfolioView(request):
    template_name = 'portfolio/portfolio.html'

    if request.method == "GET":


        portfolioposition = PortfolioModel.objects.filter(trade_id=3)

        portfolioobject = PortfoliopositionFormset(queryset=portfolioposition)

        context = {
            'portfolioposition': portfolioposition,
            'portfolioobject': portfolioobject,
        }

        return render(request, template_name, context)

    elif request.method == "POST":

        portfolioobject = PortfoliopositionFormset(request.POST)

        if portfolioobject.is_valid():
            portfolioobject.save()

        return HttpResponseRedirect('/portfolio/')

