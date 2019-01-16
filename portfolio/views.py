from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

class PortfolioView(TemplateView):
    template_name = 'portfolio/portfolio.html'