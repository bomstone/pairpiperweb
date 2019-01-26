from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddSubpositionForm
from django.forms import modelformset_factory

def AddPositionView(request):

    subposition = AddSubpositionForm(request.POST)

    if request.method == "POST":

        if subposition.is_valid():
            add_subposition = subposition.save()


    subposition = AddSubpositionForm()
    return render(request, 'addposition/addposition.html', {'subposition': subposition})
