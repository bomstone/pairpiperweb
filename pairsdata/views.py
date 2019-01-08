import matplotlib as mpl
mpl.use('Agg')
from django.views.generic import TemplateView
import matplotlib.pyplot as plt
import io
from .pipercharts import *

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import Template, Context
import base64


class PairsdataView(TemplateView):
    template_name = 'pairsdata/pairsdata.html'

    def post(self, request):     #beskriver vad som händer vid post-request (sumbit i formuläret)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        ticker_1 = request.POST.get('ticker_1')
        ticker_2 = request.POST.get('ticker_2')
        symbol_list = [ticker_1, ticker_2]

        # Hämta data ur historisk databas+livedatabas
        price = fetch_data(symbol_list, 'closing_price', start_date, end_date)

        # Separera listan till två variabler
        S1 = price[symbol_list[0]]
        S2 = price[symbol_list[1]]

        # Beräkna spread
        S1 = sm.add_constant(S1)
        results = sm.OLS(S2, S1).fit()
        S1 = S1[symbol_list[0]]  # återställer S1
        b = results.params[symbol_list[0]]
        spread = S2 - b * S1

        # Beräkna omvänd spread
        S2 = sm.add_constant(S2)
        results = sm.OLS(S1, S2).fit()
        S2 = S2[symbol_list[1]]  # återställer S2
        b = results.params[symbol_list[1]]
        spread_rev = S1 - b * S2

        # Beräkna och plotta Zscore
        zscore(spread).plot(figsize=(9, 2))
        zscore2 = zscore(spread_rev)
        zscore2.plot(figsize=(9, 2))
        plt.axhline(zscore(spread).mean(), color='black')
        plt.axhline(1.0, color='red', linestyle='--')
        plt.axhline(-1.0, color='green', linestyle='--')
        plt.legend(['Spread ' + symbol_list[1], 'Spread ' + symbol_list[0]], bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                   ncol=1, mode="expand", borderaxespad=0.);

        f = io.BytesIO()

        plt.savefig(f,
                    format="png",
                    facecolor=(0.95, 0.95, 0.95),
                    bbox_inches='tight',
                    )
        plt.clf()

        image_b64 = base64.b64encode(f.getvalue()) #konverterar bilden till base64
        image_show = str(image_b64, 'utf8') #encodar till 8 bit strängar
        context = {'image_show': image_show,}
        return render(request, self.template_name, context)

