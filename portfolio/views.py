from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def PortfolioView(request):

    return render(request, 'portfolio/portfolio.html')

