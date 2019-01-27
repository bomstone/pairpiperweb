from django.shortcuts import render, HttpResponseRedirect
from .forms import AddSubpositionForm, AddMainPosition, GeneralPositionForm


def AddPositionView(request):

    if request.method == "POST":
        subposition = AddSubpositionForm(request.POST)
        generalposition = GeneralPositionForm(request.POST)

        if subposition.is_valid():
            strategy_val = request.POST.get('strategy')
            user_val = request.POST.get('user')
            open_date_val = subposition.cleaned_data.get('open_date')


            subposition.save(strategy_val, user_val)
            AddMainPosition(strategy_val, user_val, open_date_val)

            return HttpResponseRedirect('/addposition/')

    else:
        subposition = AddSubpositionForm()
        generalposition = GeneralPositionForm()

    context = {
        'subposition': subposition,
        'generalposition': generalposition,
    }

    return render(request, 'addposition/addposition.html', context)
