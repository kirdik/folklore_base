from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from folklore_base.apps.base.models import MediaType

import csv
#a1 = '1234567'
#p = FizNositel.objects.create( inventory_number_fzn = InventoryNumber.objects.create(inventory_number = '123456' ),
#                               storaje_location_fzn = StorageLocation.objects.create( number_of_place= 'A3'),
#                               media_type_fzn=)


csvfile = 'test_base.csv'
separator = ';'
number_one = 1 #Номер столбца в таблице CSV файла
number_two = 2 #Второй номер столбца
def readcsv(csvfile, separator, number_one, number_two): # Определяем функцию которая будет читать из файла
    with open(csvfile) as file: # Открываем файл на чтение
        arrfile = csv.reader(file, delimiter = separator, quoting=csv.QUOTE_ALL)  # Читаем файл при помощи либы csv
        arrarr = []  # Инициируем массив
        for i in arrfile:  # В цикле заполняем массив данными из столбца
            arrarr.append([number_one], [number_two])
    return arrarr
list_a = readcsv(csvfile, separator, 1, 2 ) # Запускаем функцию которую написали выше
#uniclist = list(set(list_a)) #Все уникальные элементы списка
#print(uniclist)
print(list_a)
""" Считываем в массив все данные из базы из поля - Производитель"""
p1 = MediaType.objects.all()
#print(p1)
arrarr2 = []
for i in p1:
    arrarr2.append(str(i))
#print(arrarr2)
""" Сравниваем массивы и вычисляем уникальные элементы """

result = list(set(arrarr2) ^ set(uniclist))
print(result)
""" Загружаем уникальные массивы в базу"""






