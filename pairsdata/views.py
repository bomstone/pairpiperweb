from django.views.generic import TemplateView #TEMP
from django.shortcuts import render, HttpResponse
from pairsdata.forms import PairsdataForm

#def home(request):
    #return render(request, 'pairsdata/pairsdata.html')

class PairsdataView(TemplateView):
    template_name = 'pairsdata/pairsdata.html'

    def get(self, request):     #beskriver vad som händer vid get-request. Get-request skapas när sidan laddas (varför?)
        form = PairsdataForm()
        return render(request, self.template_name, {'form': form}) #renderar ett formulär enligt mallen PairsdataForm och returnerar

    def post(self, request):     #beskriver vad som händer vid post-request (sumbit i formuläret)
        form = PairsdataForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post'] #Cleaned_data ser till att texten som postats inte är skadlig

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)