from django.shortcuts import render
from .models import FileUploadFF
def audio_list(request):
    audio = FileUploadFF.objects.all()
    return render(request, 'ff/index.html', context={'audio':audio})
# Create your views here.
