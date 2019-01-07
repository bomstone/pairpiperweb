from django.views.generic import TemplateView
from . import pipercharts as pc
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import Template, Context

class PairsdataView(TemplateView):
    template_name = 'pairsdata/pairsdata.html'

    def post(self, request):     #beskriver vad som händer vid post-request (sumbit i formuläret)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        ticker_1 = request.POST.get('ticker_1')
        ticker_2 = request.POST.get('ticker_2')
        assets = [ticker_1, ticker_2]

        pc.plot_chart(assets, start_date, end_date)

        return render(request, self.template_name)

