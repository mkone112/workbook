 pip install django
 django-admin startproject <project_name>
 manage.py startapp bboard
 #регистрируем приложение в проекте
 <project_name>/settings.py
	...
	INSTALLED_APPS = [
		...
		'bboard.apps.BboardConfig',
		#путь к классу описывающему конфиг приложения и объявленному в bboard/apps.py
		#указывается в формате записи путей к модулям в стандарте Python(точечная нотация)
		#путь указывается относительно папки проекта
	]
создадим контроллер-fx выводящий что сайт в разработке
	views.py
	#удалим содержимое
		from django.http import HttpResponse
		
		def index(request):
		#отправляет текстовое сообщение
			#создаем экземпляр HttpResponse предоставляющий клиенту ответ
			return HttpResponse("Здесь будет список объявлений")
#свяжем маршрут с контроллером
samplesite/urls.py
	...
	urlpatterns = [
		path('bboard/', index),
	...
bboard/urls.py
	from django.urls import path
	
	from .views import index
	
	urlpatterns = [
		#'' - корень пути из маршрута предыдущего(родительского) уровня вложенности
		path('', index),
	]
#исправим urls.py из пакета конфигурации
	...
	from django.urls import path, include
	...
	 urlpatterns = [
		path('bboard/', include('bboard.urls')),
	...
сайт получит запрос с http://localhost:8000/bboard/
	маршрутизатор обнаружит совпадение с bboard/ удалит префикс(совпадающий с шаблоном) и получит "" 
		далее последует загрузка вложенного списка маршрутов где "" совпадет с первым маршрутом => запуститься соотв view
объявим модель объявления Bb
bboard/models.py
	from django.db import models
	
	class Bb(models.Model):
	#модель д.б. наследником django.db.models.Model
		#отдельные поля оформляются attr класса
		#в кач val им присваиваются экземпляры классов полей разных типов(объявленных в том-же django.db.models
		title = models.CharField(max_length=50)
		content = models.TextField(null=True, blank=True)
		price = models.FloatField(null=True, blank=True)
		published = models.DateTimeField(auto_now_add=True, db_index=True)
#сгенерируем миграцию на основе модели которая при применении создаст ∀ необходимые структуры в бд
manage.py makemigrations bboard
выполним миграцию
#первое exe миграций рекомендуется проводить ∀ app
#заметно увеличивает объем бд
рекомендуется удалить исключить ненужные стандартные приложения из INSTALLED_APPS
	manage.py migrate
РАБОТА С МОДЕЛЯМИ
#создадим объявление
	manage.py shell
		from bboard.models import Bb
		#создание записи модели в ram
		b1 = Bb(title='Дача', content='Общество "Двухэтажники". ' + \
		'Два этажа, кирпич, свет, газ, канализация', price=500000)
		#сохранение записи на диск
		b1.save()
		#проверим, получив val pk
		b1.pk				>> 1
#обратимся к полям созданной записи
	b1.title, b1.content, b1.published, b1.id		>> 'Дача',...,datetime.datetime(..., tzinfo=<UTC>)
	b1.id		>> 1
#создадим второе объявление
#не понял почему мы можем так сделать? - потому что эти поля необязательны ?| потому что save() выполняется в конце?
	b2 = Bb()
	b2.title = 'Автомобиль'
	b2.content = '"Жигули"'
	b2.save()
	b2.pk		>>  2
#дополним
	b2.content = '"Жигули", 1980 года, ржавая, некрашенная, сильно битая'
	b2.save()
	b2.content >> '"Жигули", 1980 года, ржавая, некрашенная, сильно битая'
#добавим еще объявление
Bb.objects.create(title='Дом', content='Трехэтажный, кирпич', price=50000000)	>> <Bb: Bb object (3)>
#выведем ∀ объявления
	for b in Bb.objects.all():
		print(b.pk, ': ', b.title)
#извлечем объявления о продаже домов
	for b in Bb.objects.filter(title='Дом'):
		print(b.pk, ': ', b.title)
	>> 3: Дом
#отсортируем записи модели по заголовку(в алфавитном)
for b in Bb.objects.order_by('title'):
	print(b.pk, ': ', b.title)
#объявление о продаже авто имеет pk=2 - отыщем его
b = Bb.objects.get(pk=2)
b.title	>> 'Автомобиль'
b.content	>>
#удалим ржавое корыто
b.delete()	>> (1, {})
exit()
СДЕЛАЕМ ЧТОБЫ контроллер index() ВЫВОДИЛ СПИСОК ОБЪЯВЛЕНИЙ ОТСОРТИРОВАННЫХ ПО УБЫВАНИЮ ДАТЫ ПУБЛИКАЦИИ
bboard/views.py
	from django.http import HttpResponse
	
	from .models import Bb
	
	def index(request):
		s = 'Список объявлений\r\n\r\n\r\n'
		#сортировка по убыванию
		for bb in Bb.objects.order_by('-published'):
			s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
		#походу можно втыкать теги прямо через аргументы! - НЕТ НИХУЯ?
		#HttpResponse представляет собой отсылаемый клиенту ответ
		#параметр content_type в его конструкторе указывает тип данных - utf8 plain text
		#без content_type='text/plain' браузер посчитает текст за HTML и может вывести его в одну строку в нечитаемом виде(проверить)
		return HttpResponse(s, content_type='text/plain; charset=utf-8')
#пишем первый dj шаблон
bboard/templates/bboard/index.html
	<!DOCTYPE html>
	<html>
		<head>
			#Браузеры преобразовывают значение атрибута http-equiv, заданное с помощью content, в формат заголовка ответа HTTP и обрабатывают их, как будто они прибыли непосредственно от сервера.
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<title>Главная - Доска объявлений</title>
		</head>
		<body>	
			<h1>Объявления</h1>
			{% for bb in bbs %}
			<div>
				<h2>{{ bb.title }}</h2>
				<p>{{ bb.content }}</p>
				#фильтр date
				<p>{{ bb.published|date:"d.m.Y H:i:s" }}</p>
			</div>
			{% endfor %}
		</body>
	</html>
#рендеринг шаблонов низкоуровневые интрументы
bboard/views.py
	from django.http import HttpResponse
	from django.template import loader
	
	from .models import Bb
	
	def index(request):
		#загружаем шаблон
		#путь указывается относительно <app>/templates
		#возвращает экзепрляр Template предоставляющий хранящийся в заданном файле шаблон
		template = loader.get_template('bboard/index.html')
		#формируем контекст [для] шаблона
		#набор данных котоные д.б. доступны внутри шаблона как var и с которыми шаблонизатор объединит этот шаблон
		#словарь Python {'var':<value>,...}
		bbs = Bb.objects.order_by('-published')
		#⊃ только bbs ⊃ список объявлений
		context = {'bbs': bbs}
		#рендеринг шаблона
		#
		return HttpResponse(template.render(context, request))
		
#рендеринг шаблонов сокращения
bboard/views.py
	from django.shortcuts import render
	
	from .models import Bb
	
	def index(request):
		bbs = Bb.objects.order_by('-published')
		return render(request, 'bboard/index.html', {'bbs': bbs})
выбираем вариант, сохраняем -> запускаем сервер -> переходим по localhost:8000/bboard/
#видим объявления