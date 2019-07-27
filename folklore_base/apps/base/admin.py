from django.contrib import admin
from folklore_base.apps.base.models import *

MyModels = [ Countries, Oblast, Rajon, Naspunk,Informant,Researcher,Organisation,MediaType,Expeditions]
admin.site.register(MyModels)

