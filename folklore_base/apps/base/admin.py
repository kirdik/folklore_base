from django.contrib import admin
from django.utils.safestring import mark_safe
from folklore_base.apps.base.models import *

admin.site.site_header = 'Банк данных экспедиционных материалов'

MyModels = [Researcher, Organisation, InventoryNumber, Reestr, Video, Photo, TimingDigitalMedia]

admin.site.register(MyModels)


class InformantAdmin(admin.ModelAdmin):
    fields = ['fio', 'date_of_birth', 'place_of_residence', 'img_informant', 'preview', 'info_informant']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img_informant.url}" height="200">')

    list_display = ('fio', 'date_of_birth', 'place_of_residence')


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


@admin.register(Naspunkt)
class NaspunktAdmin(admin.ModelAdmin):
    list_display = ['naspunkt_name', 'rajon_naspunkt']


@admin.register(Rajon)
class RajonAdmin(admin.ModelAdmin):
    inlines = [NasPunktInline]
    list_display = ['rajon_name', 'oblast_rajon']


class InformantInline(admin.TabularInline):
    model = Informant
    extra = 0


class TimingDigitalMediaInline(admin.TabularInline):
    model = TimingDigitalMedia
    extra = 0


class DigitalMediaInline(admin.TabularInline):
    model = DigitalMedia
    extra = 0


class DigitalMediaAdmin(admin.ModelAdmin):
    list_display = ['id_of_digitl_media', 'seans']
    fields = ['seans', 'id_of_digitl_media', 'fileupl', 'preview', 'file_description']
    readonly_fields = ["preview"]
    inlines = [TimingDigitalMediaInline]

    def preview(self, obj):
        return mark_safe(f'<audio src="{obj.fileupl.url}" controls></audio>')


admin.site.register(DigitalMedia, DigitalMediaAdmin)


@admin.register(SeansOfRecord)
class SeansOfRecordAdmin(admin.ModelAdmin):
    inlines = [DigitalMediaInline]
    filter_horizontal = ('informant_of_seanse',)


@admin.register(Expeditions)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('organisation_expedition', 'begin_data_expedition')
    filter_horizontal = ('seanses_of_expedition','other_org_exp')


class HddMediaDriveAdmin(admin.ModelAdmin):
    list_display = ('hdd_drive', 'hdd_drive_capacity', 'inventory_number_hdd')


admin.site.register(HddMediaDrive, HddMediaDriveAdmin)
