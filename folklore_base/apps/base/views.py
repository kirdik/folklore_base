from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import DigitalMedia, Expeditions, SeansOfRecord

class ExpeditionsList(ListView):
    model = Expeditions
    template_name = 'expeditions.html'
class ExpeditionDetail(DetailView):
    model = Expeditions
    template_name = 'seances.html'

class DigitalMediaListView(ListView):
    model = DigitalMedia
    template_name = 'digitalmedia.html'
class DigitalMediaDetailView(DetailView):
    model = DigitalMedia
    template_name = 'digitalmediadetail.html'
