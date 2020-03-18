from django.db import models

class FileUploadFF(models.Model):
    file_ff_upload = models.FileField(upload_to='files_ff',
                                      help_text="Файл ogg, mp3",
                                      verbose_name='Файл')
    name_of_file_ff = models.CharField(max_length=30,
                                       verbose_name='код')
    def __str__(self):
        return self.name_of_file_ff


# Create your models here.
