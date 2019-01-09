from django.views.generic import TemplateView

from . import pipercharts as pp

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
# from django.template import Template, Context


class PairsdataView(TemplateView):
    template_name = 'pairsdata/pairsdata.html'

    def post(self, request):     #beskriver vad som händer vid post-request (sumbit i formuläret)

        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        ticker_1 = request.POST.get('ticker_1')
        ticker_2 = request.POST.get('ticker_2')
        symbol_list = [ticker_1, ticker_2]

        chart_1 = pp.draw_chart(symbol_list, start_date, end_date)
        chart_2 = pp.draw_chart(symbol_list, '2018-01-05', end_date)
        chart_3 = pp.draw_chart(symbol_list, '2018-05-01', end_date)


        context = {'chart_1': chart_1,
                   'chart_2': chart_2,
                   'chart_3': chart_3
                   }

        return render(request, self.template_name, context)

