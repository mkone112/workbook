 pip install django
 django-admin startproject <project_name> [<path_to_project_dir>]
 #создание dj-проекта
 #без указания пути - создает папку с именем проекта в текущей папке
 manage.py startapp bboard
 #регистрируем приложение в проекте:ДВА СПОСОБА
	#ВАРИАНТ 0:добавить в INSTALLED_APPS
	 <project_name>/settings.py
		INSTALLED_APPS = [
			...
			'bboard.apps.BboardConfig',
			#путь к классу описывающему конфиг приложения(конфигурационный класс) и объявленному в bboard/apps.py
			#указывается в формате записи путей к модулям в стандарте Python(точечная нотация)
			#путь указывается относительно папки проекта
		]
	#ВАРИАНТ 1:добавить в __init__.py и INSTALLED_APPS
	<project_name>/<app_name>/__init__.py
		default_app_config = 'bboard.apps.BboardConfig'
	<project_name>/settings.py
		...
		INSTALLED_APPS = [
			...
			'bboard',
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
ПАРАМЕТРЫ ПОЛЕЙ И МОДЕЛЕЙ::СТР::50
#название модели и ее полей - Bbs, title, content, published - что может быть неудобно для пользователя
#+ отсортируем объявления по убыванию даты(свежие вверху)
#очевидно что для строковых/текстовых полей(⊃ обязательные к заполнению(null=False)) допустимо принимать '' =>
	#с null=True они смогут также ⊃ null(None?) =>
		#оно сможет ⊃ два варианта val обозначающих отсутствие val которые придется обрабатывать =>
			#не стоит делать их необязательными
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
		#может Meta это способ объединения attr относящихся к классу, а не экземпляру?
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
bboard/admin.py
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
	#BbAdmin - редактор Bb
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
		#null=True : явно помечаем поле rubric как необязательное(т.к. создать новое обязательное поле в модели уже ⊃ записи - нельзя)
		rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
		class Meta:
			...
сгенерируем миграции для внесения Δ в структуру бд
#создание bboard/migrations/0002_auto_<date_time>.py
#новая миграция 
	#создаст таблицу для модели Rubric
	#добавит в таблицу модели Bb поле rubric
	#задаст для полей модели Bb параметры verbose_name
	#задаст для самой модели параметры
		verbose_name_plural
		verbose_name
		ordering
		#указанные в главе1
		#это делается "для галочки" - подобные Δ класса модели никак не отражаются на бд
manage.py makemigrations bboard
#выводит список Δ в созданной миграции
manage.py migrate

зарегистрируем новую модель в админке
bboard/admin.py
	from .models import Rubric
	...
	admin.site.register(Rubric)
перезапуск(видимо т.к. были миграции)->админка->добавим пару рубрик
СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ МОДЕЛИ
#в списке записей модели Rubric ∀ рубрики представлены строками "<model_class_name> object (<val_ключа_записи>)"
можно объявлить для модели Rubric класс редактора и задать в нем перечень полей выводящихся в списке, но это больше подходит для моделей с несколькими значащими полями(в Rubric оно одно)
или можно переопределить .__str__() возвращающий строковое представление класса
bboard/models.py
	...
	class Rubric(models.Model):
		...
		def __str__(self):
			return self.name
		
		class Meta:
			...
зайдем в список рубрик для проверки
зайдем на страницу списка записей модели Bb и исправим ∀ объявление задав рубрику
#на странице правки записи рубрика выбирается с помощью раскрывающегося списка ⊃ строковые представления рубрик
организуем вывод рубрик объявлений в списке записей Bb
#добавим в {xn} имен полей присвоенную attr list_display ⊃ классу BbAdmin, поле rubric
/bboard/admin.py
	...
	class BbAdmin(admin.ModelAdmin):
		list_display = ('title', 'content', 'price', 'published', 'rubric')
	...
обновим страницу списка объялений => появлися столбец "Рубрика"
#строковое представление связанной записи модели
URL-ПАРАМЕТРЫ И ПАРАМЕТРИЗОВАННЫЕ ЗАПРОСЫ
#разбиваем объявления по рубрикам при выводе(а не только при хранении)
#создадим панель навигации ⊃ список рубрик
	#при щелчке на рубрику => вывод только относящиеся к нему объявления
чтобы контроллер фильтрующий объявления из модели по рубрике работал - он должен получить ключ рубрики
#что удобнее сделать через параметр GET-запроса(URL-параметр)
	bboard/rubric/<rubric_key> | /bboard/<rubric_key>
bboard/urls.py
	...
	from .views import index, by_rubric
	
	urlpatterns = [
		#rubric_id - имя параметра контроллера которому будет присвоенно val этого URL-параметра
#маршруты ⊃ URL-параметры - параметризованные
		path('<int:rubric_id>/', by_rubric),
		...
	]
bboard/views.py
	from .models import Rubric
	...
	def by_rubric(request, rubric_id):
		#помещаем в контекст шаблона список объяв отфильтрованных по полю внешнего ключа rubric, список ∀ рубрик и текущую рубрику
		bbs = Bb.objects.filter(rubric=rubric_id)
		rubrics = Rubric.objects.all()
		current_rubric = Rubric.objects.get(pk=rubric_id)
		context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
		return render(request, 'bboard/by_rubric.html', context)
bboard/templates/bboard/by_rubric.html
	<!DOCTYPE html>
	<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<title>{{ current_rubric.name }} - Доска объявлений</title>
		</head>
		<body>
			<h1>Объявления</h1>
			<h2>Рубрика: {{ current_rubric.name }}</h2>
			<div>
				<a href="/bboard/">Главная</a>
				{ % for rubric in rubrics %}
				<a href="/bboard/{{ rubric.pk }}/">{{ rubric.name }}</a>
				{% endfor %}
			</div>
			{% for bb in bbs %}
			<div>
				<h2>{{ bb.title }}</h2>
				<p>{{ bb.content }}</p>
				<p>{{ bb.published|date:"d.m.Y H:i:s" }}</p>
			</div>
			{% endfor %}
		</body>
	</html>
исправим контроллер index() и шаблон bboard/index.html для вывода панели навигации также на главной и чтобы в ∀ объяве выводилось название рубрики в виде гиперссылки
/bboard/views.py
	...
	def index(request):
		bbs = Bb.objects.all()
		rubrics = Rubric.objects.all()
		context = {'bbs': bbs, 'rubrics': rubrics}
		return render(request, 'bboard/index.html', context)
/bboard/templates/bboard/index.html
	<!DOCTYPE html>
	<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<title>Главная - Доска объявлений</title>
		</head>
		<body>
			<h1>Объявления</h1>
			<div>
				<a href="/bboard/">Главная</a>
				{% for rubric in rubrics %}
				<a href="/bboard/{{ rubric.pk }}/">{{ rubric.name }}</a>
				{% endfor %}
			</div>
			{% for bb in bbs %}
			<div>
				<h2>{{ bb.title }}</h2>
				<p>{{ bb.content }}</p>
				#вроде rubric.pk сгенерился автоматом
				<p><a href="/bboard/{{ bb.rubric.pk }}/">{{ bb.rubric.name }}</a></p>
				<p>{{ bb.published|date:"d.m.Y H:i:s" }}</p>
			</div>
			{% endfor %}
		</body>
	</html>
перезапуск сервера-> главная страница -> под заголовком появилась панель навигации с гиперссылками на рубрики ⊃ объява
перейдем по ∀ ссылке => страница отдельной рубрики
ОБРАТНОЕ РАЗРЕШЕНИЕ URLS
#при Δ шаблонных urls в url_patterns придется вносить мн-во правок в шаблоны т.к. urls формируются прямо в шаблоне + в коде формирующем адреса легко допустить ошибки
	решение: обратное разрешение urls
обратное разрешение urls
#инструмент dj
#reverse
#мы указываем маршрут, формирующий нужный url и val URL-параметров (if это параметризованный ulr), а dj генерурует на их основе url
#для реализации обратного разрешения требуется два действия:
	дать нужным маршрутам имана
	#~создать именованные маршруты
	#имя маршрута указывается в path(..., name,...)
		bboard/urls.py
			...
			urlpatterns = [
				path('<int:rubric_id>/', by_rubric, name='by_rubric'),
				path('', index, name='index'),
			]
			...
	использовать для создания url в гиперссылках шаблонов теги шаблонизатора url
		bboard/templates/bboard/index.html
			#заменим
			...
			<a href="/bboard/{{ rubric.pk }}/">
			...
			<a href="/bboard/">
			#на
			#{% url <route_name> <val_url-параметра_для_вставки_результирующий_url>}
			#по идее берем url из urls.py и передаем туда параметр
			<a href="{% url 'by_rubric' rubric.pk %}">
			...
			#маршрут index - не параметризованный => url-параметры не требуются
			<a href="{% url 'index' %}">
			...
внесем ~ правки во ∀ остальные фраменты обоих шаблонов
обновим страницу => переходы по гиперссылкам пашут
ФОРМЫ СВЯЗАННЫЕ С МОДЕЛЯМИ
#создаем страницу добавления в бд новых объяв
#используем HTML-формы
HTML-forms
#их создание без dj - "сложно и кропотливо"
объявим класс _формы связанной с моделью_
ФОРМА СВЯЗАННАЯ С МОДЕЛЬЮ
#способна генерировать теги
	создающие эл-ты управления ⊂ форме
	валидирующие введенные данные
	сохраняющие данные в связанной с формой модели
создадим форму связанную с моделью Bb
bboard/forms.py
	from django.forms import ModelForm
	
	from .models import Bb
	#класс формы связанный с моделью Bb
	class BbForm(ModelForm):
		#класс ⊃ параметры формы(класс связанной модели(attr класса model), и tuple имен полей модели кот. должны ∃ в форме)
		class Meta:
			model = Bb
			fields = ('title', 'content', 'price', 'rubric')
КОНТРОЛЛЕРЫ-КЛАССЫ
#обрабатывать формы связанные с моделью можно и в контроллерах-fx, но в мы используем контроллер-класс
#высокоуровневый контроллер-класс будет exe большую часть работы по выводу и обработке формы
bboard/views.py
	...
	from django.views.generic.edit import CreateView
	
	from .forms import BbForm
	...
	#базовый класс CreateView реализует функциональность по:
		#созданию формы
		#выводу с применением указанного шаблона
		#получению занесенных в форму данных
		#валидации данных
		#сохранению в новой записи модели
		#перенаправление на заданный url в случае успеха
	class BbCreateView(CreateView):
		template_name = 'bboard/create.html'
		form_class = BbForm
		success_url = '/bboard/'
		#переопределим get_context_data для добавления в контекст дополнительных данных(список рубрик)
		def get_context_data(self, **kwargs):
			#получаем контекст шаблона от метода базового класса
			context = super().get_context_data(**kwargs)
			#т.к. на ∀ странице должна выводиться панель навигации ⊃ список рубрик => требуется добавить в контекст шаблона еще и этот список
			context['rubrics'] = Rubric.objects.all()
			return context
bboard/templates/bboard/create.html
	<!DOCTYPE html>
	<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<title>Добавление объявления - Доска объявлений</title>
		</head>
		<body>
			<h1>Добавление объявления</h1>
			<div>
				<a href="{% url 'index' %}">Главная</a>
				{% for rubric in rubrics %}
				<a href="{% url 'by_rubric' rubric.pk %}">
				{{ rubric.name }}</a>
				{% endfor %}
			</div>
			#форма храниться в v form создаваемую базовым классом CreateView
			#т.к. не указан url по которому будут оправлены занесенные в форму данные -> данные будут отправлены по тому же адресу с которого была получена текущая страница(в данном случае тому же контроллеру-классу BbCreateView)
			<form method="post">
				{% csrf_token %}
				#ModelForm.as_p()
				#if это метод - то здесь ошибка(  form.as_p()  )
				{{ form.as_p }}
				<input type="submit" value="Добавить">
			</form>
		</body>
	</html>
добавим маршрут к CreateView
bboard/urls.py
	...
	from .views import BbCreateView
	
	urlpatterns = [
		path('add/', BbCreateView.as_view(), name='add'),
		...
	]
создадим в панели навигации ∀ страниц гиперссылку на страницу добавления объявления
	<a href="{% url 'add' %}">Добавить</a>
запустим сервер => откроем сайт и перейдем по ссылке добавить
в объявлении класса BbCreateView мы снова указали url перенаправления непосредственно(в attr класса success_url) - Bad Practice
#сгенерируем его путем обратного разрешения
views.py
	from django.urls import reverse_lazy
	
	class BbCreateView(CreateView):
		...
		success_url = reverse_lazy('index')
		...
bboard/templates/layout/basic.html
	<!DOCTYPE html>
	<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<title>{% block title %}Главная{% endblock %} - Доска объявлений</title>
		</head>
		<body>
			<header>
				<h1>Объявления</h1>
			</header>
			<nav>
				<a href="{% url 'index' %}">Главная</a>
				<a href="{% url 'add' %}">Добавить</a>
				{% for rubric in rubrics %}
				<a href="{% url 'by_rubric' rubric.pk %}">{{ rubric.name }}</a>
				{% endfor %}
			</nav>
			<section>
			{% block content %}
			{% endblock %}
			</section>
		</body>
	</html>
bboard/templates/bboard/index.html
#перепишем шаблон чтобы он стал производным от базового
	{% extends "layout/basic.html" %}
	#обязан стоять в начале ∀ производного шаблона(что логично)
	{% block content %}
	{% for bb in bbs %}
	<div class="b">
		<h2>{{ bb.title }}</h2>
		<p>{{ bb.content }}</p>
		<p><a href="{% url 'by_rubric' bb.rubric.pk %}">{{ bb.rubric.name }}</a></p>
		<p>{{ bb.published|date:"d.m.Y H:i:s" }}</p>
	</div>
	{% endfor %}
	{% endblock %}
сохраним-> проверим что главная !Δ
~исправим
bboard/templates/bboard/by_rubric.html
	{% extends "layout/basic.html" %}
	
	{% block title %}{{ current_rubric.name }}{% endblock %}
	
	{% block content %}
	<h2>Рубрика: {{ current_rubric.name }}</h2>
	{% for bb in bbs %}
	<div>
		<h2>{{ bb.title }}</h2>
		<p>{{ bb.content }}</p>
		<p>{{ bb.published|date:"d.m.Y H:i:s" }}</p>
	</div>
	{% endfor %}
	{% endblock %}
bboard/templates/bboard/create.html
	{% extends "layout/basic.html" %}
	
	{% block title %}Добавление объявления{% endblock %}
	
	{% block content %}
	<h2>Добавление объявления</h2>
	<form method="post">
		{% csrf_token %}
		{{ form.as_p }}
		<input type="submit" value="Добавить">
	</form>
	{% endblock %}
СТАТИЧЕСКИЕ ФАЙЛЫ
положим фон: bboard/static/bboard/bg.jpg
/bboard/static/bboard/style.css
	header h1 {
		font-size: 40pt;
		text-transform: uppercase;
		text-align: center;
		background: url("bg.jpg") left / auto 100% no-repeat;
	}
	nav {
		font-size: 16pt;
		width: 150px;
		float: left;
	}
	nav a {
		display: block;
		margin: 10px 0px;
	}
	section {
		margin-left: 170px;
	}
layout/basic.html
	#загружаем модуль static поддерживающий static files в шаблонах
	{% load static %}
	...
	<head>
		...
		#формируем url для статики
		<link rel="stylesheet" type="text/css" href="{% static 'bboard/style.css' %}">
	...
попробуем добавить дополнительные объявления не заполняя некоторые поля