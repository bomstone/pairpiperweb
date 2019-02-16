from django.shortcuts import render, HttpResponseRedirect
from .models import PortfolioModel
from .forms import PortfoliopositionFormset
from .transfer import transfer_tolog


def PortfolioView(request):
    template_name = 'portfolio/portfolio.html'

    if request.method == "GET":

        id_list = []
        queryset = PortfolioModel.objects.filter(insert_type='position')
        for obj in queryset:
            id_list.append(obj.trade_id)

        portfolio_object = PortfoliopositionFormset(queryset=PortfolioModel.objects.all())
        context = {
            'portfolio_object': portfolio_object,
            'id_list': id_list,
        }

        return render(request, template_name, context)

    elif request.method == "POST":

        portfolio_object = PortfoliopositionFormset(request.POST)
        trade_id_val = 0

        for form in portfolio_object:
            if form.is_valid():
                form.save()
                trade_id_val = form.cleaned_data['trade_id']
        transfer_tolog(trade_id_val)

        return HttpResponseRedirect('/portfolio/')


