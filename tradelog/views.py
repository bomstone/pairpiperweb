from django.shortcuts import render


def TradelogView(request):

    return render(request, 'tradelog/tradelog.html')