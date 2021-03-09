from django.urls import path
from .views import *

urlpatterns = [
path('expeditions', expeditions, name = 'expeditions' ),
path('seances/<int:pk>', ExpeditionDetail.as_view(), name = 'seances'),
path('dm/<int:pk>/', DigitalMediaDetailView.as_view(), name = 'post_detail'),
path('digital/', digitalmedialist, name = 'digital'),
path('matherials/<int:id>/', matherials, name = 'matherials' ),
path('informants/', informants, name = 'informants'),
path('informants/<int:id>/', informant_details, name = 'informant_details'),
]
