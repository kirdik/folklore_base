from django.db import models

# Create your models here.
'''Location - модель адреса экспедиционной записи'''


class Countries(models.Model):
    countrie_name = models.CharField(max_length=30,
                                     help_text='Страна',
                                     verbose_name='Страна')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = '01 Страны'

    def __str__(self):
        return self.countrie_name


class Oblast(models.Model):
    oblast = models.ForeignKey(Countries,
                               on_delete=models.DO_NOTHING,
                               verbose_name='Страна',
                               default='Российская Федерация')
    oblast_name = models.CharField(max_length=30,
                                   help_text='Область',
                                   verbose_name='Область')

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = '02 Области'

    def __str__(self):
        return self.oblast_name


class Rajon(models.Model):
    rajon = models.ForeignKey(Oblast,
                              on_delete=models.DO_NOTHING,
                              verbose_name='Область')

    rajon_name = models.CharField(max_length=30,
                                  help_text='Район',
                                  verbose_name='Район')

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = '03 Районы'

    def __str__(self):
        return self.rajon_name


class Naspunk(models.Model):
    naspunkt = models.ForeignKey(Rajon, on_delete=models.DO_NOTHING,
                                 verbose_name='Район')

    naspunkt_name = models.CharField(max_length=30,
                                     help_text='Населённый пункт',
                                     verbose_name='Населённый пункт')

    class Meta:
        verbose_name = 'Населённый пункт'
        verbose_name_plural = '04 Населенные пункты'

    def __str__(self):
        return self.naspunkt_name


'''End of Location'''

'''Model Informants'''


class Informant(models.Model):
    fio = models.CharField(max_length=50,
                           help_text='Фамилия Имя Отчество',
                           verbose_name='ФИО')
    maiden_name = models.CharField(max_length=30,
                                   verbose_name='Девичья фамилия',
                                   blank=True,
                                   default='')
    date_of_birth = models.DateField(verbose_name='Дата рождения',
                                     blank=True)
    place_of_residence = models.ForeignKey(Naspunk,
                                           on_delete=models.DO_NOTHING,
                                           verbose_name='Место проживания')
    place_of_birth = models.ForeignKey(Naspunk,
                                       verbose_name='Место рождения',
                                       null=True, related_name='+',
                                       on_delete=models.DO_NOTHING)
    date_move = models.IntegerField(verbose_name='Год переезда',
                                    blank=True,
                                    null=True)
    img_informant = models.ImageField(upload_to='informants/',
                                      blank=True,
                                      null=True)

    class Meta:
        verbose_name = 'Информант'
        verbose_name_plural = 'Информанты'

    def __str__(self):
        return str(self.fio) + ' ' + str(self.place_of_residence)


'''End of Informants'''

'''Model Researchers'''


class Researcher(models.Model):
    fio_researcher = models.CharField(max_length=50,
                                      help_text='Фамилия Имя Отчество',
                                      verbose_name='ФИО')
    email_researcher = models.EmailField(blank=True,
                                         verbose_name='Email')
    about_researcher = models.TextField(blank=True,
                                        verbose_name='Дополнительная информация')

    class Meta:
        verbose_name = 'Исследователь'
        verbose_name_plural = 'Исследователи'

    def __str__(self):
        return self.fio_researcher


'''End Researchers'''

'''Model Organisation'''


class Organisation(models.Model):
    name_organisation = models.CharField(max_length=30,
                                         verbose_name='Аббревиатура')
    full_name_organisation = models.CharField(max_length=120,
                                              verbose_name='Полное наименование')
    email_organisation = models.EmailField(blank=True,
                                           verbose_name='Email')
    about_organisation = models.TextField(blank=True,
                                          verbose_name='Дополнительная информация')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name_organisation


'''End Organisations'''

'''Expeditions Model'''


class Expeditions(models.Model):
    begin_data_expedition = models.DateField(verbose_name='Дата начала экспедиции')

    end_data_expedition = models.DateField(verbose_name='Дата окончания экспедиции',
                                           default='00.00.0000',
                                           null=True,
                                           blank=True)
    organisation_expedition = models.ForeignKey(Organisation,
                                                on_delete=models.DO_NOTHING,
                                                verbose_name='Организация')
    researcher_expedtion = models.ForeignKey(Researcher,
                                             on_delete=models.DO_NOTHING,
                                             verbose_name='Руководитель экспедиции')

    class Meta:
        verbose_name = 'Экспедиция'
        verbose_name_plural = 'Экспедиции'

    def __str__(self):
        return str(self.organisation_expedition) + ' ' + str(self.begin_data_expedition)


'''End Expeditions'''

''' Media type Model'''


class MediaType(models.Model):
    media_type_a = models.CharField(max_length=30,
                                    verbose_name='Тип аналогового носителя',
                                    help_text='аудиокассета, бобина, видеокассета VHS')
    manufacturer = models.CharField(max_length=30,
                                    verbose_name='Производитель',
                                    blank=True)
    additional_note = models.TextField(verbose_name='Дополнительные сведения',
                                       help_text='время звучания, метраж, '
                                                 'для какого типа воспроизводящего'
                                                 ' устройства и прочее',
                                       blank=True)

    class Meta:
        verbose_name = 'Тип аналового носителя'
        verbose_name_plural = 'Типы аналоговых носителей'

    def __str__(self):
        return str(self.media_type_a) + ' ' + str(self.manufacturer)


'''End Media type'''

'''Inventory Number model'''


class InventoryNumber(models.Model):
    inventory_number = models.CharField(max_length=40,
                                        unique=True,
                                        verbose_name='Инвентарный номер')

    class Meta:
        verbose_name = 'Инвентарный номер'
        verbose_name_plural = 'Инвентарные номера'

    def __str__(self):
        return str(self.inventory_number)


'''End Inventory Number'''

'''Storage location model'''


class StorageLocation(models.Model):
    number_of_place = models.CharField(max_length=30,
                                       verbose_name='Номер места хранения',
                                       unique=True)

    class Meta:
        verbose_name_plural = 'Номер места хранения'
        verbose_name = 'Номер места хранения'

    def __str__(self):
        return str(self.number_of_place)


'''End Storage Location'''

'''FizNositel'''


class FizNositel(models.Model):
    inventory_number_fzn = models.OneToOneField(InventoryNumber,
                                                on_delete=models.DO_NOTHING,
                                                verbose_name='Инвентарный номер',
                                                )
    storaje_location_fzn = models.ForeignKey(StorageLocation,
                                             on_delete=models.DO_NOTHING,
                                             verbose_name='Место хранения')
    media_type_fzn = models.ForeignKey(MediaType,
                                       on_delete=models.DO_NOTHING,
                                       verbose_name='Тип носителя',
                                       default=1)
    fzn_txt = models.TextField(blank=True,
                               verbose_name='Описание',
                               help_text='Ветхость, скорость записи (для бобин), и прочие примечания')
    fzn_doc = models.FileField(upload_to='fzn_doc/%Y/%m/%d/',
                               blank=True,
                               null=True,
                               verbose_name='файл с описанием содержимого',
                               )

    class Meta:
        verbose_name = 'Физический носитель'
        verbose_name_plural = 'Физические носители'

    def __str__(self):
        return str(self.inventory_number_fzn) + ' ' + str(self.storaje_location_fzn) + ' ' + str(self.media_type_fzn)


'''End FizNositel'''

'''Gallery of fiz nositel'''


class GalleryFizNositel(models.Model):
    img_fiz_nositel = models.ImageField(upload_to='gallery_fiz_nositel/%Y/%m/%d/',
                                        verbose_name='Фотография обложек и вложенных описей')
    img_fiz_nos_key = models.ForeignKey(FizNositel,
                                        on_delete=models.DO_NOTHING,
                                        blank=True,
                                        null=True,
                                        verbose_name='изображение')

    def img_fzn_a(self):
        if self.img_fiz_nositel:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<img src="{0}" width="100">'.format(self.img_fiz_nositel.url))
        else:
            return '(none)'

    img_fzn_a.short_description = 'Thumb'
    img_fzn_a.alow_tags = True

    class Meta:
        verbose_name = 'Фото носителя'
        verbose_name_plural = 'Фотографии носителей'

    # def __str__(self):
    #    return str(self.img_fiz_nositel)


'''End Gallery Fiznositel'''

'''HDD drives Model'''


class HddMediaDrive(models.Model):
    inventory_number_hdd = models.OneToOneField(InventoryNumber,
                                                on_delete=models.DO_NOTHING,
                                                verbose_name='Инвентарный номер')
    hdd_drive = models.CharField(max_length=30,
                                 verbose_name='Производитель ЖД')
    hdd_drive_capacity = models.CharField(max_length=5,
                                          verbose_name='Объем диска в гигобайтах')
    class Meta:
        verbose_name = 'Жесткий диск (HDD)'
        verbose_name_plural = 'Жесткие диски (HDD)'
    def __str__(self):
        return str(self.hdd_drive) + ' ' + str(self.inventory_number_hdd)


'''End of HDD drives'''

''' Digital media Model'''


class DigitalMedia(models.Model):
    media_file = models.FileField(upload_to='digitalmedia/%Y/%m/',
                                  verbose_name='Загрузить звуковой файл',
                                  default='no')
    place_hdd_drive = models.ForeignKey(HddMediaDrive,
                                        on_delete=models.DO_NOTHING,
                                        default=0,
                                        verbose_name='На каком HDD хранится')
    id_of_digitl_media = models.AutoField(primary_key=True,
                                          #max_length=6,
                                          unique=True,
                                          default='000000',
                                          verbose_name='ID цифровой записи')
    path_of_place = models.CharField(max_length=300,
                                     verbose_name="Путь до папки на жестком диске",
                                     default='/')

    class Meta:
        verbose_name='Цифровой медиа файл'
        verbose_name_plural = 'Цифровые медиа файлы'


'''End Digital Media'''

'''Timing of digital media'''


class TimingDigitalMedia(models.Model):
    time_stamp = models.TimeField(default='00:00:00',
                                  verbose_name='час:минута:секунда')
    number_of_temestamp = models.IntegerField(default='0',
                                              unique=True,
                                              verbose_name='Порядковый номер')
    text_for_time_stamp = models.TextField(verbose_name='Описание временной логической еденицы записи',
                                           blank=True)
    timestamp_for_dm = models.ForeignKey(DigitalMedia,
                                         on_delete=models.CASCADE)

'''End Timing'''
