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
                               verbose_name='Страна')
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

class Informant(models.Model):
    fio = models.CharField(max_length=50,
                           help_text='Фамилия Имя Отчество',
                           verbose_name='ФИО')
    maiden_name = models.CharField(max_length=30,
                                   verbose_name='Девичья фамилия',
                                   blank=True)
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

