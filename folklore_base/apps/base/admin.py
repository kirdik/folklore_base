from django.contrib import admin
from folklore_base.apps.base.models import *

MyModels = [Researcher,Organisation,Expeditions, StorageLocation, MediaType]
admin.site.register(MyModels)

class InformantAdmin(admin.ModelAdmin):
    list_display = ('fio', 'date_of_birth', 'place_of_residence' )

admin.site.register(Informant, InformantAdmin)


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
    list_display = ('inventory_number_fzn', 'storaje_location_fzn', 'media_type_fzn')
    list_filter = ('storaje_location_fzn','inventory_number_fzn')


