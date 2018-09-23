#Импорт необходимых модулей
import csv,sys,os

#Указываем путь до папки проекта Django в котором находится файл settings.py
project_dir = "/Django/project/MyWebsite"

#Добавляем в переменную sys.path путь до проекта Django
sys.path.append(project_dir)

#Определяем переменную с настройками Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#Импортируем модуль Django
import django

#Загружаем настройки Django
django.setup()

#Импортируем модель Post
from nutridelta.models import aliment

#Считываем CSV-файл
data = csv.reader(open("/Django/project/hhh.csv"),delimiter=';')

for row in data:
	#Пропускаем заголовки
	
		aliment = aliment()
		
		aliment.aliment_name = row[0]
		aliment.retinol = row[1]

aliment.save()