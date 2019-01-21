from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import PortfolioPart


class PortfolioView(TemplateView):
    template_name = 'portfolio/portfolio.html'
    def PrintPortfolio(request):
        template_name = 'portfolio/portfolio.html'

        queryset = PortfolioPart.objects.all()
        context = {
            'object_list': queryset,
            'title:': 'List'
        }

        return render(request, self.template_name, context)
'''
    variable1 = 'test1'
    variable2 = 'test2'

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        context['variable1'] = self.variable1
        context['variable2'] = self.variable2
        return context

        return render(request, self.template_name, context)'''

