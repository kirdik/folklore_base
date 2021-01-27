from django.urls import path
from .views import DigitalMediaListView, DigitalMediaDetailView, ExpeditionsList, ExpeditionDetail

urlpatterns = [
path('', ExpeditionsList.as_view(), name = 'expeditions' ),
path('seances/<int:pk>', ExpeditionDetail.as_view(), name = 'seances'),
path('dm/<int:pk>/', DigitalMediaDetailView.as_view(), name = 'post_detail'),
path('digital/', DigitalMediaListView.as_view(), name = 'home'),
]
