from django.contrib import admin
from folklore_base.apps.base.models import *

MyModels = [ Countries, Oblast, Rajon, Naspunk,
             Informant,Researcher,Organisation,
             MediaType,Expeditions, InventoryNumber,
             StorageLocation, FizNositel]
admin.site.register(MyModels)

#class InventoryNumberInline(admin.TabularInline):
#    model = InventoryNumber

#@admin.register(InventoryNumber)
#class InventoryNumberAdmin(admin.ModelAdmin):
#    inlines = [InventoryNumberInline,]


