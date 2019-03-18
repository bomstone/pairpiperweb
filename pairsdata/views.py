from django.views.generic import TemplateView
from datetime import datetime, timedelta
from . import pipercharts as pp
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from piperdatabase.symbols import symbolList


class PairsdataView(TemplateView):
    template_name = 'pairsdata/pairsdata.html'
    todays_date = datetime.now().strftime("%Y-%m-%d")
    today_minus = (datetime.today() - timedelta(days=120)).strftime('%Y-%m-%d')

    def get_context_data(self, **kwargs):
        context = super(PairsdataView, self).get_context_data(**kwargs)
        context['todays_date'] = self.todays_date
        context['today_minus'] = self.today_minus
        context['symbol_list'] = symbolList
        return {
            'todays_date': datetime.now().strftime("%Y-%m-%d"),
            'today_minus': (datetime.today() - timedelta(days=120)).strftime('%Y-%m-%d'),
            'symbol_list': symbolList,
           }


    def post(self, request):     #beskriver vad som händer vid post-request (sumbit i formuläret)

        start_date = request.POST.get('start_date_textbox')
        end_date = request.POST.get('end_date_textbox')
        asset_1 = request.POST.get('ticker_1_droplist')
        asset_2 = request.POST.get('ticker_2_droplist')
        symbol_list = [asset_1, asset_2]

        chart_1 = pp.draw_spread(symbol_list, start_date, end_date)
        chart_2 = pp.draw_spread(symbol_list, '2018-05-05', end_date)
        chart_3 = pp.draw_spread(symbol_list, '2018-01-04', end_date)
        chart_11 = pp.draw_price(symbol_list, start_date, end_date)
        chart_21 = pp.draw_price(symbol_list, '2018-05-05', end_date)
        chart_31 = pp.draw_price(symbol_list, '2018-01-04', end_date)

        context = {
            'chart_1': chart_1,
            'chart_2': chart_2,
            'chart_3': chart_3,
            'chart_11': chart_11,
            'chart_21': chart_21,
            'chart_31': chart_31,
            'todays_date': datetime.now().strftime("%Y-%m-%d"),
            'today_minus': (datetime.today() - timedelta(days=120)).strftime('%Y-%m-%d'),
            'symbol_list': symbolList,
            }

        return render(request, self.template_name, context,)

