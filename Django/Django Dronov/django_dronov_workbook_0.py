django 1.0 появился в 2005
frame-work - готовый каркас
framework - ∀-объемлющая библиотека 
для dj остается только писать код генерирующий страницы на основе данных из базы
dj следует современным стандартам веб-разработки
	архитектура "модель-контроллер-шаблон"
	использование миграций для внесения изменений в бд
	"написанное однажды применяется везде"
dj - полно-fx framefork
#для разработки среднестатического сайта достаточно только его ∃
dj - высокоуровневый framework
	самостоятельно выполняет типовые задачи
		соединение с бд
		обработка данных полученных от пользователя
		сохранение выгруженных пользователем данных
	предоставляет
		полно-fx подсис-му разграничения доступа
		исключительно мощную, удобно настраиваемую админку(в отличие от ∀ других фреймворков)
dj - удобен - содержит:
	легкий и быстрый отладочный сервер
	развитый механизм миграций
	дополнительные lib
		вывод граф миниатюр
		аутентификация через соцсети
		поддержка CAPTCHA
	основан на Python
	...
source готового сайта электронной доски объявлений: ftp://ftp.bhv.ru/9485977540582.zip | bhv.ru/<page_of_this_book>
используемое по
	Win 10 x64
	Django 2.1.3
	#dj 2.1 требует python 3.5+
	Django Simple Captcha 0.5.9
	django-precise-bbcode 1.2.9
	django-bootstrap4 		0.0.6(разработка) 0.0.7(проверка)
	Pillow					5.2.0
	django-cleanup			2.1.0
	easy-thumbnails			2.5
	Python Social Auth		2.1.0
	Django REST framework	3.8.2
	django-cors-headers		2.4.0
	mod-wsgi				4.6.4
	Angular					6.1.7
pip ⊂ в стандартную поставку Python 3.4+ 
pypi(python package index) реестр пакетов
pip требуется запускать с повышенными правами только if он установленн в директорию требующую соотв прав(напр Program Files)
django тянет за собой pytx
pytz
#библиотека 
#выполняет обработку val даты и времени с учетом временных зон
django-admin
#утилита exe административные задачи
	startproject
	#команда создания проекта
РАЗРАБОТКА ПРОЕКТА
	django-admin startproject samplesite
		samplesite
		#папка проекта
		#м.б. переименована
			manage.py
			#программный файл с кодом соответствующей утилиты сгенерированный djngo-admin
			#∀ что она делает - вызывает django-admin, передавая ей ∀ полученные команды и конфиругирует ее для обработки текущего проекта
			samplesite
			#формурует пакет Python ⊃ модули проекта и задают его конфигурация (⊃ основные настройки)(и конфигурацию ∀ приложений⊂проекту)
			#название = названию проекта, при его переименовании придется вносить серьезные правки в коде
			#в доках dj !⊃ внятного названия => будем называть его пакетом конфигурации
				__init__.py
				setting.py
				#модуль с настройками проекта
					#конфиг бд
					#пути ключевых dirs
					#параметры безопасности
					INSTALLED_APPS = [
						'django.contrib.admin',
						#административный сайт
						'django.contrib.auth',
						#реализует работу подсис-мы разграничения доступа						
						'django.contrib.sessions',
						#реализует работу подсис-мы обслуживающей серверные сессии
					...
				urls.py
				#модуль маршрутизации уровня проекта
				wsgi.py
				#модуль связывающий проект с веб-сервером(используется для деплоя)
ОТЛАДОЧНЫЙ ВЕБ-СЕРВЕР DJ
#написан на Python
#сразу готов к работе, не требует сложной настройки
в связке PHP&Yii|Lavavel требуется устанавливать сервер для тестирования отдельно

manage.py
#по ∀ видимости можно использовать и без "префикса" python т.к. .py ассоциирован с интерпритатором
	runserver
	#запускает отладочный(только?) сервер
	#порт по умолчанию TCP 8000
	startapp
	#создание нового пустого приложения
	makemigrations <app>
	#запускает генерацию миграций для ∀ моделей в app не Δ с момента пред генерации миграций
	#миграции сохраняются в пакете <app>/migrations
	sqlmigrate <app> <number_part_of_migration_file_name>
	#выводит sql генерируемого миграцией
		#bboard/0001_initial.py
		make migrations bboard 0001
	shell
	#запускает консоль dj
	createsuperuser
	#создание зарегистрированного пользователя с max правами
	#pass: min 8 char ⊃ цифры, буквы в разных регистрах
	
app в терминологии dj - отдельный фрагмент функциональности сайта более-менее независимый от других
#может реализовывать работу ∀ сайта|раздела| внутренней подсис-мы используемой другими app
#пакет Python ⊃ модули
#пакет приложения(рядом с пакетом конфигурации)
#имя пакета = имя app
создаем сайт выводящий объявления оставленные пользователями
manage.py startapp bboard
	samplesite
		...
		bboard
		#формирует одноименный пакет app
			migrations
			#папка вложенного пакета ⊃ модули сгенерированных dj миграций
				__init__.py
			admin.py
			#модуль административных настроек и классов редакторов
			apps.py
			#модуль с настройками приложения
			models.py
			#модуль с моделями
			tests.py 
			#модуль с тестирующими процедурами
			#автор считает бесполезной и не рассматривает
			views.py
			#модуль с контроллерами
контроллер dj
#view, вьюха, представление(автор считает неудачным)
#контроллер - устоявшийся термин для таких программных модулей
#код запускаемый в ответ на поступление клиентского запроса содержащего url в опред формате
#выполняют ∀ действия по подготовке данных для вывода и обработку данных от пользователя
		контроллер-fx 
		#более универсальны, но трудоемки в разработке
		контроллер-класс
		#позволяют выполнить типовые задачи(вроде вывода списка каких-либо позиций) минимумом кода
dj не предъявляет к организации кода контроллеров никаких спец требований => можно помещать их в ∀ место ⊃ автоматически создаваемый views.py
∀ контроллер-fx в качетве единственного обязательного аргумента принимает экземпляр HttpResponse
django.http.HttpResponse
#при передаче контроллеру по традиции называется request
#при получении контроллером хранит различные сведения о полученном запросе
	запрашиваемый url
	данные полученные от пользователя
	служебная информация от браузера
МАРШРУТЫ И МАРШРУТИЗАТОР
	связываем(объявляем связь) url определенного формата(шаблонного url) с контроллером
	#объявляем маршрут
	#шаблонный url должен ⊃ только относительный путь без
		названия протокола
		адреса хоста
		порта
		набора GET-параметров
		имени якоря(?)
	#шаблонный url обязан:
		завершаться "/"
		не начинаться на "/"
оформим ∀ объявленные маршруты в виде списка маршрутов в строго определенном формате чтобы подсис-ма маршрутизатора могла его использовать
при поступлении ∀ запроса от клиента dj разбирает его на составные части(посредством "посредников")
посредники
#группа программных модулей
#извлекают запрошенный пользователем url, удаляют из него ∀ кроме пути который передается маршрутизатору
маршрутизатор ищет совпадение в списке urls и передает управление соотв. контроллеру
∀ эл-т списка маршрутов должен представляться результатом возвращаемым django.urls.path()
path(template, view)
#в качестве второго параметра может принимать список маршрутов уровня приложения	
	#связывает "admin" со списком маршрутов возвращаемый св-вом urls экземпляра(?а выглядит как класс) AdminSite который хранится в var(?а я думал это модуль) site и представляет текущую административный веб-сайт dj => при переходе по <host>:port/admin/ загружается админка 
	path('admin/',admin.site.urls)
создатели dj настоятельно не рекомендуют использовать для формирования списка маршрутов тупое добавление шаблонов и контроллеров в /<project>/urls.urlpatterns
#т.к. при большом числе маршрутов его будет сложно поддерживать(вообще делать что-либо вручную это очевидно хреново) =>
	вместо этого
		маршрутизатор dj при просмотре списка маршрутов не требует полного совпадения url из клиентского запроса и шаблона, достаточно лишь совпадения с началом реального(?полученный от клиента?существующий - просто полученный адрес!) тогда шаблонизатор удаляет из реального(?) адреса его начальную часть(префикс) совпавшую с шаблоном и запускает указанный в маршруте контроллер
			,но path() позволяет указать вторым параметром другой список маршрутов вместо view => можно указать для ∀ маршрута другой вложенный в него список маршрутов
				тогда маршрутизатор выполнит просмотр маршрутов ⊃ вложенному списку используя для сравнения адрес с уже удаленным префиксом
					=> можно создать иерархию списков маршрутов, 
						в списке маршрутов уровня проекта укажем маршруты указывающие на вложенные списки записанные в отдельных app(списки маршрутов уровня app)
							в списках маршрутов уровня app запишем контроллеры ⊂ логику сайта
вложенный список маршрутов передаваемый path() должен представлять собой результат django.urls.include()							
django.urls
	.include()
	#one arg?
	#принимает строку с путем к модулю ⊃ список маршрутов
	.reverse_lazy("<route_name>"[,<val_of_url_param>]) -> готовый url
	#
		from django.urls import reverse_lazy
		
		class BbCreateView(CreateView):
			...
			success_url = reverse_lazy('index')
			...
attr класса ~ св-ва класса|статические св-ва в other pl
МОДЕЛИ
#класс Python
#однозначное и исчерпывающее определение сущности в бд
#описывает таблицу бд в которой будет храниться набор сущностей
#attr описывают поля таблицы
#Python представление таблицы и ее полей
#позволяет описывать структуры бд на высоком уровне не заботясь о добавлении данных вручную
#отдельный экземпляр модели = отдельная конкретная сущность извлеченная из бд = отдельная запись соответствующей табл
#используя объявленные в модели attr класса можно читать/писать val в полях записи
#предоставляет инструменты для выборки, фильтрации и сортировки сущностей из бд => результат: {xn} экземпляров класса модели
#объявляются на уровне app, вроде должны записываться в models.py
#основная мощь dj
реализуем вывод объявлений из бд
	можно реализовать это вручную написав код 
		создающий в бд таблицу со ∀ необходимыми полями
		считывающий данные из бд
		преобразующий их
		...
#в dj для реализации хранения ∀ сущностей строго определенной структуры достаточно создать модель
#большинство таблиц бд ⊃ ключевое поле(для хранения pk), обычно int и автоинкрементное=> уникальные val в него заносит сама СУБД
	#что не требует явного объявления в dj -> dj самостоятельно создает такое поле
		#if создать запись с pk = 2, затем с pk=3, удалить pk=2 и создать новую запись -> pk новой записи будет 4(возможно на больших наборах данных это работает иначе)
#attr класса pk поддерживается ∀ моделями, ⊃ val pk текущей записи
#attr класса м.б. получены только после сохранения
	from bboard.models import Bb
	b1 = Bb(title='...',content='...', price='...')
	b1.save()
	b1.pk			>> 1
	b1.title		>> ...
#∀ классы моделей ⊃ .objects
#.objects ⊃ диспетчер записей
ДИСПЕТЧЕР ЗАПИСЕЙ
#особая структура позволяющая манипулировать ∀ совокупностью записей ⊂ модели
#представляется экземпляром класса Manager
	<model>.objects.create(<field0>=<val0>, ...)
	#создает новую запись модели, сохраняет ее и возвращает как результат
	<model>.objects.all()
	#возвращает "набор записей" модели(экземпляр QuerySet)(iterable)
	#отдельные записи- экземпляры соответствующего класса модели
	.order_by(<field>)
	#сортирует записи по val поля указанного в параметре и возвращает получившийся в результате набор записей
		.order_by('-published')
		#видимо сортировка по убыванию
	<model>.objects.filter(<field>=<val>)
	#фильтрация записей по заданным критериям
	#возвращяет другой диспетчер записей ⊃ только отфильтрованные записи
	<model>.objects.get(<field>=<val>)
	#возвращает одну запись подходящую под критерий
	#быстрее filter()
	<запись>.delete()
	#удаляет текущую запись и возвращает сведения о кол-ве удаленных записей
	
ПОЛЯ
#default:∀ поле обязательно для заполнения
#кажется запись = экземпляр класса модели
	django.db.models
		CharField(max_length)
		#строковое поле фиксированной длинны
		TextField()
		#неограниченное поле(memo-поле)
			TextField(null=True, blank=True)
			#поле которое можно не заполнять
		FloatField
		#поле для хранения вещественных чисел
		DateTimeField
		#поле для хранения даты&времени
			DateTimeField(auto_now_add=True)
			#при создании записи(экземпляра модели) заполнять его текущими датой и временем
			DateTimeField(db_index=True)
			#создавать для поля индекс(напр для послед сортировки по дате)(т.е. поле походу становится индексом)
МИГРАЦИИ
#Python-модуль созданный dj на основе модели, предназначенный для создания в бд ∀ требуемых моделью структур
	таблиц
	полей
	индексов
	правил
	связей
#упрощает жизнь
#при exe порождает команды sql отправляемые в СУБД
#автор не описывает средства dj применяемые для создания миграций вручную
manage.py makemigrations bboard
#результат
	<app>/migrations/0001_initial.py
		from django.db import migrations, models
		
		class Migrations(migrations.Migration):
			initial = True
			dependencies = []
			
			operations = [
				migrations.CreateModel (
					#название таблицы бд = названию модели
					name = 'Bb',
					fields = [
						#поля которые модель будет использовать для хранения сущностей
						#AutoField - автоинкрементное поле, не было объявлено явно - dj создал сам
						('id', models.AutoField(auto_create=True,
						primary_key=True, serialize=False, verbose_name='ID')),
						('title', models.CharField(max_length=50)),
						('content', models.TextField(blank=True, null=True)),
						('price', models.FloatField(blank=True, null=True)),
						('published', models.DateTimeField(auto_now_add=True, db_index=True)),
					],
				),
			]
просмотрим sql генерируемый миграцией
#сгенерированный для бд по умолчанию(sqlite)
	manage.py sqlmigrate bboard 0001
		BEGIN;
		--
		-- Create model Bb
		--
		CREATE TABLE "bboard_bb" (
			"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
			"title" varchar(50) NOT NULL,
			"content" text NULL,
			"price" real NULL,
			"published" datetime NOT NULL
		);
		CREATE INDEX "bboard_bb_published_58fde1b5" ON "bboard_bb" ("published");
		COMMIT;
			)
КОНСОЛЬ DJ
#создадим пару объявлений (для отладки)
#dj ⊃ свою редакцию python shell - консоль django
#отличия
	в path ⊃ путь к папке проекта в котором запущена консоль
записи модели создаются ~ экземпляру ∀ другого класса - вызовом конструктора, val полей указываются в именованных args
ШАБЛОНЫ
#образец для формирования документа(который затем можно отдать клиенту)
	HTML
	XML
	PDF
	...
ШАБЛОНИЗАТОР
#подсис-ма dj
#загружает шаблон, объединяет его с данными(излеченными из моделей|полученными от клиента|сгенерированными при работе) и возвращает клиенту
#поддерживает мн-во директив/тегов/фильтров(max часто используемые - встроенны в программное ядро шаблонизатора) остальные реализованы в загружаемых модулях расширения
	#предварительная загрузка модуля расширения exe тегом
		load <module_name>
		#
			{% static 'link_to_static_relative_from_static' %}
			#походу генерирует ссылки на static
				{% load static %}
				...
				<head>
					...
					<link rel="stylesheet" type="text/css" href="{% static 'bboard/style.css' %}">
					...

ШАБЛОН
#⊃команды шаблонизатора
	директивы
	#~include c++
	#указывают поместить в заданное место val
		{{ <var> }}
		#извлечь val из var и вставить в это место
	теги
	#управляют генерированием содержимого результирующего документа
		{% for <elt> in <obj> %}
			...
		{% endfor %}
		#~ for in в Python
		#obj ⊃ в состав контекста шаблона(формируется программистом)
	фильтры
	#преобразуют val перед выводом
		#фильтр date преобразует val из obj в формат указанный после ":"
		#<число>.<номер_месяца>.<год из 4х цифр> <часы в 24ч формате>:<минуты>:<секунды>
		{{<obj>|date:"d.m.Y H:i:s" }}

#по умолчанию ищет шаблоны в <app>/templates/
	#можно Δ в настройках
#очевидно что шаблоны веб-страниц должны быть в *.html(т.к. затем отсылаются клиенту(браузеру))
РЕНДЕРИНГ ШАБЛОНОВ
django.template.loader('path_to_template_from_templates_dir')
#загрузка шаблона для последующего рендеринга
#путь указывается относительно <app>/templates
#возвращает экзепрляр Template предоставляющий хранящийся в заданном файле шаблон
	from django.template import loader
	template = loader.get_template('bboard/index.html')
	return HttpResponse(template.render(context, request))
контекст шаблона
#набор данных котоные д.б. доступны внутри шаблона как var и с которыми шаблонизатор объединит этот шаблон
#словарь Python {'var':<value>,...}
РЕНДЕРИНГ
#объединение шаблонизатором шаблона и данных из контекста
	django.shortcuts.render(request)
	#fx-сокращение(shortcuts) 
	#рендеринг шаблона в одном exp
	#args - подготовленный контекст шаблона; 
	#request - экземпляр HttpRequest
	#возвращает строку с HTML готовой страницы
		from django.shortcuts import render
		from .models import Bb
		
		def index(request):
			bbs = Bb.objects.order_by('-published')
			return render(request, 'bboard/index.html', {'bbs': bbs})

HttpRequest
#предоставляет клиентский запрос
СОКРАЩЕНИЯ
	fx-сокращения(shortcuts)
	#⊂ django.shortcuts
	#high-level средства
АДМИНИСТРАТИВНЫЙ САЙТ DJ
#предоставляет доступ ко ∀ моделям объявленным во ∀ app(видимо ⊂ INSTALLED_APPS)
	#на главной странице отображается список приложений зарегистрированных в проекте и объявлящих ∀ модели и их модели
	
#позволяет...
	просматривать
	добавлять
	изменять
	удалять
	фильтровать
	сортировать
	#...записи
#⊃ встроенную подсис-му разграничения доступа django.contrib.auth
django.contrib.auth
#стандартное app(в админке вроде как отображется как пользователи и группы)
#использует спец модели для хранения(по умолчанию - Пользователи и Группы)
	зарегистрированных пользователей
	групп
	прав
	#таблицы для них в бд создаются специальные миграции => для задействования встроенных средств разграничения доступа dj нужно min раз произвести миграцию
		#затем требуется создать superuser
+++++++++++++++++++++++++++++++++++++++++++++++++(остановился здесь)
ПАРАМЕТРЫ ПОЛЕЙ И МОДЕЛЕЙ::СТР::50
РЕДАКТОР МОДЕЛИ
models.Model
	.ForeignKey(<link_to_class>|<string_with_classname>, null=<bool>, on_delete=models.<model>, verbose_name=)
	#представляет поле внешнего ключа, фактических хранящий ключ записи из первичной модели
	#конструктор, первым параметром принимающий класс первичной модели в виде
		if код объявляющий класс первичной модели распологается перед кодом класса вторичной => ссылки на класс
		if вторичная модель объявлена раньше первичной => строки с именем класса
	#on_delete 
		#управляет каскадным удалением записей вторичной модели при удалении связанной записи в первичной
			models.PROTECT
			#запрет каскадного удаления
∀ поля создаваемые в моделях - по умолчанию обязательны к заполнению
	-> добавить новое, обязательное к заполнению поле в модель уже ⊃ записи => нельзя
	#видимо т.к. тогда придется добавлять val этих полей в уже ∃ записи
	#иначе СУБД вернет err
СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ МОДЕЛИ
...
ОБРАТНОЕ РАЗРЕШЕНИЕ URLS
...
ФОРМЫ СВЯЗАННЫЕ С МОДЕЛЯМИ
django.views.generic.edit
	.CreateView
		.template_name
		#путь к шаблону используемому для вывода страницы с формой
		.form_class
		#класс формы связанной с моделью
		.success_url
		#url по кот. будет выполнен переход после успешного сохранения данных
		.get_context_data()
		#формурует контекст шаблона
django.forms
	.ModelForm.as_p()
	#вывод формы с эл-тами управления на отдельных абзацах
	#генерирует только код создающий эл-ты управления => теги
		<form>
		<input>
		#придется писать вручную
<form>
#создание формы
<input>
#кнопка отправки данных
{% csrf_token %}
#тег шаблонизатора
#создает в форме скрытое поле, хранящее токен, получение которого контроллером - гарантия того что данные получены с текущего сайта и им "можно доверять"
#часть подсис-мы безопасности dj

"цифровой жетон"= токен
КОНТРОЛЛЕРЫ-КЛАССЫ
#в path() ⊂ urls.urlpatterns в случае контроллера-класса передается ссылка на результат возвращаемый .as_view() ⊃ контроллеру класса вместо самого контроллера-класса
НАСЛЕДОВАНИЕ ШАБЛОНОВ
#для сокращения кода шаблонов
#упрощение сопровождения
#механизм dj
#~наследованию классов
#базовый шаблон объявляет в себе блоки
	#блоки определяют место в шаблоне для вставки содержимого из производных(по отношению к базовому) шаблонов
	#∀ блок ⊃ уникальное в пределах шаблона имя

{% block <block_name> %}
#начало объявляемого блока
#может быть пустым|⊃ содержимое - которое
	#будет использовано if производный шаблон не задаст для него содержимое
	#будет заменено if производный шаблон задаст для него содержимое
{% endblock %}
#закрывающий тег блока
СТАТИЧЕСКИЕ ФАЙЛЫ
#файлы не обрабатываемые программно, а пересылаются клиенту как есть
#расположение по умолчанию	
	<app>/static
	#меняется в настройка проекта
ЧАСТЬ II
БАЗОВЫЕ ИНСТРУМЕНТЫ DJ
	СОЗДАНИЕ И НАСТРОЙКА ПРОЕКТА
	#создаем проект, указываем настройки, формируем ∀ необходимые apps
		установка python
		#
		установка dj
		#различные способы установки:docs.djangoproject.com/en/2.1/topics/install
		установка СУБД соотв бд
			SQLite
			#поставляется с интерпритатором python
			#создается автоматом ПРИ ПЕРВОЙ ПОПЫТКЕ ОБРАЩЕНИЯ К НЕЙ
				#для dj - при первом запуске отладочног сервера
			MySQL
			#требуется установка клиента
			#требуется настроенный сервер СУБД
			#dj(2.1+?) поддерживает MySQL 5.6+
			#distrs: dev.mysql.com/downloads/
				#⊃ собственный коннектор
					Connector/Python
					#не требует клиента MySQL|доп python libs
					#не рекомендован dj devs				
			#требуется коннектор(python lib)
				mysqlclient 
				#1.3.7+
			#бд не создается автоматом
			
			