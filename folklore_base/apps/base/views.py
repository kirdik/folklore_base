from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
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

def informants(request):
    inf = Informant.objects.all()
    return render(request, 'informants.html', {'inf': inf})
def informant_details(request, id):
    infdetail = Informant.objects.get(id=id)
    seances = SeansOfRecord.objects.select_related().filter(informant_of_seanse=id)
    return render(request, 'inf_details.html', {'infdetail': infdetail,
                                                'seances': seances})
