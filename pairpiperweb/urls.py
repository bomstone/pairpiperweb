"""pairpiperweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
import piperdatabase.views
from pairsdata.views import PairsdataView
import portfolio.views
import addposition.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pairsdata/', PairsdataView.as_view(), name='pairsdata'),
    path('piperdatabase/', piperdatabase.views.PiperdatabaseView, name='PiperdatabaseView'),
    path('piperdatabase/updatelive/', piperdatabase.views.updatelive),
    path('piperdatabase/updatehistorical/', piperdatabase.views.updatehistorical),
    path('portfolio/', portfolio.views.PortfolioView, name='PortfolioView'),
    path('addposition/', addposition.views.AddpositionView, name='AddpositionView')
]