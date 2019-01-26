from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddSubpositionForm
from portfolio.models import PortfolioModel


def AddPositionView(request):

    if request.method == "POST":
        subposition = AddSubpositionForm(request.POST)

        if subposition.is_valid():
            subposition.save()

            return HttpResponseRedirect('/addposition/')

    else:
        subposition = AddSubpositionForm()

    return render(request, 'addposition/addposition.html', {'subposition': subposition})
