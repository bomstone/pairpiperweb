from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from . import webscraper as ws

def PiperdatabaseView(request):
    return render(request, 'piperdatabase/database.html')

def updatelive(request):
    #ws.updatelivedb()
    update_live_message = ws.updatelivedb()
    context = {'update_live_message': update_live_message}
    return render(request, 'piperdatabase/database.html', context)

def updatehistorical(request):
    historical_date = request.POST.get('historical_date')
    #ws.updatehistoricaldb(historical_date)
    update_historical_message = ws.updatehistoricaldb(historical_date)
    context = {'update_historical_message': update_historical_message}
    return render(request, 'piperdatabase/database.html', context)


