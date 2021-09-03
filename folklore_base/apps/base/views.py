from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator
from .forms import PhotoForm

from .models import *


# ---------- Генерация постраничного вывода в представлении -------------#
# В шаблоне в цикл for передавать model.object_list
# В представлении передавать в конце не список {'var': var }, а переменную var

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

    context = {'model': page,
               'is_paginated': is_paginated,
               'next_url': next_url,
               'prev_url': prev_url

               }
    return context


# ---------------------------------------------#

# --------------- функция поиска -------------#
# Вставлять в представление передавать параметры
# search_query = request.GET.get('search', '')
# filter = Informant.objects.filter(fio__icontains=search_query)

def searchfunc(request, namemodel, filter, search_query):
    if search_query:
        queryset = filter
    else:
        queryset = namemodel.objects.all()
    return queryset


# --------------------------------------------#


def expeditions(request):
    explist = Expeditions.objects.all()
    context = pagegenerator(explist, 2, request)
    return render(request, 'expeditions.html', context)

def seances_of_geo(request, id):
    seances_list = SeansOfRecord.objects.filter(place_of_record_id=id)
    return render(request, 'seanceofgeo.html', {'seances_list': seances_list})


class ExpeditionDetail(DetailView):
    model = Expeditions
    template_name = 'seances.html'


def digitalmedialist(request, id=0):
    search_query = request.GET.get('search', '')
    if search_query:
        digital = DigitalMedia.objects.filter(id_of_digitl_media__icontains=search_query)
    elif id:
        digital = DigitalMedia.objects.select_related().filter(seans=id)
    else:
        digital = DigitalMedia.objects.all()
    context = pagegenerator(digital, 6, request)
    return render(request, 'digitalmedia.html', context)


class DigitalMediaDetailView(DetailView):
    model = DigitalMedia
    template_name = 'digitalmediadetail.html'


def informants(request):
    search_query = request.GET.get('search', '')
    filter = Informant.objects.filter(fio__icontains=search_query)
    inf = searchfunc(request, Informant, filter, search_query)

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


def locations(request, id=0):
    if id:
        locate = Oblast.objects.select_related().filter(id=id)
    else:
        locate = Oblast.objects.all()
    loc = pagegenerator(locate, 2, request)
    return render(request, 'locations.html', loc)

def video(request, id):
    video_req = Video.objects.select_related().filter(seans=id)
    return render(request, 'video.html', {'video_req': video_req})

def reestr(request, id):
    reestr_req = Reestr.objects.select_related().filter(seans=id)
    return render(request, 'reestr.html', {'reestr_req': reestr_req})

# def photo_upload(request):
#     error = ''
#     if request.method == 'POST':
#         form = PhotoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('photo')
#         else:
#             error = 'Неправильно заполнены поля'
#     form = PhotoForm()
#     data = {
#         form: 'form',
#         error: 'error'
#     }
def photo(request, id):
    photo = Photo.objects.select_related().filter(seans=id)
    return render(request, 'photo.html', { 'photo': photo})


