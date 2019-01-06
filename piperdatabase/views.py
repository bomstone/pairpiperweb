from django.shortcuts import render, HttpResponse
from django.template import loader


def PiperdatabaseView(request):
    return render(request, 'piperdatabase/database.html')

def updatelive(request):
    return HttpResponse('updatelive')

def updatehistorical(request):
    return HttpResponse('updatehistorical')