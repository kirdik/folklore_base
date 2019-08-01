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
                                    blank=True)

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
        verbose_name = 'Тип носителя'
        verbose_name_plural = 'Типы носителей'

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

    class Meta:
        verbose_name = 'Фото носителя'
        verbose_name_plural = 'Фотографии носителей'

    def __str__(self):
        return str(self.img_fiz_nositel)


'''End Gallery Fiznositel'''


''' Digital media Model'''
class DigitalMedia(models.Model):
    pass


'''End Digital Media'''
