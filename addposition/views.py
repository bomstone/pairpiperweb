from django.shortcuts import render, HttpResponseRedirect
from .forms import MainpositionModelForm, SubpositionFormset
from portfolio.models import PortfolioModel
from portfolio.transfer import update_mainpos


def AddPositionView(request):
    template_name = 'addposition/addposition.html'

    if request.method == "GET":
        mainposition = MainpositionModelForm()
        subposition = SubpositionFormset(queryset=PortfolioModel.objects.none())


        context = {
            'subposition': subposition,
            'mainposition': mainposition,
        }

        return render(request, template_name, context)

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
            update_mainpos()

            return HttpResponseRedirect('/addposition/')






