from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


class PortfolioView(TemplateView):
    template_name = 'portfolio/portfolio.html'

    variable1 = 'test1'
    variable2 = 'test2'

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        context['variable1'] = self.variable1
        context['variable2'] = self.variable2
        return context

        return render(request, self.template_name, context)

