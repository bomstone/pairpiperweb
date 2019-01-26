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
from django.views.generic.base import TemplateView
from django.contrib import admin
import piperdatabase.views
from pairsdata.views import PairsdataView
import portfolio.views
import addposition.views
import tradelog.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('pairsdata/', PairsdataView.as_view(), name='pairsdata'),
    path('piperdatabase/', piperdatabase.views.PiperdatabaseView, name='PiperdatabaseView'),
    path('piperdatabase/updatelive/', piperdatabase.views.updatelive),
    path('piperdatabase/updatehistorical/', piperdatabase.views.updatehistorical),
    path('portfolio/', portfolio.views.PortfolioView, name='PortfolioView'),
    path('addposition/', addposition.views.AddPositionView, name='AddpositionView'),
    path('tradelog/', tradelog.views.TradelogView, name='TradelogView'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)