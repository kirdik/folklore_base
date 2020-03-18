from django.contrib import admin
from folklore_base.apps.ff.models import *

MyModelsFF = [FileUploadFF,]
admin.site.register(MyModelsFF)

# Register your models here.
