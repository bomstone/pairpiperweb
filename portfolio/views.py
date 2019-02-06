from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import PortfolioModel
from .forms import PortfoliopositionFormset


def PortfolioView(request):
    template_name = 'portfolio/portfolio.html'

    if request.method == "GET":

        portfolioposition = PortfoliopositionFormset(queryset=PortfolioModel.objects.filter(trade_id=2))

        context = {
            'portfolioposition': portfolioposition,
        }

        return render(request, template_name, context)

    elif request.method == "POST":

        portfolioposition = PortfoliopositionFormset(request.POST)

        if portfolioposition.is_valid():

            for form in portfolioposition:
                form.save()

            return HttpResponseRedirect('/portfolio/')

        else:
            print(portfolioposition.errors)

