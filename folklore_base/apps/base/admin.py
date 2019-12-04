from django.contrib import admin
from folklore_base.apps.base.models import *
admin.site.site_header = 'Банк данных фольклорных записей'


MyModels = [Researcher,Organisation,Expeditions, StorageLocation, MediaType, InventoryNumber]
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

class TimestampInline(admin.TabularInline):
    model = TimingDigitalMedia

@admin.register(DigitalMedia)
class DigitalMediaAdmin(admin.ModelAdmin):
    inlines = [TimestampInline]

class HddMediaDriveAdmin(admin.ModelAdmin):
    list_display = ('hdd_drive', 'hdd_drive_capacity', 'inventory_number_hdd')

admin.site.register(HddMediaDrive, HddMediaDriveAdmin)

