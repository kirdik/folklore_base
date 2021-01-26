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


class Naspunkt(models.Model):
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

'''Model Informant'''
class Informant(models.Model):
    fio = models.CharField(max_length=50,
                           help_text='Фамилия Имя Отчество указывать полностью',
                           verbose_name='ФИО')
    date_of_birth = models.IntegerField(verbose_name='Год рождения',
                                     blank=True,
                                     null=True,
                                     help_text='Указывать только год рождения. Точную дату при необходимости добавить в "Дополнительно"')
    place_of_residence = models.ForeignKey(Naspunkt,
                                           on_delete=models.DO_NOTHING,
                                           verbose_name='Место проживания')
    img_informant = models.ImageField(upload_to='informants/',
                                      blank=True,
                                      null=True,
                                      verbose_name='Фотография исполнителя')
    info_informant = models.TextField(verbose_name='Дополнительная информация',
                                      help_text='Здесь можно добавить такие сведения как: '
                                      'девичья фамилия, '
                                      'место рождения, '
                                      'год переезда, '
                                      'точная дата рождения, '
                                      'дата смерти, '
                                      'контактная информация',
                                      blank=True)
    #data_seans_of_record_inf = models.ForeignKey(SeansOfRecord,
    #                                             on_delete=models.DO_NOTHING,
    #                                             blank=True,
    #                                             null=True)
    class Meta:
        verbose_name = 'Информант'
        verbose_name_plural = 'Информанты'

    def __str__(self):
        return str(self.fio) + ' ' + str(self.place_of_residence)


'''End of Informant'''
''' Seans zapisi Model'''
class SeansOfRecord(models.Model):
    data_seans_of_record = models.DateField(verbose_name='Дата сеанса записи')
    place_of_record = models.ForeignKey(Naspunkt,
                                        on_delete=models.DO_NOTHING,
                                        verbose_name='Место записи')
    informant_of_seanse = models.ManyToManyField(Informant)

    class Meta:
        verbose_name = 'Сеанс записи'
        verbose_name_plural = 'Сеансы записи'

    def __str__(self):
        return str(self.data_seans_of_record) + ' ' + str(self.place_of_record)

'''End of Seanse of record'''


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
    seans = models.ForeignKey(SeansOfRecord,
                              on_delete=models.DO_NOTHING)
    place_hdd_drive = models.ForeignKey(HddMediaDrive,
                                        on_delete=models.DO_NOTHING,
                                        default=0,
                                        verbose_name='На каком HDD хранится')
    id_of_digitl_media = models.CharField(unique=True,
                                          default='CRF20201213_34_A',
                                          verbose_name='ID цифровой записи',
                                          max_length=45)
    fileupl = models.FileField(upload_to='audio/',
                               verbose_name='Аудиофайл')
    file_description = models.TextField(max_length=600,
                                        verbose_name='Описание и тайминг',
                                        default='00:00:00 Русского \n00:00:30 Конец')

    class Meta:
        verbose_name='Цифровой медиа файл'
        verbose_name_plural = 'Цифровые медиа файлы'
    def __str__(self):
        return str(self.id_of_digitl_media)


'''End Digital Media'''
