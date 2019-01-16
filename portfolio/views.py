from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddMiniFuture

def PortfolioView(request):
    form = AddMiniFuture()
    return render(request, 'portfolio/portfolio.html', {'form': form})

