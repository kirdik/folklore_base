from .models import Photo
from django.forms import ModelForm, FileField, TextInput, ClearableFileInput, FileInput

class PhotoForm(ModelForm):
        class Meta:
            model = Photo
            fields = ('photo_file', 'description_photo', 'seans')
            widgets = {
                'photo_file': FileInput(attrs={
                    'multiple': True,
                    "class": "form-control-file",
                    "placeholder": "Выбрать файл"
                }),
                "description_photo": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание'
                })
            }
            # file_field = FileField(widget=FileInput(attrs={'multiple': True,
            #                                                         'class': 'form-control-file',
            #                                                         'placeholder': 'Выбрать файл'
            #                                                         }))