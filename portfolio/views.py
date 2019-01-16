from django.shortcuts import render, HttpResponse, HttpResponseRedirect


class PortfolioView(TemplateView):
    template_name = 'portfolio/portfolio.html'