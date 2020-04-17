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
	from bboard.views import index
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
		b1	>> <Bb: Bb object (None)> # походу None т.к. !∃ pk(пока что)
		#сохранение записи на диск
		b1.save()
		#проверим, получив val pk
		b1					>> <Bb: Bb object (1)>
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
Bb.objects.create(title='Дом', content='Трехэтажный, кирпич', price=50000000)	>> <Bb: Bb object (3)> #т.е. obj создан(т.к. обзавелся pk(3))
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
manage.py createsuperuser
пакет_конфигурации/settings.py
	...
	LANGUAGE_CODE = 'ru-ru'
	TIME_ZONE = 'Europe/Moscow'
	...
открываем админку -> вводим пароль 
	в списке приложений только Пользователи и Группы(django.contrib.auth)
ЗАРЕГИСТРИРУЕМ ПРИЛОЖЕНИЕ В АДМИНКЕ
bboard/admin.py
#модуль административных настроек
	from django.contrib import admin
	
	from .models import Bb
	#вызываем .register() у экземпляра AdminSite представляющего саму админку
	admin.site.register(Bb)
сохраним, обновим страниу -> готово
∀ название модели - ссылка на страницу списка ее записей
кнопка [добавить <model_name>] -> страница добавления новой записи 
щелкнуть на строку записи для ее редактирования
	там же ее можно удалить
записи можно выбирать и выполнять над их группами поддерживаемые действия
раскрывающийся список ∀ поддерживаемых моделью(заданных для нее классом-редактором) действий находится над списком записей модели
	при выборе моделей и действия и нажатии кнопки выполнения dj выведет подробности выполняемой операции и запросит подтверждение&
++++++++++++++++++++++++++++++++++++++++++++++(остановился здесь)
ПАРАМЕТРЫ ПОЛЕЙ И МОДЕЛЕЙ::СТР::50
#название модели и ее полей - Bbs, title, content, published - что может быть неудобно для пользователя
#+ отсортируем объявления по убыванию даты(свежие вверху)
eng::verbose::подробный
#в вызове ∀ конструктора указываем verbose_name
#verbose_name - человеко-читаемое название поля для вывода
bboard/models.py
	class Bb(models.Model):
		title = models.CharField(max_length=50, verbose_name='Товар')
		content = models.TextField(null=True, blank=True, verbose_name='Описание')
		price = models.FloatField(null=True, blank=True, verbose_name='Цена')
		published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
		
		#attr класса Meta зададут параметры самой модели
		class Meta:
			#название модели в мн-ом числе
			verbose_name_plural = 'Объявления'
			#название модели в од-ом числе
			verbose_name = 'Объявление'
			#{xn} полей используемых для сортировки по умолчанию
			ordering = ['-published']
сохраним -> обновим
	в списке приложений модель представляется "Объявления"
	на странице списка записей, запись представляется "Объявление"
	на страницах добавления|правки записи эл-ты управления представляются "Товар" "Описание" "Цена"
теперь можно исправить контроллер, убрав указание сортировки при извлечении списка записей
#т.к. сортировка по умолчанию, заданная в параметрах модели действует не только в админке
bboard/views.py
	...
	def index(request):
		bbs = Bb.objects.all()
		...
РЕДАКТОР МОДЕЛИ
#на странице списка записей ∀ позиции представляются "<class_model_name> object (<key_val>)"
#представление модели в админке по умолчанию
	#можно задать свои параметры представления модели объявив для нее класс редактор
	from django.contrib import admin
	
	from .models import Bb
	#редактор объявляется как подкласс ModelAdmin ⊃ django.contrib.admin
	#ModelAdmin ⊃ атрибуты задающие параметры представления модели
	class BbAdmin(admin.ModelAdmin):
		#{xn} имен полей которые должны выводиться в списке записей
		list_display = ('title', 'content', 'price', 'published')
		#{xn} имен полей для преобразования в гиперссылки на страницу правки записи
		list_display_links = ('title', 'content')
		#{xn} имен полей по которым будет выполняться фильтрация
		search_fields = ('title', 'content', )
	#заменили этот участок для админки
	admin.site.register(Bb, BbAdmin)
перейдем по списку записей и попробуем найти "газ"
СВЯЗИ МЕЖДУ МОДЕЛЯМИ::СТР 53
выходим из админки, останавливаем сервер
#добавим рубрики объявлений(недвижимость, транспорт, бытовая техника, ...)
bboard/models.py
	...
	class Rubric(models.Model):
		#для модели создается индекс для вывода рубрик с сортировкой по названию
		name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
		
		class Meta:
			verbose_name_plural = 'Рубрики'
			verbose_name = 'Рубрика'
			ordering = ['name']
			
добавим в модель Bb поле внешнего ключа связывающее текущую запись модели с записью в Rubric
#связь "один-со-многими"(одна рубрика на n объявлений)
#модель Rubric - первичная(primary), Bb - вторичная
bboard/models.py
	class Bb(models.Model):
		...
		rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
		class Meta:
			...