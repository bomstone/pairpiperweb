from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse


class PairsdataView(TemplateView):
    template_name = 'pairsdata/pairsdata.html'

    def post(self, request):     #beskriver vad som händer vid post-request (sumbit i formuläret)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        ticker_1 = request.POST.get('ticker_1')
        ticker_2 = request.POST.get('ticker_2')
        assets = [ticker_1, ticker_2]

        args = {'start_date': start_date, 'end_date': end_date, 'ticker_1': ticker_1, 'ticker_2': ticker_2}
        return render(request, self.template_name, args)