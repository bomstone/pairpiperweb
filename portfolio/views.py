from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import PortfolioPart


def PrintPortfolio(request):
    template_name = 'portfolio/portfolio.html'

    queryset = PortfolioPart.objects.all()
    context = {
        'object_list': queryset,
    }

    return render(request, template_name, context)