from django.contrib import admin
from folklore_base.apps.base.models import *
admin.site.site_header = 'Банк данных фольклорных записей'


MyModels = [Researcher,Organisation,Expeditions, InventoryNumber]

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
    model = Naspunkt
@admin.register(Rajon)
class RajonAdmin(admin.ModelAdmin):
    inlines = [NasPunktInline]


class InformantInline(admin.TabularInline):
    model = Informant
    extra = 0

class DigitalMediaInline(admin.TabularInline):
    model = DigitalMedia
    extra = 0
class DigitalMediaAdmin(admin.ModelAdmin):
    list_display = ['id_of_digitl_media', 'seans']
admin.site.register(DigitalMedia, DigitalMediaAdmin)


@admin.register(SeansOfRecord)
class SeansOfRecordAdmin(admin.ModelAdmin):
    inlines = [DigitalMediaInline]
    filter_horizontal = ('informant_of_seanse',)



class HddMediaDriveAdmin(admin.ModelAdmin):
    list_display = ('hdd_drive', 'hdd_drive_capacity', 'inventory_number_hdd')

admin.site.register(HddMediaDrive, HddMediaDriveAdmin)
