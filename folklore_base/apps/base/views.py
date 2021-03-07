from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator

from .models import *


def expeditions(request):
    explist = Expeditions.objects.all()
    paginator = Paginator(explist, 1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = { 'explist': page,
                'is_paginated': is_paginated,
                'next_url': next_url,
                'prev_url': prev_url

    }

    return render(request, 'expeditions.html', context)

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
