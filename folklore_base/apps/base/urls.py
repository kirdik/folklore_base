from django.urls import path
from .views import *

urlpatterns = [
    path('', map, name='map'),
    path('expeditions', expeditions, name='expeditions'),
    path('seances/<int:pk>', ExpeditionDetail.as_view(), name='seances'),
    path('dm/<int:pk>/', DigitalMediaDetailView.as_view(), name='dm_detail'),
    path('digital/', digitalmedialist, name='digital'),
    path('digital/<int:id>', digitalmedialist, name='digital'),
    path('informants/', informants, name='informants'),
    path('informants/<int:id>/', informant_details, name='informant_details'),
    path('locations/', locations, name='locations'),
    path('locations/<int:id>/', locations, name='locate_select'),
    path('video/<int:id>', video, name='video'),
    path('reestr/<int:id>', reestr, name='reestr'),
    path('seanceofgeo/<int:id>', seances_of_geo, name='seanceofgeo'),
    path('upload/', photo_upload, name='photo_upload'),
    path('photo/<int:id>', photo, name='photo'),

]
