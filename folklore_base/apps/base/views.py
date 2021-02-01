from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


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

def matherials(request, id):
    mat = DigitalMedia.objects.select_related().filter(seans=id)
    return render(request, 'matherials.html', {'mat': mat})
