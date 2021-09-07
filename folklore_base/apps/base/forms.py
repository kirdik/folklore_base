from .models import Photo
from django.forms import ModelForm, FileInput, TextInput

class PhotoForm(ModelForm):
        class Meta:
            model = Photo
            fields = ('photo_file', 'description_photo', 'seans')
            widgets = {
                'photo_file': FileInput(attrs={
                    "class": "form-control-file",
                    "placeholder": "Выбрать файл"
                }),
                "description_photo": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание'
                })
            }