from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import webscraper

def PiperdatabaseView(request):
    return render(request, 'piperdatabase/database.html')

def updatelive(request):
    webscraper.updatelivedb()
    return HttpResponseRedirect('/piperdatabase')

def updatehistorical(request):
    historical_date = request.POST.get('historical_date')
    webscraper.updatehistoricaldb(historical_date)
    return HttpResponseRedirect('/piperdatabase')