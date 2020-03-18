from django.urls import path
from .views import *
urlpatterns = [
    path('', audio_list)
]