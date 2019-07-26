# Generated by Django 2.2.3 on 2019-07-26 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naspunk',
            name='naspunkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Rajon', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='oblast',
            name='oblast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Countries', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='rajon',
            name='rajon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Oblast', verbose_name='Область'),
        ),
        migrations.CreateModel(
            name='Informant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(help_text='Фамилия Имя Отчество', max_length=50, verbose_name='ФИО')),
                ('maiden_name', models.CharField(max_length=30, null=True, verbose_name='Девичья фамилия')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Дата рождения')),
                ('date_move', models.IntegerField(null=True, verbose_name='Год переезда')),
                ('place_of_birth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.Naspunk', verbose_name='Место рождения')),
                ('place_of_residence', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Naspunk', verbose_name='Место проживания')),
            ],
        ),
    ]
