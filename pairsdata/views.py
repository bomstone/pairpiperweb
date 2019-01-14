from django.views.generic import TemplateView
import datetime
from . import pipercharts as pp
from django.shortcuts import render, HttpResponse, HttpResponseRedirect


todays_date = datetime.datetime.now()

class PairsdataView(TemplateView):
    template_name = 'pairsdata/pairsdata.html'

    def post(self, request):     #beskriver vad som händer vid post-request (sumbit i formuläret)

        start_date = request.POST.get('start_date_textbox')
        end_date = request.POST.get('end_date_textbox')
        symbol_list = [request.POST.get('ticker_1_droplist'), request.POST.get('ticker_2_droplist')]

        chart_1 = pp.draw_chart(symbol_list, start_date, end_date)
        chart_2 = pp.draw_chart(symbol_list, '2018-05-05', end_date)
        chart_3 = pp.draw_chart(symbol_list, '2018-01-01', end_date)


        context = {'chart_1': chart_1,
                   'chart_2': chart_2,
                   'chart_3': chart_3,
                   }

        return render(request, self.template_name, context)

