from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse


class PiperdatabaseView(TemplateView):
    template_name = 'piperdatabase/database.html'