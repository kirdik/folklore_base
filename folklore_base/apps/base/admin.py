from django.contrib import admin
from folklore_base.apps.base.models import *

MyModels = [ Naspunk,
             Informant,Researcher,Organisation,
             MediaType,Expeditions, InventoryNumber,
             StorageLocation,GalleryFizNositel]
admin.site.register(MyModels)


class OblastInline(admin.TabularInline):
    model = Oblast
@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    inlines = [OblastInline]

class RayonInline(admin.TabularInline):
    model = Rajon
@admin.register(Oblast)
class OblastAdmin(admin.ModelAdmin):
    inlines = [RayonInline]

class NasPunktInline(admin.TabularInline):
    model = Naspunk
@admin.register(Rajon)
class RajonAdmin(admin.ModelAdmin):
    inlines = [NasPunktInline]

class GalleryFiznositelInline(admin.TabularInline):
    model = GalleryFizNositel

@admin.register(FizNositel)
class FiznositelAdmin(admin.ModelAdmin):
    inlines = [GalleryFiznositelInline]


