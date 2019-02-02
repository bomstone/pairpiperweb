from django.shortcuts import render, HttpResponseRedirect
from .forms import MainpositionModelForm, SubpositionFormset
from django.forms import modelformset_factory
from portfolio.models import PortfolioModel


def AddPositionView(request):

    if request.method == "GET":
        mainposition = MainpositionModelForm()
        subposition = SubpositionFormset(queryset=PortfolioModel.objects.none())


        context = {
            'subposition': subposition,
            'mainposition': mainposition,
        }

        return render(request, 'addposition/addposition.html', context)

    elif request.method == "POST":

        mainposition = MainpositionModelForm(request.POST)
        subposition = SubpositionFormset(request.POST)

        if mainposition.is_valid() and subposition.is_valid():



            mainposition.save()

            for form in subposition:
                form.save(
                    strategy_val=request.POST.get('strategy'),
                    user_val=request.POST.get('user'),
                    )

            return HttpResponseRedirect('/addposition/')






