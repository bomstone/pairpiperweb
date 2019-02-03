from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import PortfolioModel
from .forms import PortfoliopositionFormset


def PortfolioView(request):
    template_name = 'portfolio/portfolio.html'

    if request.method == "GET":
        portfolioposition = PortfoliopositionFormset(queryset=PortfolioModel.objects.all())

        context = {
            'portfolioposition': portfolioposition,
        }

        return render(request, template_name, context)

    elif request.method == "POST":

        queryset = PortfolioModel.objects.all()

        context = {
            'object_list': queryset,
        }

        return render(request, template_name, context)

