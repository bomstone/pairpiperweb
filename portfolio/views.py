from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddPosition

def PortfolioView(request):
    if request.method == "POST":
        form = AddPosition(request, POST)


        strategy = form.cleaned_data['strategy']
        legs = form.cleaned_data['legs']

        start_date = form.cleaned_data['start_date']
        start_time = form.cleaned_data['start_time']
        exposure = form.cleaned_data['exposure']

        ticker = form.cleaned_data['ticker']
        ul_open = form.cleaned_data['ul_open']
        mf_open = form.cleaned_data['mf_open']
        mf_finlevel = form.cleaned_data['mf_finlevel']
        quantity = form.cleaned_data['quantity']
        commission = form.cleaned_data['commission']

        print(ul_open, ticker)

    form = AddPosition()
    return render(request, 'portfolio/portfolio.html', {'form': form})

