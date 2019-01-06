from django.urls import path
from pairsdata.views import PairsdataView


urlpatterns = [
    path('', PairsdataView.as_view(), name='pairsdata'),

]