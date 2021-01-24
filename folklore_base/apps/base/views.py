from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import DigitalMedia

class DigitalMediaListView(ListView):
    model = DigitalMedia
    template_name = 'digitalmedia.html'
class DigitalMediaDetailView(DetailView):
    model = DigitalMedia
    template_name = 'digitalmediadetail.html'
