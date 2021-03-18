from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator

from .models import *

def pagegenerator(namemodel, number, request):

    paginator = Paginator(namemodel, number)
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

    context = { 'model': page,
                'is_paginated': is_paginated,
                'next_url': next_url,
                'prev_url': prev_url

    }
    return context



def expeditions(request):
    explist = Expeditions.objects.all()
    context = pagegenerator(explist, 2, request)
    return render(request, 'expeditions.html', context)

class ExpeditionDetail(DetailView):
    model = Expeditions
    template_name = 'seances.html'
#----DigitalMedia---#
#------это вме можно оптимизировать в одно представление------№
def digitalmedialist(request):
    search_query = request.GET.get('search', '')
    if search_query:
        digital = DigitalMedia.objects.filter(id_of_digitl_media__icontains=search_query)
    else:
        digital = DigitalMedia.objects.all()
    context = pagegenerator(digital, 6, request)
    return render(request, 'digitalmedia.html', context)

class DigitalMediaDetailView(DetailView):
    model = DigitalMedia
    template_name = 'digitalmediadetail.html'

def matherials(request, id):
    mat = DigitalMedia.objects.select_related().filter(seans=id)
    return render(request, 'matherials.html', {'mat': mat})
#----End-Digital--------#

def informants(request):
#------Этот участок поиска надо вывести в отдельную функцию -------#
    search_query = request.GET.get('search', '')
    if search_query:
        inf = Informant.objects.filter(fio__icontains=search_query)
    else:
        inf = Informant.objects.all()

#------------------------------------------------------------------#

    context = pagegenerator(inf, 2, request)
    return render(request, 'informants.html', context)

def informant_details(request, id):
    infdetail = Informant.objects.get(id=id)
    seances = SeansOfRecord.objects.select_related().filter(informant_of_seanse=id)
    return render(request, 'inf_details.html', {'infdetail': infdetail,
                                                'seances': seances})
def map(request):
    map = Naspunkt.objects.all()
    return render(request, 'index.html', {'map': map})
