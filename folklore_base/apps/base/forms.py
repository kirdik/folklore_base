from .models import Photo, TimingDigitalMedia
from django.forms import ModelForm, TextInput, FileInput, TimeInput, Select, NumberInput

class PhotoForm(ModelForm):
        class Meta:
            model = Photo
            fields = ('photo_file', 'description_photo', 'seans')
            widgets = {
                'photo_file': FileInput(attrs={
                    'multiple': True,
                    "class": "form-control",
                    "placeholder": "Выбрать файлы"
                }),
                "description_photo": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание'
                }),
                'seans': Select(attrs={
                    'class': 'form-control',
                    'disabled': True
                })
            }

class TimingForm(ModelForm):
    class Meta:
        model = TimingDigitalMedia
        fields = ('time_stamp', 'end_time_stamp', 'number_of_temestamp', 'text_for_time_stamp', 'timestamp_for_dm')
        widgets = {
            'time_stamp': TimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Начало фрагмента'
            }),
            'end_time_stamp': TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Конец фрагмента'
            }),
            'number_of_temestamp': NumberInput(attrs={
                'class': 'form-control'
            }),
            'timestamp_for_dm': Select(attrs={
                'disabled': True,
                'class': 'form-control'
            }),
            'text_for_time_stamp': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            })
        }
