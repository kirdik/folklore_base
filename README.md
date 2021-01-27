[Python]:https://www.python.org
[ссылке]:https://github.com/kirdik/folklore_base/tree/addfile
# Банк данных фольклорно-этнографических материалов
Задачи банка: описание хранимых исходников и их оцифрованных копий, <br>
хранение внутри банка сжатых копий оцифрованных аудио для их полного описания и последующей работы с ними. <br>
Первый релиз не будет поддерживать учет старых физических носителей и оцифрованных копий. <br>
Пока разработка идет для возможности работать с аудио и видео файлами полученными в ходе экспедиции.<br>
Так же будет возможность загружать сканы реестров.<br>
Банк разрабатывается в рамках моей работы в [Центре русского фольклора ГРДНТ им. В.Д. Поленова](http://folkcentr.ru)<br>
Если вы хотите присоединиться к разработке, пишите на chebotarev@folkcentr.ru

### Установка:
Для работы требуется установленный на компьютере интерпретатор [Python]<br>
Далее необходимо перейти в ветку **addfile** проекта.<br>
Если не знаете как, то просто пройдите по этой [ссылке]<br>
После этого в правом вверхнем углу нажмите зеленую кнопу "Code" и в выпадающем меню нажмите "Download ZIP". <br>
Далее вам необходимо распаковать скачанный файл, затем открыть консоль или терминал, это зависит от вашей операционной системы, перейти в скачанную папку (folklore_base) и выполнить несколько команд:<br>

```
pip install -r requrements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```

