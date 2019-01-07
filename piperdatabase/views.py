from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import webscraper


def PiperdatabaseView(request):
    return render(request, 'piperdatabase/database.html')

def updatelive(request):
    webscraper.updatelivedb()
    return HttpResponseRedirect('/piperdatabase')

def updatehistorical(request):

    return HttpResponseRedirect('/piperdatabase')