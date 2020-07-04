django 1.0 появился в 2005
frame-work - готовый каркас
framework - ∀-объемлющая библиотека 
для dj остается только писать код генерирующий страницы на основе данных из базы
проект написанный на Python(весьма сомнительно что дело в этом) загружает ∀ модули в ram при запуске => при Δ кода требуется перезапуск
#судя по сообщениям консоли этим занимается StatReloader
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
можно подвесить dj добавив ∀ сложное exp вроде a**b
#что довольно очевидно
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
	#видимо что-то с заголовками для организации межсайтового взаимодействия
	mod-wsgi				4.6.4
	Angular					6.1.7
	
	
Trac
#баг-трекер, вики, управление проектами
#совместим с wsgi

Bottle
#совместим с wsgi

CherryPy
#совместим с wsgi

Flask
#совместим с wsgi

Pylons
#совместим с wsgi

Pyramid
#совместим с wsgi

Rack
#Ruby ~ wsgi

JSGI
#JS ~ wsgi


PSGI
#Perl ~ wsgi


wsgi
#web server gateway interface
#вроде чисто python термин
#стандарт взаимодействия серверной Python-программы и самим веб-сервером(вроде Apache)
	#определяет middleware-компоненты предоставляющие интерфейсы app & серверу ->
		для сервера middleware является app
		для app middleware явл сервером
		->
			позволяет составлять цепи WSGI-совместимых middleware
		#простая обертка над obj приложения
		#мб реализован замыканием
#python ⊃ мно-во библиотек, тулкитов, ... неумеющих взаимодействовать друг с другом
#wsgi предоставляет простой, универсальный интерфейс между большинством веб-серверов и веб-app|фреймвоками
#спеки(должно удовлетворять)
	#callable obj
	#принимать environ, start_response(что-то такое я делал)
		environ
		#словарь v окружения
		start_response
		#запрос при старте|~?
		#обработчик запроса
	#вызывать обработчик с кодом HTTP-ответа и HTTP-заголовками
	#возвращать iterable ⊃ тело ответа
#простейший пример
	def simplest_wsgi_app(environ, start_response):
		start_response('200 OK', [('Content-Type', 'text/plain')])
		yield 'Hello, world!'

pip ⊂ в стандартную поставку Python 3.4+ 
	pip show <packet>
	#просмотр данных пакета ⊃ зависимости
pypi(python package index) реестр пакетов
pip требуется запускать с повышенными правами только if он установленн в директорию требующую соотв прав(напр Program Files)
django тянет за собой pytz и sqlparse

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
		#м.б. переименована/перемещена
			manage.py
			#программный файл с кодом соответствующей утилиты сгенерированный djngo-admin
			#∀ что она делает - вызывает django-admin, передавая ей ∀ полученные команды и конфиругирует ее для обработки текущего проекта
			#служебная утилита
			samplesite
			#формурует пакет Python ⊃ модули проекта и задают его конфигурация (⊃ основные настройки)(и конфигурацию ∀ приложений⊂проекту)
			#название = названию проекта, при его переименовании придется вносить серьезные правки в коде
			#в доках dj !⊃ внятного названия => будем называть его пакетом конфигурации
				__init__.py
				
				
				setting.py
				#модуль с настройками проекта
				#конфиг бд
				#имя v = имя параметра
				#val форматов даты и времени - на мой взгляд полная наркомания
					<название месяца на английском>: 'F'|'E'
					<число>						   : 'd'|'j'
					...
				#при записи форматов дат/времени используются те же спецсимволы что и в фильтре шаблонизатора date
				#при записи форматов даты/времени для полей ввода используются спецсимволы используемые в вызовами strftime() и strptime()
					#их перечень:docs.python.org/3/library/datetime.html#strftime-strptime-behavior
				#пути ключевых dirs
				#параметры безопасности
				
					BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) |os.path.join(BASE_DIR, ...)
					#путь к проекту(по умолчанию вычисляется автоматом)
					
					SECRET_KEY = <str>
					#используется ядром dj и подсис-мой разграничения доступа для шифрования данных
					#генерируется django-admin при создании проекта
					#может использоваться для атаки на сайт
					#не следует менять без необходимости
					
					DEBUG=<Bool>
					#режим работы сайта
						True(включается при создании проекта)
						#отладочный
						#вывод страницы отладки при ∀ err
						False(по умолчанию)
						#эксплутационный
						#при ∀ err выводит стандартное сообщение сервера(not found(404)/internal server error(500))
						#более строгие настройки безопасности
						
					ALLOWED_HOSTS = []
					#
					
					
					INSTALLED_APPS = [
					#заполняется при создании проекта
					#при удалении приложения из списка => следует удалить ∀ используемые им посредники
						'django.contrib.admin',
						#реализует fx административного сайта
						'django.contrib.auth',
						#реализует работу подсис-мы разграничения доступа						
						#используется django.contrib.admin
						'django.contrib.contenttypes',
						#⊃ список ∀ моделей объявленных во ∀ app проекта
						#используется
							при создании полиморфных связей между моделями(дронов глава 16)
							django.contrib.admin
							django.contrib.auth						
						'django.contrib.sessions',
						#реализует работу подсис-мы обслуживающей серверные сессии
						#обеспечивает хранение данных клиента на сервере в сессиях
						#используется django.contrib.admin
						'django.contrib.messages',
						#вывод/обработка всплывающих msg
						#используется django.contrib.admin
						'django.contrib.staticfiles',
						#реализация обработки static
						#не требуется if проект !⊃ static(что как-то маловероятно)
					]
					
					MIDDLEWARE = <list>:[]
					#список посредников
					#middleware:eng:посредник
					#val генерируемое при создании проекта - посредники ⊂ dj
						[
							'django.middleware.security.Security.Middleware',
							#реализация доп защиты сайта от сетевых атак
							#очевидно не стоит отключать
							'django.contrig.sessions.middleware.SessionMiddleware',
							#обеспечение работы сессий на low level
							#используется
								django.contrib.auth
								django.contrib.sessions
								django.contrib.messages
							'django.middleware.common.CommonMiddleware',
							#учавствует в предварительной обработке запросов
							#не стоит отключать
							'django.middleware.csrf.CsrfViewMiddleware',
							#видно что-то с токенами
							#защита от межсайтовых запросов при обработке данных переданных сайту HTTP-медодом POST
							#не стоит отключать if сайт получает данные от пользователей через POST
							'django.contrib.auth.middleware.AuthenticationMiddleware',
							#что-то с авторизацией
							#добавляет в obj запроса(request?) attr ⊃ текущего user, который можно использовать для определения какой user входил на сайт
							#используется
								django.contrib.admin
								django.contrib.auth
							'django.contrib.messages.middleware.MessageMiddleware',
							#обработка всплывающих msg на low level
							#используется
								django.contrib.admin
								django.contrib.messages
							'django.middleware.clickjacking.XFrameOptionsMiddleware',
							#доп защита от сетевых атак
							#очевидно не стоит отключать
						]
						
					ROOT_URLCONF = <project_dir>.<urls.py>
					#путь к модулю хранящем маршруты уровня проекта
					
					TEMPLATES = [
						{
							'BACKEND': 'django.template.backends.django.DjangoTemplates',
							'DIRS': [],
							#доп папки с шаблонами?
							'APP_DIRS': True,
							#видимо использовать ли dir ⊃ apps с шаблонами?
							'OPTIONS': {
								'context_processors': [
									'django.template.context_processors.debug',
									'django.template.context_processors.request',
									'django.contrib.auth.context_processors.auth',
									'django.contrib.messages.context_processors.messages',
									
								],
							},
						},
					]
					
					WSGI_APPLICATION = '<project_dir>.wsgi.application'
					
					DATABASES = <dict>:{}
					#val при создании проекта
						#указывает единственную бд в формате SQLite ⊂ в файле <project>/db.sqlite3
						{
							'default': {
								'ENGINE': 'django.db.backends.sqlite3',
								#формат бд
								#путь к модулю реализующему работу с нужным форматом бд
								#доступные val	
									django.db.backends
										.sqlite3
										.mysql
										.postgresql
										.oracle
								'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
								#путь к файлу бд(sqlite3)|имя бд(серверные субд)
								'TIME_ZONE'
								#TZ для val date/time ⊂ db
								#используется if формат бд не поддерживает val даты/времени ⊃ timezone(а такие ∃?)
								#val по умолч: None(параметр вообще не указан)(val берется из одноименного val проекта)
								'HOST'
								#используется only for серверных СУБД
								#адрес сервера СУБД
								'PORT':''
								#используется only for серверных СУБД
								#порт для подключения к серверу СУБД
								#по умолч - пустая str - использовать порт по умолчанию(порт по умолчанию для ∀ бд?|порт по умолчанию для dj)
								'USER'
								#используется only for серверных СУБД
								#имя пользователся СУБД
								'PASSWORD'
								#используется only for серверных СУБД
								#пароль пользователя СУБД
								'CONN_MAX_AGE':<int>:0
								#используется only for серверных СУБД
								#число секунд в течение которого соединение с бд будет открыто
									0 
									#закрытие сразу после обработки запроса
								'OPTIONS':<dict>:{}
								#используется only for серверных СУБД
								#доп параметры специфичные для СУБД
								#∀ елт - отдельный параметр(что как-то очевидно)
							}
						}
					#хранит ∀ бд используемые проектом
					
					
					AUTH_PASSWORD_VALIDATORS = [
						{
							...
						}
					]
					#перечисление валидаторов паролей
					
					
					LANGUAGE_CODE = 'ru-ru':'en-us'
					#код языка используемого для вывода сис-ых msg и страниц django.contrib.admin
					
					
					TIME_ZONE = <str>:
					#val по умолч:'America/Chicago', при создании проекта:UTC
					
					
UTC
#всемирное координированное время
					#список доступных зон:en.wikipedia.org/wiki/List_of_tz_database_time_zones
					#возм val
						'Europe/Moscow'
						
						
					USE_I18N = <bool>:True
					#состояние ⊂ dj сис-мы автоперевода на язык указанный в LANGUAGE_CODE
						USE_I18N = True
						#∀ сообщения админки выводятся локализованными
						#понижает perf
						USE_I18N = False
						#∀ сообщения выводятся на en-us
						#увеличивает perf
						
						
					USE_L10N = <bool>:True
					#в книге USE_L18N(очевидная ошибка)
					#val по умолч:False, при создании проекта True
						USE_L10N = True
						#числа, даты, время при выводе форматируются по правилам языка указанного в LANGUAGE_CODE
						#переопределяет настройки проекта
						USE_L10N = False
						#числа, даты, время - при выводе форматируются согласно настройкам проекта


					USE_TZ=<bool>
					#False:по умолч, при создании проекта:True
					#хранение tz
						USE_TZ = True
						#dj будет хранить val даты/времени ⊃ tz => TIME_ZONE указывает tz по умолчанию
						USE_TZ = False
						#dj ⊃ дату/время !⊃ tz => TIME_ZONE указывает tz для них
						
						
					STATIC_URL = ''
					#путь до static
					
					
					FILE_CHARSET
					#кодировка текстовых файлов
					#параметр отсутсвует by def
					#кодировка по умолчанию = 'utf-8'
					
					
					DEFAULT_CHARSET='utf-8'
					#кодировка страниц по умолчанию
					#параметр отсутсвует by def
					
					
					DECIMAL_SEPARATOR=<str>:'.'
					#требует USE_L18N = False, иначе игнорируется(очевидно тк параметр переопределяется)
					#символ используемый для разделения целой.дробной части вещественных чисел
					
					
					NUMBER_GROUPING=<int>:0
					#требует USE_L18N = False, иначе игнорируется(очевидно тк параметр переопределяется)
					#число цифр в числе составляющих группу
						NUMBER_GROUPING=0
						#группировка не используется
						
						
					THOUSAND_SEPARATOR=<str>:','
					#требует USE_L18N = False, иначе игнорируется
					#символ разделения групп цифр при выводе
					
					
					USE_THOUSAND_SEPARATOR=<bool>:False
					#требует USE_L18N = False, иначе игнорируется
					#использовать разбиение на группы
					
					
					SHORT_DATE_FORMAT=<str>:'m/d/Y'
					#требует USE_L18N = False, иначе игнорируется
					#формат по умолч для вывода даты в коротком виде
					#val по умолч: 'm/d/Y' : <месяц>/<число>/<год из 4х цифр>
					#дронов рекомендует установить
						SHORT_DATE_FORMAT = 'j.m.Y'
						
						
					SHORT_DATETIME_FORMAT=<str>:'m/d/Y P'
					#требует USE_L18N = False, иначе игнорируется
					#формат по умолч для вывода даты и времени в коротком виде
					#val по умолч: 'm/d/Y P' : <месяц>/<число>/<год_из_4х_цифр> <часы в 12-ти часовом формате>
					#примеры
						'j.m.Y H:i:s'
						#<число>.<месяц>.<год_из_4х_цифр> <часы_в_24х_часовом_формате>:<минуты>:<секунды>
						
						
					DATE_FORMAT=<str>:'N j, Y'
					#требует USE_L18N = False, иначе игнорируется
					#формат по умолч для вывода val даты в полной записи
					#val по умолч:'N d, Y':<eng_назв_месяца> <date> <year_xxxx>
						'E'
						#локализованное назв месяца?
						
						
					DATETIME_FORMAT=<str>:'N j, Y, P'
					#требует USE_L18N = False, иначе игнорируется
					#формат по умолч для вывода val даты и времени
					#дронов рекомендует: 'j E Y H:i:s'
					
					
					TIME_FORMAT=<str>:'P'
					#требует USE_L18N = False, иначе игнорируется
					#default формат вывода времени
					
					
					MONTH_DAY_FORMAT=<str>:'F, j'
					#требует USE_L18N = False, иначе игнорируется
					#default формат вывода месяца и числа
					#default val:'F, j'
					
					
					YEAR_MONTH_FORMAT=<str>:'F Y'
					#требует USE_L18N = False, иначе игнорируется
					#default формат вывода месяца и года
					
					
					DATE_INPUT_FORMATS=<list>:[...]
					#требует USE_L18N = False, иначе игнорируется
					#список форматов в которых пользователи могут заносить val в поля ввода
					#получив val даты в виде str dj {xn} сравнивает его со ∀ форматами в этом списке
					#дронов рекомендует ['%d.%m.%Y']
					
					
					DATETIME_INPUT_FORMATS=<list>:[...]
					#требует USE_L18N = False, иначе игнорируется
					#список форматов в которых пользователи могут заносить val даты и времени в поля ввода
					#дронов рекомендует:['%d.%m.%Y %H:%M:%S']
					
					
					TIME_INPUT_FORMATS=<list>:['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']
					#требует USE_L18N = False, иначе игнорируется
					#список форматов в которых пользователи могут заносить val времени в поля ввода
					
					
					FIRST_DAY_OF_WEEK=<int>:0
					#требует USE_L18N = False, иначе игнорируется
					#номер дня с которого начинается неделя
						0 : вс
						6 : сб
						
						
				urls.py
				#модуль маршрутизации уровня проекта
				
				
				wsgi.py
				#модуль связывающий проект с веб-сервером(используется для деплоя)


ПОСРЕДНИКИ
#middleware
#программные модули exe предварительную обработку клиентского запроса перед передачей контроллеру и окончательную обработку ответа контроллера
#∀ посредники должны быть указаны в соотв списке в settings.py
#см wsgi
#могут исп для
	обработки сессий
	аутентификации
	маршрутизации запросов(управления url)
	балансировки нагрузки
	Δ заголовков
	...

ОТЛАДОЧНЫЙ ВЕБ-СЕРВЕР DJ
#написан на Python
#сразу готов к работе, не требует сложной настройки
#загружает ∀ модули в ram при запуске => повышает быстродейтвие, требует перезапуска при Δ кода
#перезапускается сам при обнаружении Δ в используемых модулях
#при некоторых Δ(создание новых модулей|шаблонов можен не перезапускаться|перезапускаться криво)
#может требовать перезапуск даже в случаях когда ∀ вроде должно работать
в связке PHP&Yii|Lavavel требуется устанавливать сервер для тестирования отдельно
проекты на PHP в отличие от Python не загружают ∀ модули в ram при запуске => требуют перезапуски реже


manage.py
#по ∀ видимости можно использовать и без "префикса" python т.к. .py ассоциирован с интерпритатором
#основные параметры
	[-h|--help]
	#py manage.py <command> -h ~ py manage.py help <command>
	[--version]
	#по ∀ видимости версия ∀ отдельнои утилиты
	[--noinput|--no-input]
	#без вывода
	[-v|--verbosity {0,1,2,3}]
	#output verbosity level
		0: minimal
		1: normal
		2: verbose
		3: very verbose
	[--traceback]
	#raise on CommandError except
	[--no-color] [--force-color]
#команды
	[auth]
	
		changepassword
		#change user pass for django.contrib.auth
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--database <database_to_use>]
			[--version]
			[-v {0,1,2,3}] [--settings <python_path_to_settings_module>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[username] = <current_username>
			


		createsuperuser
		#создание зарегистрированного пользователя с max правами
		#очевидно нуждается в ∃ бд
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--username <username>]
			[--noinput|--no-input]
			#not prompt the user for any kinds
			#требует --username, и val остальных обязательных полеи
			#тк передать pass в параметре нельзя(по очевидным причинам) созданныи superuser не сможет логиниться до получения пароля
			[--database <database_to_use>] = "default"
			#
			[--email <superuser_email>]
			[--version]
			#по ∀ видимости версия утилиты createsuperuser
			[-v|--verbosity {0,1,2,3}]
			[--settings <python_path_to_settings_module>] = DJANGO_SETTINGS_MODULE
			#пример
				--settings "myproject.settings.main"
			[--pythonpath <python_path>]
			#dir to add to the Python path
				--pythonpath "/home/django_projects/myproject"
			[--traceback] [--no-color] [--force-color]
		#pass: min 8 char ⊃ цифры, буквы в разных регистрах
		


	[contenttypes]
		remove_stale_contenttypes
		#?
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--noinput|--no-input] [--database <db_name>] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		
	[django]
		check
		#проверяет ∀ dj проект на потенциальные проблемы
		#запускается автоматом при старте dj? исп подсисмами(напр для вывода err msg на страницах) dj?
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-t|--tag <tags>]
			#run only check labeled with given tag
			[--list-tags]
			#list available tags
			[--deploy]
			#check deployment settings
			[--fail-level {CRITICAL,ERROR,WARNING,INFO,DEBUG}] = ERROR
			#message level that will cause the command to exit with a non-zero status
			[--version] [-v|--verbosity {0,1,2,3}] [--settings <python_path_to_settings_module>]
			[--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[app_label [app_label ...]]
			
		
		
		compilemessages
		#компилит .po фаилы в .mo используя встроенную поддержку gettext
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-l|--locale LOCALE]
			#Locale(s) to process (e.g. de_AT). Default is to process all. Can be used multiple times.
			[-x|--exclude EXCLUDE] = none
			#исключенные локали, мб исп мн-во раз
			[--use-fuzzy] [--version] [-v|--verbosity {0,1,2,3}] [--settings <python_path_to_settings_module>]
			[--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]

		
		
		createcachetable
		#create the tables needed to use the SQL cache backend
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--database <db_name>] = "default"
			#дб для создания таблиц
			[--dry-run]
			#вывод SQL для запуска без его запуска
			[--version] [--settings <python_path_to_settings_module>]
			[--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[table_name [table_name ...]]
			#opt table names. Otherwise, settings.CACHES is used to find cache tables.
			
			
			
		dbshell
		#runs the command-line for specifisd db
			[-h|--help]
			[--database <db_name>] = "default"
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]



		diffsettings
		#отображает Δ settings.py от его default вида
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--all]
			#(?)display all settings, regardless of their val. In "hash" mode
			#default val are prefexed  by "###"
			[--default MODULE]
			#settings module to compare the curr settings against
			#leave empty to compare against dj defaut settings
			[--output {hash, unified}]
			#формат вывода
				'hash'
				#вывод ∀ Δ настроек, with the settings that don't appear in the defaults followed by ###
				'unified'
				#prefixes the default settings with a '-', followed by the changed setting with a '+' 
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]

		
		
		dumpdata
		#output the content of the database as a  fixture(?) of the given format(using ∀ model's default manager unless --all is specified)
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--format <format>]
			#specifies the outpet serialization format for fixtures
			[--indent <indent>]
			#specifies the indent leve to use when pretty-printing output
			[--database <db_name>] = "default"
			#db to dump fixtures from
			[-e|--exclude <app_label|<app_label.ModelName>]
			#можно исп неск раз
			[--natural-foreign]
			#(?)исп natural foreign keys if доступны
			[--natural-primary]
			#(?) исп natural primary keys if доступны
			[-a|--all]
			#use dj base manager to dump all models stored in the database ⊃ those that would otherwise be filtered|modified by a custom manager
			[--pks <primary_key0, primary_key1,...]
			#only dump obj with given primary keys.
			#работает only if указана ОДНА модель
			[-o|--output <file_for_output>]
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должны стоять в конце)
			[app_label0[.ModelName] [app_label1[.ModelName]] ...]
			#restricts dumped data to the specified app_label|app_label.ModelName

fixtures:eng:?			
			

		flush
		#УДАЛЯЕТ ∀ ДАННЫЕ ⊂ ∀ бд, ⊂ добавленные миграциями
		#does not achive a "fresh install" state
			[-h|--help] [--noinput|--no-input] [--database <db_name>] [--version] [-v {0,1,2,3}] [--settings <setting>]
			[--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		

		
		inspectdb
		#(sic!) introspects the db tables & outputs a dj model module
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[database <db_name>] = "default"
			[--include-partitions]
			#также выводить модели для partition tables
			[--include-views]
			#также выводить модели для views
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должны стоять в конце)
			[table [table ...]]
			#tables|views for introspection
			


		loaddata
		#install the name fixture(s) in the db
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--database <db_name>] = "default"
			[--app <app_label>]
			#only look for fixtures in the specified app
			[-i|--ignorenonexistent]
			#ignores entries in the serialized data for fields that do not currently exist on the model
			[-e|--exclude <app_label|<app_label.ModelName>]
			#можно исп неск раз
			[--format <format>]
			#format of serialized data when reading from stdin
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			fixture0 [fixture1 ...]
			#fixture labels



		makemessages
		#runs over the entire source tree of the current directory and pulls out all strings marked for translation
			#it creates|updates a msg file in the conf/locale(in dj tree) | locale (for projects&apps) dir
		#должна быть запущенна с --locale|--exclude|-all
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-l|--locale <locale>]
			#создание|обновление msg files для заданных локалеи
			#локали
				pt_BR
			#мб исп неск раз
			[-x|--exclude <locales_to_exclude>] = none
			#мб исп неск раз
			
			[-d|--domain <domain>] = "django"
			#the domain of the msg files
			[-a|--all]
			#обновить msg фаилы для ∀ ∃ локалеи
			[-e|--extensions <comma_separated_extensions>] = "js" if (domain is "djangojs") else "html,txt,py"
			#расширения фаилов для проверки
			#мб исп неск раз
			[-s|--symlinks]
			#следовать по симлинкам
			[-i|--ignore <glob_style_pattern>]
			#мб исп неск раз
			#ignore files|dirs
			[--no-default-ignore]
			#don't ignore common glob-style patterns 'CSV', '.*', '*~', '*.pyc'
			[--no-wrap]
			#don't break long msg lines into several lines
			[--no-location]
			#don't write '#: filename:line' lines
			#~ --add-location 'never'
			[--add-location [{full, file, never}]] = 'full'
			#control '#: filename:line' lines
				'full'
				#the lines ⊃ file name&line number
				'file'
				#line number is omitted(опущены?)
				'never'
				#the lines are supressed
				#~ --no-location
			#requires gettext 0.19+
			[--no-obsolete]
			#remove obsolete msg strs
			[--keep-pot]
			#keep .pot file after making msgs(for debugging)
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
			
ommited:eng:опущен?
obsolete:eng:?


gettext
#(?) вероятно модуль получения текста
#используется manage.py makemessages
			
obsolete:eng:?
		
		makemigrations
		#запускает генерацию одного файла миграции для ∀ моделей в app не Δ с момента пред генерации миграции
		#миграции сохраняются в пакете <app>/migrations
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--dry-run]
			#вывод сведений о формируемой миграции без ее формирования
			#тупо выводит в консоль тоже что и при миграции
				py manage.py makemigrations --dry-run
					Migrations for '<app>':
						<app>\migrations\<migration_name>
							- Create model <model_name>
							...
			#думаю подходит для тестов моделеи
			[--merge]
			#исп для устранения конфликтов миграций
			[--empty]
			#создание "пустой" миграции для ручного формирования
			[--noinput|--no-input]
			#скрыть вывод сведений о формируемой миграции

			[-n|--name <migration_name>]
			#имя формируемой миграции добавляемое к порядковому номеру
			#if !∃ => default имя:
				initial
				#для начальной миграции(создающей первые версии ∀ необходимых структур)
				auto_<date_time_stamp>
				#созданные после initial Δ созданные ранее структуры
			[--no-header]
			#не добавлять заголовок ⊃ комментариями
			[--check]
			#exit with !0 status if model changes are missing migrations
			#вывод сведений о Δ моделей с последней миграции без формирования миграции
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<apps_labels(aliases)_через_пробел>]
			#if не указан -> обрабатываются модели объявленные во ∀ apps проекта			
			
		migrate
		#выполнение миграции
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--noinput|--no-input]
			#отключить вывод сведений о применеии
			[--database <db_name>]
			[--fake]
			#помечает ∀ миграции как exe без Δ бд
			#исп if ∀ Δ были внесены в бд вручную
			
			[--fake_initial]
			#пропуск exe начальной миграции
			#исп if бд ⊃ ∀ необх структуры для модификации
			[--plan]
			#show a list of the migration action that will be performed
			[--run-syncdb]
			#создает таблицы для apps без миграций
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<app_alias> [<migration_name>|<номер>]]
			#без указания -> exe ∀ не exe миграции ⊂ ∀ apps
			#без указания <migration_name> => ∀ миграции ⊂ <app>
		migrate <app_alias> zero
		#отмена ∀ миграций ⊂ app с удалением ∀ созданных ими структур из бд
			#НЕЛЬЗЯ ОТМЕНИТЬ ОТДЕЛЬНУЮ МИГРАЦИЮ

			
			
		sendtestemail
		#отправка testemail
			[-h|--help]
			[--managers]
			#исп адреса указанные в settings.MANAGERS
			[--admins]
			#исп адреса указанные в settings.ADMINS
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]



		shell
		#запускает консоль dj
		#пытается исп IPython|bpython при наличии
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--no-startup]
			#if using plain python -> ignore env v PYTHONSTARTUP & ~/.pyhonrc.py
			[-i|--interface {ipython, bpython,python}]
			[-c|--command <command>]
			#exe <command> & exit
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]



		showmigrations
		#просмотр списка миграций отсортированных по алфавиту
		#[x] - exe миграция
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--database <db_name>] = "default"
			[-l|--list]
			#show a list of all migrations and which are applied
			#исключает [--plan|-p]
			[--plan|-p]
			#вывод плана миграций(отсортированный в порядке очереди) вместо миграций
			#verbosity level 2+ -> ⊂ all direct migrations dependencies & reverse dependencies(run_before)
			#исключает [-l|--list]
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<app_label> [<app_label> ...]]
			#при !∃ -> вывод ∀ с разбиениям по apps


		sqlflush
		#возвращает sql необходимыи для возвращения ∀ таблиц бд к состоянию fresh install
			[-h|--help]
			[--database <db_name>] = "default"
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
			


		sqlmigrate
		#выводит sql генерируемого миграцией
			#bboard/0001_initial.py
			make migrations bboard 0001
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--database <db_name>] = "default"
			[--backwards]
			#creates sql to UNAPPLY the migration, rather(?) than to apply it
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<app_label> <migration_name>
			#app ⊃ миграции <number_part_of_migration_file_name>

rather:eng:тоже?


		sqlsequencereset
		#prints the sql for resetting {xn} for the given apps
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--database <db_name>] = "default"
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<app_label> [<app_label> ...]



		squashmigrations
		#слияние миграций в одну для уменьшения их числа что ускоряет их применение к свежей бд
		#исп if модель многократно Δ с последующей генерацией миграций => миграций м.б. много
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--no-optimize]
			#исп при неудачном слиянии|неработоспособности результирующей миграции
			#видимо тупое объединение фаилов
			[--noinput|--no-input]
			#не выводить сведения о слиянии
			[--squashed_name <имя_результирующей_миграции>]
			#if отсутствует
				<имя_первой_слитой_миграции>_squashed_<имя_последней_слитой_миграции>.py			
			[--no-header]
			#не добавлять заголовочныи коммент к результату
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<app_alias> [<first_migration_name>] <last_migration_name>
			#указанные миграции ⊂ диапазону
		#~слияние патчей
			#слияние с initial по указанную
				squashmigrations bboard 0004
			#слияние с указанной по указанную
				squashmigrations bboard 0002 0004
		


		startapp
		#создание нового пустого приложения(структуры директорий dj app)
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--template <template>]
			#путь|url для загрузки шаблонов
			[-е|--extension <extension0>[, <extension1> ...] ] = "py"
			#file extension for render
			#мб исп неск раз
			[-n|--name <file_name0> [,<file_name1> ...]]
			#file name(s) to render
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<app_name>
			#app|project name
			[<path_to_dir_of_app_packet]
			#if путь к папке app не указан - пакет с указаным именем будет создан в текущей папке
			#else if папка app указана - она будет преобразована в пакет приложения

		
		
		startproject
		#вероятно = startproject ⊂ django-admin
		
		
		
		test
		#
		
		
		
		testserver
		#
	
	
	
	[django_extensions]
		admin_generator
		#
		
		
		
		clean_pyc
		#
		
		
		
		clear_cache
		#
		
		
		
		compile_pyc
		#
		
		
		
		create_command
		#
		
		
		
		create_jobs
		#
		
		
		
		create_template_tags
		#
		
		
		
		delete_squashed_migrations
		#
		
		
		
		describe_form
		#
		
		
		
		drop_test_database
		#
		
		
		
		dumpscript
		#
		
		
		
		export_emails
		#
		
		
		
		find_template
		#
		
		
		
		generate_password
		#
		
		
		
		generate_secret_key
		#
		
		
		
		graph_models
		#
		
		
		
		mail_debug
		#
		
		
		
		merge_model_instances
		#
		
		
		
		notes
		#
		
		
		
		passwd
		#
		
		
		
		pipchecker
		#
		
		
		
		print_settings
		#
		
		
		
		print_user_for_session
		#
		
		
		
		reset_db
		#
		
		
		
		reset_schema
		#
		
		
		
		runjob
		#
		
		
		
		runjobs
		#
		
		
		
		runprofileserver
		#
		
		
		
		runscript
		#
		
		
		
		runserver_plus
		#
		
		
		
		set_default_site
		#
		
		
		
		set_fake_emails
		#
		
		
		
		set_fake_passwords
		#
		
		
		
		shell_plus
		#
		
		
		
		show_templatetags
		#
		
		
		
		show_urls
		#
		
		
		
		sqlcreate
		#
		
		
		
		sqldiff
		#
		
		
		
		sqldsn
		#
		
		
		
		sync_s3
		#
		
		
		
		syncdata
		#
		
		
		
		unreferenced_files
		#
		
		
		
		update_permissions
		#
		
		
		
		validate_templates
		#
		
		
		
	[sessions]
		clearsessions
		#
		
		
		
		
	[staticfiles]
		collectstatic
		#
		
		
		findstatic
		#
		
		
		runserver
		#запускает отладочный(только?) сервер
			[[<adress>][:][<port>]] = 127.0.0.1:8000(TCP)
			[--noreload]
			#отключение автоперезапуска при Δ кода
			[--nothreading]
			#force one thread
			#по умолчанию режим многопоточный
			[--ipv6] [-6]
			#использовать IPv6
			#адрес по умолч	::1
		#examples
			python manage.py runserver 1.2.3.4
			python manage.py runserver 4000
			

		
		
verbose:eng:подробно?
		
		

DJANGO ENVIRONEMENT
		ENVIRONEMENT VARIABLES
			#их явно можно менять
				os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

			DJANGO_SETTINGS_MODULE
			#⊃ python путь к <project>.settings.main
			
			
			
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
			#модуль административных настроек и классов редакторов(?)


			apps.py
			#модуль с настройками приложения
			#⊃ объявление конфигурационного класса описывающего настройки app
				from django.apps import AppConfig
				
				class <AppName>Config(AppConfig):
					name = '<AppName>'
					#path to app относительно папки проекта в виде строки
					#обязательный
					#создается manage.py при создании app
					#не требуется менять
					label = <str>
					#необязателен, !∃ по умолч => if не указан - используется последний компонент пути ⊃ name(назв папки app)
					#псевдоним app
					#используется 
						для указания app в вызовах manage.py
						...
					#должен быть уникальным в пределах проекта
					verbose_name=<str>
					#имя app выводимое в админке
					#необязателен, по умолч !∃ => if не указан используется label
					path
					#необязателен, по умолч !∃ => if не указан определяется dj


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
		имени якоря(#id?)
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
	#связывает "admin/" со списком маршрутов возвращаемый св-вом urls экземпляра(?а выглядит как класс) AdminSite который хранится в var(?а я думал это модуль) site и представляет текущую административный веб-сайт dj => при переходе по <host>:port/admin/ загружается админка 
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

	.include(arg, namespace=None)
	#two arg
	#принимает строку с путем к модулю ⊃ список маршрутов
	
	
	.reverse_lazy("<route_name>"[,<val_of_url_param>]) -> готовый url
	#генерация url путем обратного разрешения	
		from django.urls import reverse_lazy
		
		class BbCreateView(CreateView):
			...
			success_url = reverse_lazy('index')
			...
			
			
attr класса ~ св-ва класса|статические св-ва в other pl


МОДЕЛИ
#упрощает работу с бд
#ORM
#класс Python, объявляемый на уровне отдельного app
#однозначное и исчерпывающее определение сущности в бд
#описывает таблицу бд в которой будет храниться набор сущностей
#attr описывают поля таблицы
#Python представление таблицы и ее полей/записей
#позволяет описывать структуры бд на высоком уровне не заботясь о добавлении данных вручную
#отдельный экземпляр модели = отдельная конкретная сущность извлеченная из бд = отдельная запись соответствующей табл
#используя объявленные в модели attr класса можно читать/писать val в полях записи
#предоставляет инструменты для выборки, фильтрации и сортировки сущностей из бд => результат: {xn} экземпляров класса модели
#объявляются на уровне app, вроде должны записываться в models.py
#требования к модели
	класс модели должен быть наследником Model ⊃ django.db.models | другого класса модели
	#наследование от другого класса модели ⊃ ряд особенностей
	код классов моделей ⊂ <app>/models.py
	для успешной обработки ядром dj, app ⊃ модели должно ⊂ INSTALLED_APPS
#основная мощь dj
реализуем вывод объявлений из бд
	можно реализовать это вручную написав код 
		создающий в бд таблицу со ∀ необходимыми полями
		считывающий данные из бд
		преобразующий их
		...
#в dj для реализации хранения ∀ сущностей строго определенной структуры достаточно создать модель
#lowlevel
	∀ модель представляет отдельную таблицу бд
	по умолч таблицы получают имена <app_alias>_<model_class_name>
	∀ поле модели представляет отдельное поле в соотв бд
	по умолч поля таблицы называются именами полей модели
	if модель !⊃ объявления ключевого поля => создается dj 
		с именем id
		типом int
		меткой автоинкремента
		и созданным ключевым индексом
	по умолч никакие другие индексы в таблице не создаются
#м.б. создана для представления ∃ в бд таблицы, для чего требуется указать
	имя таблицы
	имена ∀ ⊂ ей полей
#при создании модели для !∃ таблицы требуется генерация и и применение миграции
#большинство таблиц бд ⊃ ключевое поле(для хранения pk), обычно int и автоинкрементное=> уникальные val в него заносит сама СУБД
	#что не требует явного объявления в dj -> dj самостоятельно создает такое поле
		#if создать запись с pk = 2, затем с pk=3, удалить pk=2 и создать новую запись -> pk новой записи будет 4(возможно на больших наборах данных это работает иначе)
#attr класса pk поддерживается ∀ моделями, ⊃ val pk текущей записи
#attr класса м.б. получены только после сохранения
	from bboard.models import Bb
	b1 = Bb(title='...',content='...', price='...')
	b1.save()
	#pk - универсальный attr моделей, предоставляющий доступ к ключевому полю
	#удобен if модель ⊃ ключевое поле с именем != стандарнтному(id) -> не придется вспоминать его имя
	b1.pk			>> 1
	b1.title		>> ...
#∀ классы моделей ⊃ .objects
#.objects ⊃ диспетчер записей, видимо реализует ∀ магию генерации запросов
#совершенно очевидно что .objecs наследуется от models.Model
	БАЗОВЫЕ ИНСТРУМЕНТЫ
	#создание моделей следует за созданием и настройкой проекта и apps
	#большинство сайтов хранит данные бд
	#основные принципы механизма моделей dj
		класс модели
		#представляет ∀ сущности класса и ⊂ в бд
		#описывает набор отдельных val(полей) ⊂ сущности этого класса
		#предоставляет инструменты для работы со ∀ сущностями класса
			извлечение
			фильтрация
			сортировка
			...
		экземпляр класса
		#отдельная сущность класса извлеченная из бд
		#предоставляет инструменты для работы с отдельными val ⊂ сущности
			сохранение
			удаление
			создание новых сущностей
			...
		набор извлеченных из бд сущностей
		#представляется {xn} экземпляров соотв класса модели
	для предоставления отдельного поля ⊂ сущности, в классе модели объявляется attr которому присваивается экземпляр класса, представляющего поле требуемого типа(int,str, float, datetime,...), доп параметры поля указываются в параметрах конструктора
	#через них впоследствии можно получить доступ к val этих полей
#поля хранятся в attr; поведение в методах(не уверен что это good);параметры в Meta;


ДИСПЕТЧЕР ЗАПИСЕЙ
#особая структура(obj) позволяющая манипулировать ∀ совокупностью записей ⊂ модели
#представляется экземпляром класса Manager ⊃ django.db.models
#по идее поддерживается и производными от Manager вроде RelatedManager
	<model>.objects
	
		.__eq__()
		#метод перегрузки =
		
		.__format__()
		.__ge__()
		.__gt__()
		.__hash__()
		#он таки hashable
		.__le__()
		.__lt__()
		.__ne__()
		.__reduce__()
		
		
		.create(<field0>=<val0>, ...)	-> <model_instance>
		#создает новую запись модели, сохраняет ее и возвращает как результат
		#не требует .save()
			r = Rubric.objects.create(name='Мебель')
			#проверим создана ли запись
			r.pk		>> 5
		
		
		.all()	->	django.db.models.query.QuerySet
		#возвращает "набор ∀ записей" модели(экземпляр QuerySet)(iterable)
		#отдельные записи- экземпляры соответствующего класса модели
			[r.name for r in Rubric.objects.all()]
		
		.last()	->	<model_instance>
		#return последнюю запись набора | if набор пуст -> None
			b = Bb.objects.last()
			b.title -> 'Дача'
		#учитывает сортировку заданную вызовом .order_by() | параметром модели ordering
		#противоположен first
		
		.filter([<field0>=<val>, ...])	-> django.db.models.query.QuerySet
		#фильтрация записей по заданным критериям
		#см НАПИСАНИЕ УСЛОВИЙ ФИЛЬТРАЦИИ
		#противоположен .exclude(...)
		#возвращяет другой диспетчер записей ⊃ только отфильтрованные записи
			#∀ объявления с ценой >= 10000
			for b in Bb.objects.filter(price__gte=10000):
				print(b.title)
		#поддерживается QuerySet -> можно сцеплять вызовы
			r = Rubric.objects.get(name='Недвижимость')
			for b in Bb.objects.filter(rubric=r).filter(price__lt=1000000):
				print(b.title)
			#хотя конечно можно обойтись и filter
				for b in Bb.objects.filter(rubric=r, price__lt=1000000):
					print(b.title)
		#без параметров ~ all()
					
		.exclude(<field0>=<val>, ...)	-> django.db.models.query.QuerySet
		#противоположен filter(...)
		#возвращает записи НЕ удовлетворяющие условиям
		#см НАПИСАНИЕ УСЛОВИЙ ФИЛЬТРАЦИИ
			#∀ объявления кроме тех чья цена не менее 10000
			for b in Bb.objects.exclude(price__gte=10000):
				print(b.title)
		#поддерживается QuerySet -> можно сцеплять вызовы(см. .filter)
			#хотя можно обойтись и .exclude() (см .filter)
			
			
		.get(<field>=<val> [, <field>=...])	-> <app>.models.<Model>
		#возвращает одну запись подходящую под критерий
		#быстрее filter()
		#if записей не нашлось -> бросает DoesNotExist чей класс вложен в класс модели чья запись не была найдена
		#if записей неск -> бросает MultipleObjectsReturned ⊃ django.core.exceptions
			r = Rubric.objects.get(name='Растения')
			r.pk	>> 7
		#условия поиска объединяются and
			r = Rubric.objects.get(pk=5, name='Сантехника') 
			>> bboard.models.DoesNotExist: Rubric matching query does not exist
		
				
		<secondary>.get_next_in_order()	->	<primary>
		#доступен if secondary ⊃ задание произвольного переупорядочивания записей связанных с одной записью primary(указан параметр order_with_respect_to)
		#возвращает след в установленном порядке запись
			r = Rubric.objects.get(name='Мебель')
			bb2 = r.bb_set.get(pk=34)
			bb2.pk						>> 34
			bb3 = bb2.get_next_in_order()
			bb3.pk						>> 33
		
		<secondary>.get_previous_in_order() -> <primary>
		#доступен if secondary ⊃ задание произвольного переупорядочивания записей связанных с одной записью primary(указан параметр order_with_respect_to)
		#возвращает предыдущую в установленном порядке запись
			r = Rubric.objects.get(name='Мебель')
			bb2 = r.bb_set.get(pk=34)
			bb1 = bb2.get_previous_in_order()
			bb1.pk						>> 37
		
		.get_or_create(<kwargs_для_фильтрации> [, defaults=None]) -> (найденая|созданная запись, False (if была найдена)|True(if была создана)) -> (<model_instance>, <bool>)
		#возвращает одну запись по фильтрам, при отсутсвии записи => создает ее на основе фильтров и сохранит и возвратит
			defaults:<dict_с_val_для_остальных_полей_создаваемой_записи>
			#при условии что модель !⊃ поля defaults;
			if модель ⊃ поле defaults и по нему нужно выполнить поиск => следует исп фильтр вида
				defaults__exact
		#пример
			Rubric.objects.get_or_create(name='Мебель') 			>> (<Rubric: Мебель>, False)
			Rubric.objects.get_or_create(name='Сантехника')		>> (<Rubric: Сантехника>, True)
		#if записей найдется > одной => бросает MultipleObjectsReturned ⊃ django.core.exceptions
		
		
		.update_or_create(<kwargs_для_фильтров>[, defaults=None])	-> (<model_instance>, <bool>)
		#~.get_or_create, но при нахождении записи обновляет поля в соотв с ⊂ defaults
			Rubric.objects.update_or_create(name='Цветы')	>> (<Rubric: Цветы>, True)
			Rubric.objects.update_or_create(name='Цветы', defaults={'name': 'Растения'})
			>> (<Rubric: Растения>, False)

bulk:eng:наваливать
		
		.bulk_create(<{xn} добавляемых записей> [, batch_size=None]) -> [<model_instance0>,...]
		#добавление записей в модель
			batch_size
			#число записей в одной SQL-команде
			#if !∃ добавление за одну команду
		#return экземпляр QuerySet ⊃ добавленные записи
			r = Rubric.objects.get(name='Бытовая техника')
			Bb.objects.bulk_create([
				Bb(title='Пылесос', content='Хороший, мощный', price=1000, rubric=r),
				Bb(title='Стиральная машина', content='Автоматическая', price=3000, rubric=r)
			])
			>> [<Bb: Bb object (None)>, <Bb: Bb object (None)>]
		#работает напрямую с бд -> возвращаемые записи ⊃ пустое pk поле -> при их создании не вызывается .save() ->
			#-> if модель ⊃ переопред .save() ⊃ доп действия при сохранении - они !exe

		
		.latest(['[-]<field_name0>',<'[-]field_name1'>, ... ])	->	<model_instance> | raise <app>.models.Empty.DoesNotExists
		#получение последней записи модели(⊃ max val в полях даты/времени)
		#if модель ⊃ get_latest_by = '-...' => получение самой ранней записи
		#~.earliest, наоборот
			b = Bb.objects.latest('published')
			b.title			>> 'Стиральная машина'
		#вроде просто исп сортировку по алфавиту
			Bb.objects.create(title='latest', content='test')
			Bb.objects.latest('title')		>> <Bb: Трактор>
			
			
		.earliest(['<field_name0>',<'field_name1'>, ... ])	->	<model_instance> | raise <app>.models.Empty.DoesNotExists
		#возвращает запись ⊃ min val в полях даты/времени(самую раннюю)(посути исп простую сортировку по алфавиту)
		#предварительно exe временную сортировку по возрастанию val полей даты/времени(по умолч - по возрастанию)
		#проверка начинается с первого указанного поля, if val одинаково у неск записей -> проверяется след поле, etc
		#if модель ⊃ get_latest_by = '-...' => получение самой поздней записи
		#if модель ⊃ get_latest_by задающий поля для просмотра -> метод можно вызывать без параметров
		#if подходящих записей не нашлось -> бросает DoesNotExist
			#первое объявление на сайте
			b = Bb.objects.earliest('published')
			b.title			>> 'Дача'
			#последнее
			b = Bb.objects.earliest('-published')
			b.title			>> 'Стиральная машина'
			#самое раннее объявление о продаже транспорта
			r = Rubric.objects.get(name= 'Транспорт')
			b = r.bb_set.earliest('published')
			#первое объявление с ценой не менее 10000
			b = Bb.objects.filter(price__gte=10000).first()
			
			
		.exists()
		#0 args
		#быстр, рекомендуем
		#if набор ⊃ записи -> True
		#else	-> False
			r = Rubric.objects.get(name='Сантехника')
			Bb.objects.filter(rubric=r).exists()	>> False
		
		.count()	-> число_записей_набора
		#0 args
		#быстр, рекомендуем
			Bb.objects.count()	>> 12

		.update()
		#по идее наследуется <QuerySet>
		#см <Query_set>
<instance_of_model>

		.get_next_by_<field_name>([<field>=<val>])
		#доступен if модель ⊃ min одно поле DateField|DateTimeField
		#return запись чье поле с указанным именем ⊃ следующее в порядке увеличения val даты
		#if указаны условия поиска - они также учитываются
			b = Bb.objects.get(pk=1)
			b.title									>> 'Дача'
			#след хронологически запись
			b2 = b.get_next_by_published()
			b2.title								>> 'Дом'
			#след хронологически запись с ценой < 1000
			b3 = b.get_next_by_published(price__lt=1000)
			b3.title								>> 'Мотоцикл'
			
			
		.get_previous_by_<field_name>([<field>=<val>])
		#доступен if модель ⊃ min одно поле DateField|DateTimeField
		#return запись чье поле с указанным именем ⊃ пред в порядке увеличение val даты
		#if указаны условия поиска - они также учитываются
		#~.get_next_by_<field_name>			
		
		
		.delete()
		#удаляет текущую запись и возвращает сведения о кол-ве удаленных записей
			#сама запись ⊂ v остается
			Bb.objets.all()					>> <QuerySet [..., <Bb: post>, ...]
			b = Bb.objets.get(title='post')
			b.delete()
			Bb.objets.filter(title='post')	>> <QuerySet []>
			b								>> <Bb: post>
<Query_set>
#вроде производный Manager -> поддерживает его методы(solid же)
#поддерживает .latest(), .earliest(), .last(), .first()
		
		
		.update(<field_name=new_value>) -> count_changed_fields:int
		#исправляет ∀ записи в наборе
			Bb.objects.filter(price=None).update(price=10)
		#не вызывает .save() -> !exe доп действия ⊃ при его переопределении

		
		.delete() -> (<total_deleted>:int, {<models>:<deleted_count>}
		#0 args
		#удаляет ∀ записи набора
			Bb.objects.filter(content=None).delete()	>> (2, {'bboard.Bb': 2})
		#возвращает dict ~ возвращаемому <запись?>.delete() (?проверить)
		#не вызывает .delete() модели (мб критично if он переопределен)
		
		
		.order_by(['<field0>', '<field1>', ...])
		#сортирует записи по возрастанию val поля указанного в параметре и возвращает получившийся в результате набор записей
		#if у записей равны val первого поля -> проверяются val в след
			for r in Rubric.objects.order_by('name'):
				print(r.name)
			>> Бытовая техник >> Мебель >> Недвижимость ...
			#сначала по названию рубрик, затем по убыванию цены
			for b in Bb.objects.order_by('rubric__name', '-price'):
				price(b.title)
		#∀ вызов отменяет параметры сортировки заданные пред вызовом(а без вызова они что сохраняются?) или в параметре ordering ⊂ модели
			#'?' => сортировка в случайном порядке
			#мб медленна
				for r in Rubric.objects.order_by('?'):
					...
					
					
		.reverse()
		#разворачивает набор записей
			for r in Rubric.objects.order_by('name').reverse():
				print(r.name)
				
				

судя по консоли там ∀ dj на except
	
КЛАССЫ ПОЛЕЙ МОДЕЛЕЙ
#default:∀ поле обязательно для заполнения
#кажется запись = экземпляр класса модели
	django.db.models
	#вроде ⊃ ∀ модели
	#поля также могут принимать args поддерживаемые полями ∀ типов не указанные здесь
	#при исп в шаблоне -> подсвечиваются красным при вводе некорректных данных
	
		CharField(max_length:int)
		#строковое поле ограниченной длинны
		#при привышении max_length -> текст просто уезжает за границу поля
		#занимает в бд V необходимый для ⊃ числа символов указанных в max_length
			#=> предпочтительно
		#название в админке почему-то жирное
		#в формах представляется <input type="text" ...>
			default
			#вроде принимает val ∀ типа
		
			
		TextField([max_length:int])
		#неограниченное текстовое поле(memo-поле)(выглядит как уязвимость)
			TextField(null=True, blank=True)
			#поле которое можно не заполнять
		#⊃ ярлык для перетаскивания границ(Δ размера поля)
		#при привышении лимита по размерам при вводе, появляется полоса прокрутки, автоматически прокручивающаяся к строке ввода
		#в формах представляется <textarea>
		#миграции
			#SQLite
				"<field_name>"  text NOT NULL
		
		
		EmailField([max_length:int=254])
		#str⊃ корректный email
		#вроде простая проверка на соотв шаблону <ascii>@<ascii>.<domain>
		#ящики в зоне .рф вроде не поддерживаются
		#название в админке почему-то жирное
		#в формах представляется <input type="email" ...>
		#миграции
			#SQLite
				"<field_name>" varchar(<max_length_val>) ...
		
		
		URLField([max_length:int=200])
		#str⊃ корректный url
		#работают ∀ url которые принял бы браузер
		#при указании протокола и ctrl-enter над формой появляется ссылка "Сейчас: <a><url></a>", и "Изменить" перед формой
		#название в админке почему-то жирное
		#примеры
			art.com			-> bad
			http:art.com	-> ok
		#в формах представляется <input type="url" ...>
		#миграции
			#SQLite
				"<field_name>" varchar(<max_length_val>) ...
				
		
		SlugField([max_length:int=50[, allow_unicode=<bool>:False]])
		#слаг - str однозначно идетифицирующая запись
		#исп как часть url
		#allow_unicode=True - может ⊃ ∀ символы Unicode; False=> ascii only
		#для ∀ SlugField автоматом создается индекс => db_index=True не требуется
		#может ⊃ только буквы, цифры, подчеркиваний и дефисов
		#название в админке почему-то жирное
		#вроде принимает ∀ строку ни на что не возмущаясь -> не знаю зачем
		#в формах представляется <input type="text">
		#миграции
			#SQLite
				"<field_name>" varchar(<max_length_val>) ...
				
		
		BooleanField([null=<bool>:False])
		#null=True : поле получает возможность хранить null
		#val по умолч: None, а не False, что конечно логично
		#выпадающий список
			Да
			Нет
			Неизвестно
			#а на eng?
		#в формах представляется <select>
		#миграции
			#SQLite
				"<field_name>" bool ...
		
		NullBooleanField
		#~BooleanField(null=True)
		#deprecated, оставлен для совместимости со старыми dj
		#в формах представляется <select>		
		#миграции
			#SQLite
				"<field_name>" bool ...
				
		
		IntegerField()
		#signed 32bit int(обычная длинна)
		#название в админке почему-то жирное
		#по умолч не заполнено
		#⊃ кнопки ⏶⏷ при нажатии Δ число +-1
		#при вводе не числа ввод сбрасывается при отправке
		#при вводе float с нулевой дробной частью -> преобразуется в int
		#при вводе float с дробью, орет что нужно int
		#exp не поддерживаются
		#при вводе числа > 32 бита и добавлении 1 часть разрядов сбрасывает в 0, но число принимается хотя контроль стрелками ломается -> хз как это пашет
		#в формах представляется <input type="number"...>
		#миграции
			#SQLite
				"<field_name>" integer ...
		
		
		SmallIntegerField()
		#signed 16bit int(half length)
		#название в админке почему-то жирное
		#~IntegerField()
		#миграции
			#SQLite
				"<field_name>" smallint ...
		
		
		BigIntegerField()
		#signed 64bit int(double)
		#название в админке почему-то жирное
		#IntegerField() поле в 2 раза длинее
		#в формах представляется <input type="number" min="-9223372036854775808" max="9223372036854775807"...>
		#миграции
			#SQLite
				"<field_name>" bigint ...


		PositiveIntegerField()
		#unsigned 32bit int(usual)
		#название в админке почему-то жирное
		#в формах представляется <input type="number" min="0"...>
		#миграции
			#SQLite
				"<field_name>" integer unsigned NOT NULL CHECK ("<field_name>" >= 0)
				
		
		PositiveSmallIntegerField()
		#unsigned 16bit int(half)
		#название в админке почему-то жирное
		#ругается на отрицательные
		#принимает -0
		#в формах ~PositiveIntegerField
		#миграции
			#SQLite
				"<field_name>" smallint unsigned NOT NULL CHECK ("field_name>" >= 0)
		
		
		FloatField()
		#поле для хранения вещественных чисел
		#слегка длинее BigInteger()
		#название не выделяется жирным в админке в отл от многих других полей
		#val ⊃ . преобразуется в ,
		#⊃ стрелки Δ 1 сбрасывающие дробь
		#при передаче больше одной , сбрасывает ввод при отправке ~ не цифрам
		#в формах представляется <input type="number" step="any" ...>
		#миграции
			#SQLite
				"<field_name>" real ...
		
		
		DecimalField(max_digits, decimal_places)
		#действит число фиксированной длинны
		#реализован Decimal ⊂ decimal
			max_digits
			#max знаков ⊂ ∀ числу
			decimal_places
			#max знаков ⊂ дробной части
		#пример
			price = models.DecimalField(max_digits=8, decimal_places=2)
		#название в админке почему-то жирное	
		#⊃ стрелки с Δ min возможной для указанного decimal_places(0,01 by def) сбрасывающие часть меньше		
		#при вводе большего числа цифр ругается сохраняя ввод в поле
		#в формах представляется <input type="number" step="<10^-(<decimal_places>)>" ...>
		#миграции
			#SQLite
				"<field_name>" decimal ...
				
		
		DateField([auto_now:<bool>=False],[auto_now_add=<bool>])
		#date ⊂ datetime -> ⊃ теже лимиты
		#по идее форматы принимаемых val берутся из соотв параметров
		#True для auto_now|auto_now_add => делает поле невидимым(видимо для пользователя) и необязательным для занесения на уровне dj(editable=False, blank=True)
		#auto_now и auto_now_add взаимоисключающие
			auto_now
			#True: при ∀ сохранении записи => в поле заносится текущая дата
			#может исп для хранения даты посл Δ записи
			#False: val ⊂ полю !Δ при сохранении
			auto_now_add
			#~auto_now, ! текущая дата заносится только при создании записи, ! при послед сохранении
			#исп для ⊃ даты создания записи
		#название в админке почему-то жирное
		#⊃ рядом кнопки "Сегодня"|<значек календаря> ⊃ удобный календарь ⊃ "вчера"|"сегодны"|"завтра" и "отмена"
		#в обычном шаблоне простое текстовое поле !⊃ доп кнопки
		#в формах представляется <input type="text"...>
		#миграции
			#SQLite
				"<field_name>" date ...
		
		
		DateTimeField([default=<datetime>, blank=<bool>, null=<bool>)
		#поле для хранения даты&времени
		#~DateField, ! val ⊂ datetime.datetime
			DateTimeField(auto_now_add=True)
			#при создании записи(экземпляра модели) заполнять его текущими датой и временем
			DateTimeField(db_index=True)
			#создавать для поля индекс(напр для послед сортировки по дате)(т.е. поле походу становится индексом)
		#по идее форматы принимаемых val берутся из соотв параметров
		#что-то не смог отобразить в админке dj
		#в формах представляется <input type="text"...>
		#миграции
			#SQLite
				"<field_name>" datetime ...

		
		TimeField([auto_now:<bool>=False],[auto_now_add=<bool>])
		#поле ⊃ время 24 формат
		#pm|am вроде не жрет
		#по идее форматы принимаемых val берутся из соотв параметров
			h:m:[s[.ms]]
		#datetime.time
			auto_now
			#~DateField
			auto_now_add
			#~DateField
		#название в админке почему-то жирное	
		#⊃ кнопки "Сейчас"|<значек_часов> ⊃	"Выберите время": "Сейчас" "Полночь" "6 утра" "Полдень" "6 вечера" "Отмена"
		#с auto_now_add=True|auto_now=True -> не может быть добавлено в форму(тк поле становится non-editable)
		#в формах представляется <input type="text"...>
		
		
		DurationField()
		#промежуток времени
		#datetime.timedelta
		#название в админке почему-то жирное
		#вроде принимает float -> не удивительно -> это простое текстовое поле
		#в формах представляется <input type="text"...>
		#миграции
			#SQLite
				"<field_name>" bigint ...
				
		
		BinaryField([editable=False])
		#bytes(bytearray?memoryview?) произвольной длинны
		#что-то не отобразилось в админке
		#в формах представляется <input type="text"...>
		#миграции
			#SQLite
				"<field_name>" BLOB ...		
		
		
		GenericIPAdressField(protocol:'IPv4'|'IPv6'|'both'='both',inpack_ipv4:<bool>=False)
		#IP-адресс(IPv4|IPv6)
		#str
			inpack_ipv4
			#True=> преобразование IPv4 адресов записанных в формате IPv6 в формат IPv4
			#требует protocol='both'
		#название в админке почему-то жирное
		#в формах представляется <input type="text"...>
		#миграции
			#SQLite
			#длинна видимо зависит от протокола(39 )
				"<field_name>" char(39)
		
		
		AutoField(auto_created:<bool>=True, primary_key:<bool>=True, serialize:<bool>=False, verbose_name='ID')
		#неуверен в обязательности и полноте параметров
			auto_created
			#
			primary_key
			#
			serialize
			#
		#автоинкрементное поле ⊃ уникальные инкрементирующиеся 32bit int
		#почти ∀ используется как ключевое, и не требует явного объявления(создается dj автоматом при отсутствии в модели)
		#при попытке создания второго начал ругаться
		#миграции
			#SQLite
				"<field_name>" integer NOT NULL PRIMARY KEY AUTOINCREMENT
		
		BigAutoField
		#64bit ~ AutoField
		#миграции
			...
		
		
		UUIDField
		#уникальные, универсальный(?) id
		#представлен UUID from uuid, в виде str
		#мб Δ(например в форме(при указанном editable=True))
		#в форме представляется обычным текстовым полем
		#может исп как ключевое вместо AutoField/BigAutoField
		#требует ручной генерации id для записей
			import uuid
			from django.db import models
			...
			class Bb(models.Model):
				id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
				...
		
		
		<ПОЛЕ_ДЛЯ_⊃_ФАЙЛОВ>
		...
		
		
		<ПОЛЕ_ДЛЯ_⊃_ИЗОБРАЖЕНИЙ>
		...


ПАРАМЕТРЫ ПОЛЕЙ

	ПАРАМЕТРЫ ПОДДЕРЖИВАЕМЫЕ ПОЛЯМИ НЕКОТРЫХ ТИПОВ
		max_length:int
		#при вводе <int> символов дальнейший ввод не возможен
		#при попытке вставить больше сисмволов ввод обрезается
		#не влияет на размер формы by def
		#миграции
			#SQLite
			#передается параметром
				"<field_name>" char(39)
		
		
	ПАРАМЕТРЫ ПОДДЕРЖИВАЕМЫЕ ПОЛЯМИ ∀ ТИПОВ
		
		
		verbose_name
		#имя выводимое в 
			админке
			напротив эл-тов управления в веб-формах
		#для вывода исп <label>
		#if не указано - исп имя поля(самои v) с большои буквы
		#при большой длинне переносится по строкам
		
		
		help_text = <str>:''
		#доп поясняющий текст для вывода(следует сразу за полем, напротив verbose_name)
		#⊃ спец символы HTML не преобразуются в литералы, а выводятся как есть => можно форматировать текст HTML тегами
		#в формах представлен
			<span class="helptext">
				<b>...</b>
			</span>
		#в формах при пустом val не добавляется на страницу
		#миграции -> вроде никак не пишется в бд
		
		
		default
		#val по умолч записываемое в поле if в него не занесено другое val
			#может быть указано 2мя способами
				обычное immutable val
				#не подходит для mutable
					is_active = models.BooleanField(default=True)
				ссылкой на fx вызываемой при создании ∀ новой записи, возвращающей нужное val
					def is_active_default():
						return not is_all_post_passive
					...
					is_active = models.BooleanField(default=is_active_default)
				#при передачи fx она вызывается автоматом(~ ∀ fx)
					models.CharField(..., default=lambda x: x)	>> TypeError: lambda() missing arg
					models.CharField(..., default=lambda: 'val') >> при передаче в форму выведет 'val'
		#вроде исп val возвращаемое __str__|__repr__ при его отсутствии|но вроде не __call__ по краинеи мере if это не fx(видимо ⊃ проверку на тип и if function -> дергает __call__)
			CharField
			TextField
			EmailField
			URLField
			SlugField
			DurationField
			BinaryField
			GenericIPAddressField
			#дергают __str__ -> __repr__
			DateField
			DateTimeField
			TimeField
			#дергают __call__ -> __str__ -> __repr__			
		#при занесении val в форму пользователетем требуется обновление страницы с очисткои кеша(val ⊃ кеша затирает default)
		#исп в формах для заполнения стандартным val
		#исп для задания val для уже ∃ полеи при Δ моделеи
			models
				.ForeignKey
				#видимо требует ∃? val своего типа

				.BooleanField
				#требует bool
				
				.CharField
				#кажется val ∀ типа
				
				.<∀_числовые_поля>
				#int, str ⊃ int, str ⊃ float, float, decimal и возможно ∀ numbers
				#!⊃ ограничения по размеру
				#!поддерживают str ⊃ exp
				#отображают float ⊃ '.'
				
				.<∀_временные_поля>
				#отображают float ⊃ ','
				#вроде принимает val ∀ типов
				
				.DurationField
				#отображают float ⊃ '.'
		#кажется для val не exe валидация(неудивительно тк оно никуда не сохраняется, а просто выводится в форме)
			-> можно написать ∀ приглашение к вводу?
			#нихрена -> числовые поля не жрут str
		#миграции -> вроде никак не пишется в бд


		unique=<bool>:False
		#
			unique=True
			#уникальное поле, для которого автоматом создается индекс(=> его не нужно указывать явно)
			#в текущее поле м.б. занесено только уникальное в пределах таблицы val
			#при попытке занести val ⊂ полю другой записи - вызовет exept IntegrityError ⊂ django.db
		#миграции
			#SQLite
				"<field_name>" UNIQUE ...


		unique_for_date=<str>
		#при указании имени поля даты|даты и времени(DateField|DateTimeField) => текущее поле может ⊃ только val уникальные в пределах даты ⊂ указанному полю
			title = models.CharField(max_length=50, unique_for_date='published')
			published = models.DateTimeField()
			#title позволяет ⊃ только val уникальные в пределах даты ⊂ published
		#миграции -> не смог проверить(вероятно валидация происходит на уровне dj) -> походу исп валидаторами(возм требуется поддерзка бд)
		#разумеется при добавлении записеи через консоль валидации не происходит -> можно добавлять ~ записи
		#в админке dj при попытке создать записи ⊃ ~ даты
			>> Значение в поле «Title» должно быть уникальным для фрагмента «date» даты в поле Published.
		
		
		unique_for_month=<str>
		#~unique_for_date, но вместо даты - конкретный месяц конкретного года
		#миграции -> не смог проверить(вероятно валидация происходит на уровне dj) -> походу исп валидаторами(возм требуется поддерзка бд)
 
		
		
		unique_for_year=<str>
		#~unique_for_date, но вместо даты - год
		#миграции -> не смог проверить(вероятно валидация происходит на уровне dj)
		#не уверен что также принимает date(dj не среагировал)
		
		
		null=<bool>:False
		#позволяет бд оставлять поле пустым
		#не рекомендуется для текстовых полеи(лучше ''(blank=True)) тк это создает два варианта пустых val
		#затрагивает только поле модели, но не поведение dj по умолч => dj в ∀ случае не позволит занести в поле пустое val(контролируется blank)
			null=True
			#таблица может ⊃ val null => быть необязательным к заполнению
			null=False
			#поле обязано содержать val ⊃ пустую строку
		#миграции
			#SQLite
				"<field_name>" NULL|NOT NULL
		
		
		blank=<bool>:False
		#необязательность поля на уровне dj
		#в отличие от null настраивает поведение dj-форм
		#задает поведение dj при выводе форм и валидации введенных в них данных
			blank=True
			#позволяет не заносить в поле val(заносить пустое val(напр '')) даже при null=False
		#очевидно не влияет на бд
		
		
		choices
		#{xn} val доступных для занесения в поле
		#∀ элт д.б. {xn} ⊃ 2 obj
			val записываемое в поле
			#принадлежащее типу поддерживаемому полем
			val выводимое в качестве пункта списка
			#string only(?)
		#м.б. использован для создания полей со списком для выбора
			class Bb(models.Model):
				KINDS = (
					(None, 'Выберите рубрику')
					('b', 'Куплю'),
					('s', 'Продам'),
					('c', 'Обменяю'),
				)
				kind = models.CharField(max_length=1, choices=KINDS)
				...
		#if поле необязательное на уровне dj(blank=False) список вариантов ⊃ пункт '---------'(9 минусов) обозначающий отсутствие val
			#может быть заменен
				...
				(None, '<новый текст пустого пункта>')
				...
				#для текстовых полей можно исп '' вместо None
		#не влияет на бд
		#вроде превращает поле в список ⊃ val своего типа, в формах представленныи <select>
		
		
		db_index=<bool>:False
		#True - создать индекс в таблице по текущему полю
		#разумеется индексов мб неск
		#миграции
			#SQLite
				CREATE INDEX "..." ON "..." ("field_name");

		
		primary_key=<bool>:False
		#True - ключевое поле(поле преобразуется в ключевое) =>неявно null=False, unique=True
		#модель может ⊃ only одно primary_key поле
		#if не задано явно - создается dj автоматом с именем id
		#миграции
			#SQLite
				"<field_name>" ... PRIMARY KEY ...

		
		
		editable=<bool>:True
		#True - вывод в составе формы
		#False - запрет на вывод в составе формы(даже при явном создании его в форме)
		#вроде не во ∀ случаях применим к полю
		#возможность редактировать поле(в форме)(вкладываться в ModelForm)
		
		
		db_column=<str>
		#имя поля, if !∃ => по умолч получает имя поля модели(механизм был указан ранее)
			...
			cf = models.CharField(max_length=4, db_column='new_name')
			...
			>>
				...
				"new_name" varchar(4) NOT NULL
				...


ПАРАМЕТРЫ САМОЙ МОДЕЛИ
#описываются attr непроизводного класса Meta вложенного в класс модели
	
	
	verbose_name
	#имя сущности(ед число) ⊂ модели для вывода в
		админке
	#не влияет на бд
	#вроде не отображается в orm
	
	verbose_name_plural
	#имя набора сущностей(мн число) ⊂ модели для вывода в
		админке
	#не влияет на бд
	#вроде не отображается в orm

	
	unique_together
	#{xn} str ⊃ имена полей ⊃ уникальные(в пределах табл) комбинации val
	#при попытке занести в них ∃ в таблице комбинации val -> вызвает ValidationError exept ⊂ django.core.exceptions
		#комбинации названий товаров и даты публикации должны быть уникальны в пределах модели
		class Bb(models.Model):
			...
			class Meta:
				unique_together = ('title', 'published')
		#можно указать несколько групп
		class Bb(models.Model):
			...
			class Meta:
				unique_together = {
					('title', 'published'),
					('title', 'price', 'rubric'),
				}
		#при попытке записи одинаковых сочетании -> dj выведет <model_verbose_name> с такими val полеи уже ∃
	#в бд дополнительно создает индекс из указанных полеи
		#sqlite
			...
			CREATE UNIQUE INDEX "<app_name>_<project_name>_<field0_field1_...>_..._uniq" ON "<app_name>_<project_name>" ("<field0>","<field1>",...)
			...

	ordering:<{xn}_str_имен_полей_по_кот_должна_exe_sort>
	#параметры сортировки записей моделей по умолч
		'-<field_name>'
		#минус перед названием поля - обратный порядок сортировки
			#сортировка сначало по убыванию published, затем по возрастанию title
			class Bb(models.Model):
				...
				class Meta:
					ordering = ['-published', 'title']
	#по всеи видимости не влияет на бд и обрабатывается dj
	#влияет на порядок вывода в orm -> и в dj
		
	
	
	get_latest_by:<str|{xn}⊃str>
	#имя поля типа DateField|DateTimeField используемое для получения позднейшей/самой ранней записи с помощью .latest()|.earliest() без параметров(поэтому например '-' переданные в get_latest_by и .latest() не накладываются друг на друга)
	#можно задать
		str
		#.latest() вернет самую свежую запись(⊃max val в поле published)
			class Bb(models.Model):
				...
				published = models.DateTimeField()
				
				class Meta:
					get_latest_by = 'published'
		{xn} str
		#использование нескольких полей(if поля записей хранят одинаковое val => сравниваются след поля, ...)
			class Bb(models.Model):
				...
				added = models.DateTimeField()
				published = models.DateTimeField()
				
				class Meta:
					get_latest_by = ['added', 'published']
	#можно инвертировать порядок сортировки => .latest() вернет самую старую запись, .earliest() наоборот
		...
		class Meta:
			get_latest_by = '-published'
	#вроде не влияет на порядок вывода в админке|orm
	#!Δ бд
	
	
	
	order_with_respect_to:'<name_of_field_of_current_model>'
	#позволяет сделать набор записей произвольно упорядочиваемым
	#принимает str ⊃ имя поля текущей модели => записи ⊃ одинаковое val в этом поле м.б. упорядочены произвольно
		#теперь объявления одной рубрики можно произвольно упорядочить
		class Bb(models.Model):
			...
			rubric = models.ForeignKey('Rubric')
			
			class Meta:
				order_with_respect_to = 'rubric'
	#при использовании => dj создает в таблице бд поле
		<имя_заданного_поля>_order
		#⊃ int порядковый номер текущей записи в {xn}(сохраняя тем самым порядок)
		и задает его как val параметра ordering
		#=> записи извлеченные из модели будут отсортированы по этому полю и указать другие параметры будет нельзя
	#вроде вообще не мб исп с ordering
		class Bb(models.Model):
			...
			class Meta:
				...
				ordering = ['-published']
				
				
	
	
	indexes
	#{xn} Index(from django.db.models) ⊃ неск. полей
	#типа индексирования для ускорения дальнейшего поиска?
		#формат конструктора:
			Index(field=[][, name=None])
				fields
				#список str ⊃ имена полей включаемых в индекс
				#для сортировки по убыванию '-<field_name>'
				name
				#имя индекса
				#if не указан => задается dj
	#пример
		class Bb(models.Model):
			...
			class Meta:
				indexes = [
					models.Index(fields=['-published', 'title'], name='main'),
					models.Index(fields=['title', 'price', 'rubric']),
				]
	
	
	index_together
	#альтернативный способ создания индексов ⊃ неск полей
	#принимает последовательность последовательностей str ⊃ имена полей
		class Bb(models.Model):
			...
			class Meta:
				index_together = [
					['-published', 'title'],
					['title', 'price', 'rubric'],
				]
	#для создания одного индекса - {xn} полей(вместо {xn} {xn})
		class Bb(models.Model):
			...
			class Meta:
				index_together = ['-published', 'title']
	
	
	default_related_name:<str>
	#имя attr записи primary для доступа к записям secondary
	#соответствует related_name конструкторов класов полей внешних ключей
	#неявно задает val в related_name и related_query_name конструкторов
	
	
	db_table
	#имя таблицы ⊃ данные модели
	#if !∃ => именуется по умолч





URL МОДЕЛИ
#dj позволяет формировать url на запись модели(url модели)
#url модели может вести на
	страницу ⊃ содержимое записи
	список связанных записей
	...
	ФОРМИРОВАНИЕ URL МОДЕЛИ
	#два способа
		
		
		ДЕКЛАРАТИВНЫЙ
		#описываем формат url в 
			<project>/settings.py
				...
				#"набор" адресов
				#удобно исп lambda
				ABSOLUTE_URL_OVERRIDES = {
						<app_alias>.<model_class_name> : <fx(obj_записи_модели) -> 'str с готовым url'>,
						...
				}
		#пример: объявление dict формирующего url вида "/bboard/<ключ_рубрики>/" на основе экземпляра Rubric(рубрики) ведущий на страницу ⊃ список связанных объяв
			...
			ABSOLUTE_URL_OVERRIDES = {
				'bboard.rubric': lambda rec: "/bboard/%s/" % rec.pk,
			}
			...
			#теперь для помещения url модели в код шаблона -> вставим в шаблон вызов(?по примеру что-то не похоже на вызов) метода .get_absolute_url который унаследован ∀ моделями от базового класса Model
				<a href="{{ rubric.get_absolute_url }}">{{ rubric.name }}</a>
				#~ url модели получается везде(напр в контроллере)
		
		
		ИМПЕРАТИВНЫЙ
		#непосредственное переопределение .get_absolute_url()
			class Rubric(models.Model):
				...
				def get_absolute_url(self):
					return "/bboard/%s/" % self.pk


МЕТОДЫ МОДЕЛИ
	
	.__str__()
	#строковое представление модели
	#используется	
		при указании в шаблоне непосредственого вывода obj записи, а не val его поля|результата метода
		#пример
			{{ rubric }}
	
	
	.save([update_fields:<{xn} полей для обновления>=None][, force_insert=False][, force_update=False])
	#сохранение записи в бд
	#очевидно что update_fields и force_insert конфликтуют с force_insert
		update_fields
		#требуется только при Δ неск полей, и !Δ поля ⊃ много данных(?насколько)
			b = Bb.objects.get(pk=17)
			b.title = 'Земельный участок'
			b.save(update_fields=['title'])
		#if !∃ -> обновляет ∀ поля
		#задает force_update=True
		force_insert
		#True: принудительное создание записи
		#может исп if таблица ⊃ не int с автоинкрементацией(напр str)я val в которое при сохранении нужно заносить вручную, но т.к. pk будет ⊃ val => dj определит ее как уже сохраненную ранее и выполнит UPDATE что приведет к ошибке
		#при force_insert=True, force_update=True(=> при update_fields) => ValueErr: Cannot force both
		force_update
		#True: принудительное обновление записи
		#не требуется при update_fields
		#при force_insert=True	-> ValueErr: Cannot force both
	#переопределяется для добавления логики при сохранении
	#при определении необходимо вызвать метода базового класса
		def save(self, *args, **kwargs):
			# some actions before saving
			if self.is_model_correct():
				super().save(*args, **kwargs)
			# some actions after saving
	#if запись ⊃ ключ(pk заполнено) -> dj определит ее как уже ∃ в бд -> обновит запись используя соотв SQL-запрос UPDATE
	
	
	.delete()	-> (<число удаленных записей ∀ моделей проекта>, {'<model>':<число_удаленных_записей>})
	#удаление записи(прямо из бд)
	#переопределяется для добавления логики при удалении
	#~ .save() требуется вызов из базового класса
		def delete(self, *args, **kwargs):
			# some actions before deletion
			if self.need_to_delete():
				super().delete(*args, **kwargs)
			# some actions after deletion


ФУНКЦИОНАЛЬНОЕ ПОЛЕ
#read only поля ⊃ val вычисляемыми на основе других данных
	СОЗДАНИЕ fx-поля
	#объявление метода без параметров, возвращающего нужное val, чье имя станет именем поля
		#создадим fx-поле title_and_price
		class Bb(models.Model):
			...
			def title_and_price(self):
				if self.price:
					return '%s (%.2f)' % (self.title, self.price)
				else:
					return self.title
		#теперь можно вывести val fx-поля напр в шаблоне
		<h2>{{ bb.title_and_price }}</h2>
	#для fx-поля можно указать название для вывода на страницу в качестве
		заголовка столбца
		надписи на эл-те управления
		...
		#просто нужно присвоить attr short_description ⊃ методу str ⊃ название
			class Bb(models.Model):	
				...
				def title_and_price(self):
					...
				title_and_price.short_description = 'Название и цена'


ВАЛИДАЦИЯ МОДЕЛИ
#проверка данных занесенных во ∀ поля модели на корректность
#м.б. реализована непосредственно в модели|связанной форме
	переопределение метода модели
		
		clean()
		#не должен принимать параметры/возвращать val(только вызывать ValidationError)
		#пример
			#поле описания товара - обязательно, цена - только положительна
			#это лучше делать через параметры конструкторов полей (!пример учебный)
				#прикольно - набираем dict ⊃ err-s для последующего вывода
				class Bb(models.Model):
					...
					def clean(self):
						errors = {}
						if not self.content:
							msg = 'Укажите описание продаваемого товара'
							errors['content'] = ValidationError(msg)
						if self.price and self.price < 0:
							msg = 'Укажите неотрицательное значение цены'
							errors['price'] = ValidationError(msg)
						if errors:
							raise ValidationError(errors)
		#при необходимости вывода err msg относящегося ко ∀ модели, а не опред полям
			#исп в качестве ключа dict ⊃ список err-s val ⊂ v NON_FIELD_ERRORS ⊃ django.core.exceptions
				from django.core.exceptions import NON_FIELDS_ERRORS
				...
				errors[NON_FIELDS_ERRORS] = ValidationError('Ошибка в модели!')
/ВАЛИДАЦИЯ МОДЕЛИ


вызов exept ?= кинуть exept
	ВАЛИДАТОРЫ
	#exe валидацию val ⊂ отдельным полям
	#реализуются классами|fx
	
		СТАНДАРТНЫЕ ВАЛИДАТОРЫ DJ
		#реализующие их классы ⊃ django.core.validators
		#if val не проходит проверку => вызывает
		
			django.core.exceptions
			
			
				.ValidationError(<err_msg>:<str>[, code=None][, params:<dict>=None]
				or
				.ValidationError(<'list'_of_err's>)
				#вторая форма исп при валидации неск(∀) полей
					<err_msg>
					#описание err допущенной посетителем при вводе
					#для вставки val исп заменитель
						% (<ключ_эл-та_dict_переданного в params>s)
						#думаю s в конце - опечатка(либо неважно)
					code
					#можно исп стандартные|кастомные
					#настроятельно рекомендуется указывать(dj devs)
						#текст err msg для которой указан код м.б. Δ формой связанной с моделью|вручную через error_messages в конструкторе поля =>
							if требуется всегда выводить <err_msg> как есть => не следует исп
					params
					#принимает dict ⊃ val для помещения в <err_msg>
					<'list'_of_err's>
					#удобнее исп 
						dict('field_name_with_invalid_data':<{xn}_экземпляров_ValidationError>, ...)
						#∀ экземпляр ValidationError - представляет одну из err
					#может принимать list|tuple, ! => нельзя указать к какому полю относятся те|иные err-s => форма не выведет их напротив нужного эл-та управления
					
					
				NON_FIELD_ERRORS
				#v исп для вывода err msg относящееся ко ∀ модели, а не отдельным полям
				
				
		#можно указать для ∀ поля в параметре
			validators
			#⊃ конструктору поля		
				from django.core import validators
				
				class Bb(models.Model):
					title = models.CharField(max_length=50, validators=[validators.RegexValidator(regex='^.{4,}$')])
		#некоторые типы полей по умолч используют валидаторы
			CharField		->		MaxLengthValidator
			EmailField		->		EmailValidator
			URLField		->		URLValidator
			GenericIPAdressField	->	validate_ipv4_adress
										validate_ipv6_adress
										validate_ipv46_adress
			SlugField				->	validate_slug
										validate_unicode_slug
		
		django.core.validators
			
			
			ВАЛИДАТОРЫ-КЛАССЫ
				
				.RegexValidator(
						regex=None[,
						message:<str>:=None][,
						code=None][,
						inverse_match:<bool>=None][,
						flags=0]
						)
				#проверка на соотв re
					regex
					#re
					#str|<class 'regex'> ⊂ python
					message
					#str ⊃ errMsg
					#if не указан -> исп default msg
					code
					#код ошибки
					#if не указан -> исп default code:
						"invalid"
					inverse_match=False
					#False -> val должно соотв re
					#True -> наоборот
					flag
					#флаги re
					#исп only if re ⊂ str
				
				
				.MinLengthValidator(<min_length>[, message=None])
				#проверяет введенное str val на достаточность длинны
					message
					#сообщение об ошибке
					#if не указан => исп default
					#код ошибки "min_length"
				
				
				.MaxLengthValidator(<max_length>[, message=None])
				#проверяет введенное str val на превышение max length
					#сообщение об ошибке
					#if не указан => исп default
					#код ошибки "max_length"
				
				
				.EmailValidator([message=None][, code=None][, whitelist=None])
				#проверяет email's
					message
					#~others validator
					code
					#~RegexValidator
					whitelist=['localhost']
					#{xn} str⊃ имена доменов не проверяемых валидатором
				
				
				.URLValidator([schemes=][, regex=][, message=][, code=])
				#проверка корректности urls
					schemes=['http', 'https', 'ftp', 'ftps']
					#{xn} str ⊃ обозанчения протоколов для которых будет exe валидация
					regex
					#re для сравнения
					#str|<class 'Regex'> ⊂ Python
					#if !∃ => проверка !exe
					message
					#~others validators
					code
					#~RegexValidator
				
				
				.ProhibitNull([message=None][, code=None])
				##проверяет не содержит ли str нулевой char:'\x00'
					message
					#~others validators
					code
					#код ошибки
					#if не указан-> исп "null_characters_not_allowed"
				
				
				.MinValueValidator(<min_val>[, message=None])
				#проверяет не меньше ли число минимума
					message
					#if не указан -> исп "min_value"
				
				
				.MaxValueValidator(<max_val>[, message=None])
				#проверяет не больше ли число максимума
					message
					#if не указан -> исп "max_value"
				
				
				.DecimalValidator(<max_число_цифр_в_числе>,<число_цифр_дробной_части>)
				#проверяет действительное число фиксированной точности представленное Decimal from decimal
				#коды ошибок
					"max_digits"
					#число цифр во ∀ числе больше заданного
					"max_decimal_places"
					#число цифр дробной части больше заданного
					"max_whole_digits"
					#(цифр в целой части) > (число ∀ цифр) - (число цифр ⊂ дробной части)
			
			
			ВАЛИДАТОРЫ-FX
				
				validate_ipv46_adress()
				#валидация адресов протоколов IPv4/IPv6
				
				
				validate_ipv4_adress()
				#валидация адресов протоколов IPv4
				
				
				validate_ipv6_adress()
				#валидация адресов протоколов IPv6
				
				
				int_list_validator([sep=','][, message=None][, code='invalid'][, allow_negative=False])
				#возвращает экземпляр RegexValidator настроенный на проверку int разделенных указанным символом-разделителем
					allow_negative
					#разрешение отрицательных
			
			
			VAR ⊃ ГОТОВЫЕ OBJ ВАЛИДАТОРА НАСТРОЕННЫЙ ПОД ОПРЕД ПОВЕДЕНИЕ
				
				validate_email
				#экземпляр EmailValidator ⊃ defaults настройки
				
				
				validate_slug
				#экземпляр RegexValidator настроенный на проверку слагов
				#допускает наличие в слагах только
					latin letters
					цифр
					"-"
					"_"
				
				
				validate_unicode_slug
				#~validate_slug, вместо латинских букв - буквы(не символы) unicode
				
				
				validate_comma_separated_integer_list
				#экземпляр RegexValidator настроенный на проверку str ⊂ int разделенные ','
				
				
prohibit:eng:запрещать
ftps
#походу ftp с шифрованием


ВЫВОД СВОИХ СООБЩЕНИЙ ОБ ОШИБКАХ
#видимо то что видит user при вводе в формы
#стандартные сообщения обычно понятны
#указываются в параметре конструкторов полей
	error_messages={'код_ошибки': 'msg', ...}
	#пример
		#указание для поля title своего error message
		from django.core import validators
		...
		class Bb(models.Model):
			title = models.CharField(max_length=50, verbose_name='Товар',
				      validators=[validators.RegexValidator(regex='^.{4,}$')],
				      error_messages={'invalid': 'Неправильное название товара'})
	#коды ошибок явно берутся из валидатора
	#доступные для указания коды ошибок
		
		"null"
		#поле таблицы не может ⊃ null => его следует заполнить
		
		
		"blank"
		#в эл-т управления должно быть занесено val
		#видимо когда пользователь пытается оставить обязательное поле пустым
		
		
		"invalid"
		#неверный формат val
		#видимо когда пользователь вводит дичь
		
		
		"invalid_choice"
		#в поле со списком заносится val не указанное в списке(?как)
		
		
		"unique"
		#в поле заносится не уникальное val
		
		
		"unique_for_date"
		#в поле заносится не уникальное val в пределах даты
		
		
		"invalid_date"
		#некорректная дата(напр 30.14.2018)
		
		
		"invalid_time"
		#некорректное время(напр 25:73:80)
		
		
		"invalid_datetime"
		#некорректное дата и время(напр 30.14.2018 25:73:80)		
		
		
		"min_length"
		#str короче указанного минимума
		
		
		"max_length"
		#str длиннее указанного max
		
		
		"null_characters_not_allowed"
		##str ⊃ "\x00"
		
		
		"min_value"
		#число меньше min
	

		"max_value"
		#число > max
		
		
		"max_digits"
		#общее число цифр в сохраняемом Decimal > заданного max
		
		
		"max_decimal_places"
		#число цифр в дробной части > заданного max
		
		
		"max_whole_digits"
		#(число цифр целой части сохраняемого Decimal) > (max цифр в целой и дробной части) - (число цифр в дробной части)
		
		
НАПИСАНИЕ КАСТОМНЫХ ВАЛИДАТОРОВ
#разумеется if нужный валидатор не ⊂ dj
	
	валидатор-fx
	#должен принимать one arg(wtf?) и вызывать ValidationError ⊃ django.core.exceptions
		#см ValidationErr
	#не должна(не обязана?) возвращать результат
	#пример валидатора четности
		from django.core.exceptions import ValidationError
		
		def validate_even(val):
			if val % 2 != 0:
				raise ValidationError('Число %(value)s нечетно', code='odd', params={'value': val})
		
		class Bb(models.Model):
			...
			price = models.FloatField(validators=[validate_even])	
	
	
	вадидатор-класс
	#исп при необходимости передачи args
	#валидация exe в .__call__() принимающий проверяемое val и бросающее ValidationError при его невалидности
	#пример валидатора вхождения в заданный диапазон
		from django.core.exceptions import ValidationError
		
		class MinMaxValueValidator:
			def __init__(self, min_value, max_value):
				self.min_value = min_value
				self.max_value = max_value
			
			def __call__(self, val):
				if val < self.min_value or val > self.max_value:
					msg = (
					'Введенное число должно находиться'
					'в диапазоне от %(min)s до %(max)s'
					)
					raise ValidationError(
					          msg, code='out_of_range', params=('min': self.min_value, 'max': self.max_value))		

							  
МИГРАЦИИ
#вроде нельзя создать миграцию для пустой модели
#разумеется задает лишь структуру бд -> данные пишутся отдельно
#Python-модуль созданный dj на основе модели, предназначенный для создания в бд ∀ требуемых моделью структур
	таблиц
	полей
	индексов
	правил
	связей
#упрощает жизнь
#при exe порождает команды sql, соотв СУБД указанной в настройка проекта, отправляемые в СУБД
#почти всегда формируются dj по запросу
	#автор не описывает средства dj применяемые для создания миграций вручную
	#описание программых инструментов для формирования миграций вручную:docs.djangoproject.com/en/2.1/ref/migration-operations/
#!dj отслеживает ∀ Δ моделей ⊃ напрямую не затрагивающие структуры бд(видимо не Δ их)
	#напр: при указании в конструкторе поля модели arg verbose_name -> dj все равно создаст в миграции код Δ параметры поля таблицы в бд =>
		ВСЕГДА ПРОДУМЫВАЙ СТРУКТУРУ МОДЕЛЕЙ ЗАРАНЕЕ(до первои миграции) И СТАРАЙСЯ НЕ МЕНЯТЬ ЕЕ
#для отслеживания (не)выполненных миграций dj создает в бд по умолч(?поведение|?бд) таблицу
	django_migrations
	#крайне не рекомендуется трогать руками
	#∀ запись содержит
		имена exe миграций
		app name
		дата и время выполнения
#пример миграции
	from django.conf import settings
	from django.db import migrations, models
	import django.db.models.deletion
	...
	#порядок полеи немного !~ порядку обЪявления в модели
	#dependencies - пред "инкрементные" миграции
	class Migration(migrations.Migration):
		initial = <bool>
		dependencies = [
			migrations.CreateModel(
				name='<ModelName>',
				fields=[
					('id', <полное_обЪявление_поля_из_models>),
					...
				]
			)
		]
#миграции не Δ бд, все-равно генерируют sql
	<app>/models.py
		...
		class ExampleModel(models.Model):
			...
			class Meta:
				ordering = ['-created']
	...
	py manage.py makemigrations && py manage.py sqlmigrate
	>>
		BEGIN;
		--
		-- Change Meta options on fieldstest
		--
		COMMIT;
#при Δ моделеи !Δ структуру бд, Δ отражаются на orm и без создания/exe миграции
		
		
СЛОЖНЫЕ СЛУЧАИ ПРИ МИГРАЦИЯХ
#] нужно связать модели поста и комментария, изначально комментарии ⊃ только текст
	class Post(models.Model):
		text = models.TextField()
		title = models.CharField(blank=True)
		
	class Comment(models.Model):
		text = models.TextField()
		#добавляем связь с постом
		post = models.ForeignKey(Post, on_delete=models.CASCADE)
	py manage.py makemigrations -> You are trying to add a non-nullable field without a default
	#РЕШЕНИЯ
		добавить в модель null=True
		#неправильно, ведь ∀ комментарии должен быть привязан к какому-либо посту
		добавить в модель default=<default_val>
		#неправильно, ведь ∀ комментарии должен быть привязан к какому-либо посту
		удаление ∀ миграции и бд
		использование дата-миграции
			создать новую модель ⊃ связь ForeignKey
				class Comment(models.Model):
					text = models.TextField()
				class PostComment(models.Model):
					text = models.TextField()
					post = models.ForeignKey(Post, on_delete=models.CASCADE)
			создать и применить миграцию
			скопировать данные из Comment в PostComment с помощью дата-миграции
			удалить модель Comment
			переименовать PostComment в Comment
ДАТА-МИГРАЦИЯ
#специальная миграция которая просто запускает пользовательскии Python-код
ФАЙЛЫ МИГРАЦИЙ
#⊃ <app>/migrations/ c именем по умолч 
	<порядковый_номер_из_4х_цифр>_<migration_name>.py
	#номер - помечает очередность формирования
	#не стоит переименовывать после exe т.к. dj использует имена exe миграций
	
	
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
#dj ⊃ свою редакцию python shell - консоль django
#отличия
	в path ⊃ путь к папке проекта в котором запущена консоль
записи модели создаются ~ экземпляру ∀ другого класса - вызовом конструктора, val полей указываются в именованных args


ИНТЕГРАЦИЯ С JUPYTER NOTEBOOK
	pip install ipython jypyter django-extensions
	settings.py
		INSTALLED_APPS = [
			...
			'django_extensions',			
		]
		...
		# dj 3+?
		os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
		
	~/.jupyter/jupyter_notebook_config.py
		c.NotebookApp.browser = ".../Firefox52/firefox.exe -new-window %s"
		...
		c.NotebookApp.port = 20000
		...
		c.NotebookApp.webbrowser_open_new = 1
	сменить defaut браузер на тот-же firefox(52) в PyCharm
	py manage.py shell_plus --notebook
#при Δ проекта(например моделеи) требуется перезапуск kernel



РАБОТА С ДАННЫМИ

	ЗАПИСЬ ДАННЫХ
	
		ПРАВКА ЗАПИСЕЙ
		#Δ ∃ в бд записей - проще всего
		#для этого требуется предварительно извлечь запись
			from bboard.models import Bb
			b = Bb.objects.get(pk=17)
			b							>> <Bb: Bb objects (17)>
			#занесение/Δ данных - простое присвоение в attr
			b.title = 'Земельный участок'
			b.content += ' Большой'
			#после чего выполнить .save()
			b.save()
			#в поле со списком следует заносить val для записи в поле задающееся первым эл-том {xn}
				#походу выбирает эл-т соотв переданному ключу(см. choices)
			b.kind = 's'
			
			
		СОЗДАНИЕ ЗАПИСЕЙ
		#3 способа:
			0. создать пустой экз, записать в поля val и save()
				from bboard.models import Rubric
				r = Rubric()
				r.name = 'Бытовая техника'
				r.save()
				
				
			1. создать экз с передачей val в конструкторе и save()
				r = Rubric(name='Сельхозинвентарь')
				r.save()
				
				
			2. исп create() ⊃ диспетчеру записей
				#сохранение не требуется
				r = Rubric.objects.create(name='Мебель')
				r.pk					>> 5
				
		#при создании записи ∀ способом dj проверяет pk записи
			if (pk == '' or pk == None)(отсутствие ключа) => dj предпологает что записи нет в бд => посылает SQL INSERT
			
			
	ОБРАБОТКА СВЯЗАННЫХ ЗАПИСЕЙ
	
		"ОДИН-СО-МНОГИМИ"
		#поле внешнего ключа secondary всегда ⊃ obj primary представляющий связанную запись
		при создании записи secondary можно присвоить полю внешнего ключа obj представляющий связываемую запись primary
				b = Bb()
				b.title = 'Диван'
				b.contents, b.price = 'Продаваемый', 100
				b.rubric = Rubric.objects.get(name='Мебель')
				b.save()
				#модель представляющая запись primary таблицы получает attr	с именем по умолч <secondary_name>_set(можно изменить указав related_name в конструкторе поля) ⊃ экземпляр RelatedManager ⊂ django.db.models.fields.related
				подробнее django.db.models	fields.related
				
				
		"ОДИН-С-ОДНИМ"
		#поле внешнего ключа secondary всегда ⊃ obj primary представляющий связанную запись
		#простейша => dj ⊃ min соовт инструментов
			установление связи с записью primary в запись secondary
			#присвоением primary в поле внешнего ключа secondary
			#пример
				#создание записи secondary AdvUser и связывание с запись primary User представляющей пользователя admin
					from django.contrib.auth.models import User
					from testapp.models import AdvUser
					#primary
					u = User.objects.get(username='admin')
					#secondary
					au = AdvUser.objects.create(user=u)
					au.user			>> <User: admin>
					#primary получает attr ⊃ связанную запись secondary с именем secondary в low case
					u.advuser		>> <AdvUser: AdvUser objects (1)>
					#=> можно связать запись primary с записью secondary присвоив secondary этому attr(типа вручную)
					#связывание с другой записью той же модели
					au2 = AdvUser.objects.get(pk=2)
					u.advuser = au2
					#save() требуется видимо потому что .create() создает запись в бд
					u.save()
					
					
		"МНОГИЕ-СО-МНОГИМИ"
		#if установлена между двумя моделями -> перед связыванием записи должны быть сохранены
		#в отличие от "ОДИН-СО-МНОГИМИ" и "ОДИН-С-ОДНИМ" attr представляющий поле ⊃ экз RelatedManager
			#=> можно исп методы ⊂ RelatedManager для связывания записей
				.add()
				#подробнее RelatedManager
				.create()
				#подробнее RelatedManager
				.set()
				#подробнее RelatedManager
	ПРОИЗВОЛЬНОЕ ПЕРЕУПОРЯДОЧИВАНИЕ ЗАПИСЕЙ
	#if secondary ⊃ order_with_respect_to -> ее записи связанные с ∀ записью primary можно произвольно переупорядочить получив запись primary и вызвав нужный метод
		.get_<secondary_name>_order()
		#подробнее RelatedManager
		.set_<secondary_name>_order()
		#подробнее RelatedManager
	
	
	МАССОВАЯ ЗАПИСЬ ДАННЫХ
	#dj ⊃ спецсредства для массовой записи ⊂ Manager -> производным RelatedManager
	#быстрее программных инструментов моделей(которые при их исп не работают) т.к. напрямую общаются с бд
	
		.bulk_create(...)
		#подробнее <model>.objects
		
		<...>.update(...)
		#подробнее <model>.objects
		
		<...>.delete(...)
		#подробнее <model>.objects
	
	
	ВАЛИДАЦИЯ МОДЕЛИ
	#исп редко, чаще exe на уровне связанной формы
		full_clean([exclude=None][, validate_unique=True]) -> None
		#валидация модели
			exclude:<{xn}_fields_name>
			#if !∃ -> проверка ∀ полей
			validate_unique
			#True: if модель ⊃ уникальные поля -> проверяются на уникальность заносимых val
		#if данные не корректны
			бросает ValidationError ⊂ django.core.exceptions
			сохраняет в <проверяемая модель>.message_dict = {field:[<messages>,...],...}
		#примеры
			#извлекаем заведомо корректную запись
			b = Bb.objects.get(pk=1)
			#запись корректна
			b.full_clean()
			#пустая запись не корректна(обязательные поля - пусты)
			b = Bb()
			b.full_clean()
			>>
				Traceback ...
					raise ValidationError(errors)
				django.core.exceptions.ValidationError: {
					'title': ['This field cannot be blank'],
					'rubric': ['This field cannot be blank'],
					'content': ['Укажите описание продаваемого товара']
				}
	
	
	ВЫБОРКА ДАННЫХ
		ИЗВЛЕЧЕНИЕ VAL ИЗ ПОЛЯ ЗАПИСИ
			#из attr модели представляющих эти поля
			from bboard.models import Bb
			b = Bb.objects.get(pk=1)
			b.title, b.content, b.price, b.pk	>> ...
		ДОСТУП К СВЯЗАННЫМ ЗАПИСЯМ
		#средства доступа к связанным записям и создаваемые dj различаются для разных типов связей
			"ОДИН-СО-МНОГИМИ"
			#получение записи primary из secondary
				#через attr класса представляющего поле внешнего ключа
					b.rubric	>> <Rubric: Недвижимость>
					b.rubric.name, b.rubric.pk	>> 'Недвижимость', 1
			#т.к. в primary создается attr <secondary>_set ⊃ диспетчер обратной связи RelatedManager
				#чем торгуют в "Недвижимость"
				from bboard.models import Rubric
				r = Rubric.objects.get(name='Недвижимость')
				for bb in r.bb_set.all():
					print (bb.title)
				#дешевле 10 000
				for bb in r.bb_set.filter(price__lte=10000):
					print(bb.title)
				#Δ имя attr primary ⊃ RelatedManager
				class Bb(models.Model):
					rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, related_name='entries')
				...
				>> for bb in r.entries.all(): print(bb.title)
			"ОДИН-С-ОДНИМ"
			#элементарна
			#получить запись primary из secondary
				#через attr класса поля внешнего ключа
				from testapp.models import AdvUser
				au = AdvUser.objects.first()
				au.user	>> <User: admin>
				au.user.username	>> 'admin'
				#из primary можно получить доступ к записи secondary через attr класса с именем secondary
				from django.contrib.auth import User
				u = User.objects.first()
				u.advuser	>> <AdvUser: AdvUser object (1)>
			"МНОГИЕ-СО-МНОГИМИ"
			#набор записей ведомой модели предоставляется диспетчером обратной связи ⊂ attr класса ведущей (представлящий поле внешнего ключа)
				from testapp.models import Machine
				m = Machine.objects.get(pk=1)
				m.name				>> 'Самосвал'
				print(s.name for s in m.spares.all())	>> ['Гайка', 'Винт']
			#доступ к записям ведущей из ведомой
				#через attr <имя_ведущей>_set
				from testapp.models import Spare
				s = Spare.objects.get(name='Гайка')
				print(m.name for m in s.machine_set.all())	>> 'Самосвал'
		ВЫБОРКА ЗАПИСЕЙ
			
			ВЫБОРКА ∀ ЗАПИСЕЙ
			#см RelatedManager-> .all()
			
			
			ИЗВЛЕЧЕНИЕ ОДНОЙ ЗАПИСИ
				.first()
				#см .first()
				
				.last()
				#см .last()
		
				.earliest()
				#см .earliest()
				
				.latest()
				#см .latest()

			
			ПОДСЧЕТ ЗАПИСЕЙ НАБОРА
				.exists()
				#см .exists()
				
				.count()
				#см .count()
			
			
			ПОИСК ЗАПИСИ
			#max частая операция
				
				.get()
				#см .get()
				
				.get_next_by_<field_name>
				#см .get_next_by_<field_name>
				
				.get_previeus_by_<field_name>
				#см .get_previeus_by_<field_name>
				
				.get_next_in_order()
				#см .get_next_in_order()
				
				.get_previeus_in_order()
				#см .get_previeus_in_order()
			
			
			ФИЛЬТРАЦИЯ ЗАПИСЕЙ
			#в отличие от поиска записей мб ∀ колво(⊃ 0)
			#∀ возвращенное число записей не приведет к вызову exept
			#dj ⊃ два противоположных метода для фильтрации
				.filter()
				#см .filter()
				
				.exclude()
				#см .exclude()
			
			
			НАПИСАНИЕ УСЛОВИЙ ФИЛЬТРАЦИИ
			#при записи условий фильтрации в методах вроде filter() и exclude() в формате
				<field>=<value>
				#dj отбирает записи ⊃ поле ⊃ точно совпадающее val
				для сравнений
					без учета регистра
					val >|< заданной величины
					#исп модификаторы
			#нельзя указывать поля несколько раз
				Bb.objects.get(title__icontains='Д', title_contains='о')
					>> SyntaxErr:keyword argument repeated
					
					
			МОДИФИКАТОРЫ
			#добавляется к имени поля и отделяется от него двойным underscore
			<field_name>__<modificator>
			
			exact
			#точное совпадение с учетом регистра
			#~<field_name>=<value>
			#исп if имя поля модели = ключевое слово python(только?)
				class__exact='superclass'
			
			
			iexact
			#точное совпадение без учета регистра
			
			contains
			#val ⊂ полю, ⊃ заданное val С УЧЕТОМ РЕГИСТРА
			
			icontains
			#~contains БЕЗ УЧЕТА РЕГИСТРА
			
			startswith
			#val поля начинается с указанного val С УЧЕТОМ РЕГИСТРА
			
			istartswith
			#~startswith БЕЗ УЧЕТА РЕГИСТРА
			
			endswith
			#~startwith наоборот
			
			iendswith
			#~endswith БЕЗ УЧЕТА РЕГИСТРА
			
			lt
			#val ⊂ полю МЕНЬШЕ заданного
			
			lte
			#val ⊂ полю должно быть МЕНЬШЕ|РАВНО заданному
			
			gt
			#val ⊂ полю должно быть БОЛЬШЕ заданного
			
			gte
			#val ⊂ полю должно быть БОЛЬШЕ|РАВНО заданному
			
			range
			#val ⊂ полю должно ⊂ ЗАДАННОМУ ДИАПАЗОНУ ⊃ ПРЕДЕЛЫ
			#задается кортежем (<начальное_val>, <конечное_val>)
			
			date
			#val поля оценивается как дата
				published__date=datetime.date(2018, 6, 1)
				
			time
			#val поля оценивается как время
				published__time=datetime.time(12, 0)
				
			year
			#сравнение с ГОДОМ извлеченным из val даты ⊂ полю
				published__year=2018
				published__year__lte=2017
			
			month
			#сравнение с МЕСЯЦЕМ извлеченным из val даты ⊂ полю
				
			day
			#сравнение  с ЧИСЛОМ извлеченным из val даты ⊂ полю
			
			week
			#сравнение с НОМЕРОМ НЕДЕЛИ извлеченным из val даты ⊂ полю
			
			week_day
			#сравнение с НОМЕРОМ ДНЯ НЕДЕЛИ извлеченным из val даты ⊂ полю
			
			quarter
			#сравнение с НОМЕР КВАРТАЛА(1...4) извлеченным из val даты ⊂ полю
			
			hour
			#сравнение с ЧАСОМ извлеченным из val даты ⊂ полю
				published__hour=12
				published__hour__gte=13
				
			minute
			#сравнение с МИНУТОЙ извлеченной из val даты ⊂ полю
			
			second
			#сравнение с СЕКУНДОЙ извлеченной из val даты ⊂ полю
			
			isnull
			#True -> поле должно ⊃ null(быть пустым)
			#False -> поле должно ⊃ !null(быть заполненным)
				content__isnull=False
				
			in
			#val поля должно ⊂ указанному списку|кортежу|QuerySet
				pk__in=(1, 2, 3, 4,⊃)
			
			regex
			#val поля должно совпадать с re С УЧЕТОМ РЕГИСТРА
				content__regex='газ|вода'
				
			iregex
			#~regex БЕЗ УЧЕТА РЕГИСТРА
			
		ФИЛЬТРАЦИЯ ЗАПИСЕЙ ПО VAL ПОЛЕЙ СВЯЗАННЫХ ЗАПИСЕЙ
		  'ОДИН-СО-МНОГИМИ'|'ОДИН-С-ОДНИМ'
			ФИЛЬТРАЦИЯ ЗАПИСЕЙ SECONDARY ПО VAL ПОЛЕЙ PRIMARY
			#условие фильтрации записывается в формате
				<имя_поля_внешнего_ключа>__<имя_поля_primary>
					#∀ объявления о продаже транспорта
					for b in Bb.objects.filter(rubric__name='Транспорт'):
						print(b.title)
			ФИЛЬТРАЦИЯ ЗАПИСЕЙ PRIMARY ПО VAL ПОЛЕЙ SECONDARY
			#условие фильтрации записывается в формате
				<secondary>__<имя_поля_secondary>
				#не уникальные
					#∀ рубрики ⊃ объявления с ценой > 10000
					#Недвижимость ⊃ неск объявлений с указанными val полей
					for r in Rubric.objects.filter(bb__price__gt=10000):
						print(r.name)
					>> Недвижимость Недвижимость Недвижимость Транспорт
			#разумеется можно указать другой фильтр исп вместо имени secondary
				#указывается в related_query_name конструктора поля
				class Bb(models.Model):
					rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, related_query_name='entry')
				for r in Rubric.objects.filter(entry__price__gt=10000):
					print(r.name)
		  'МНОГИЕ-СО-МНОГИМИ'
		  #~'ОДИН-С-ОДНИМ'|'ОДИН-СО-МНОГИМИ'
			#∀ машины ⊃ гайки
			for m in Machine.objects.filter(spares__name='Гайка'):
				print(m.name)
			>> Самосвал
			
			#∀ детали ⊂ самосвала
			for s in Spare.objects.filter(machine__name='Самосвал'):
				print(s.name)
			>> Гайка >> Винт
		
		СРАВНЕНИЕ С VAL ДРУГИХ ПОЛЕЙ
		#сравнение val полей друг с другом
		#dj ⊃ класс F ⊃ django.db.models
			F('<имя поля для сравнения>')
			#экземпляр класса исп для сравнения
				#объявления у которых название ⊂ в описании
				from django.db.models import F
				f = F('title')
				for b in Bb.objects.filter(content__icontains=f):
					print(b.title)
			#можно исп для занесения нового val в поля
				#уменьшим вдвое цены ∀ объявлений
				f = F('price')
				for b in Bb.objects.all():
					b.price = f / 2
					b.save()
			#исп для создания вычисляемых полей(см annotate)
			
			
			Value(<value_of_const>[, output_field=None])
			#исп для создания вычисляемых полей(см annotate)
				output_field:<экз_типа>
				#задание типа константы
					None
					#определеяется автоматом
			
			
		СЛОЖНЫЕ УСЛОВИЯ ФИЛЬТРАЦИИ
		#возможности .filter()|.exclude() позволяют лишь указать набор условий объедиенных and
			объединение по правилам ИЛИ
			#исп класс Q ⊃ django.db.models
			Q(<условие_фильтрации>)
			#только одно усл
			#экз исп в вызовах .exclude()|.filter()
			#экз мб объединены
				&
				|
				~
				#эти оператры возвращают новй экз Q
					#выборка объявлений недвижимости ИЛИ бытовой техники
					from django.db.models import Q
					q = Q(rubric__name='Недвижимость') | \
					      Q(rubric__name='Бытовая техника')
					for b in Bb.objects.filter(q):
						print(b.title)
						#видимо ∀ объявление должно ⊂ только одной рубрике, но не обеим сразу
					>> Пылесос >> Стиральная машина >> Земельный участок >> Дом >> Дача
					#выборка объявлений о продаже транспорта с ценой <= 5000
					q = Q(rubric__name='Транспорт') & ~Q(price__gt=5000)
					for b in Bb.objects.filter(q):
						print(b.title)
					>> Мотоцикл
		ВЫБОРКА УНИКАЛЬНЫХ ЗАПИСЕЙ
			distinct([<field0>, <field1>, ...])
			#при исп PostgreSQL можну указать в параметрах имена полей val которых определяют уникальность записи
			#if параметры !∃ -> уникальность записи определяется val ∀ ее полей
				#вывод рубрик ⊃ объявления с ценой > 10000
				for r in Rubric.objects.filter(bb__price__gt=10000).distinct():
					print(r.name)
				>> Недвижимость Транспорт
		
		ВЫБОРКА УКАЗАННОГО ЧИСЛА ЗАПИСЕЙ
		#QuerySet поддерживает срезы
		#отриц индексы не поддерживаются
		#?проверить подробнее
			Rubric.objects.all()[:3]
		
		
		СОРТИРОВКА ЗАПИСЕЙ
			.order_by()
			#см .order_by()
			
		
		АГРЕГАТНЫЕ ВЫЧИСЛЕНИЯ
		#затрагивают val поля ∀ записей модели
			вычисление кол-ва объявлений
				∀
				удовлетворяющих условиям
			среднее арифметическое цены
			max цена
			...
		#exe агрегатными fx
			
			ВЫЧИСЛЕНИЯ ПО ∀ ЗАПИСЯМ МОДЕЛИ
				aggregate(<agregate_fx0>, <agregate_fx1>, ...)
				#return dict ⊃ результары exe соотв агрегатных fx
				#принимает позиционные/именованные args
					#if fx - позиционный arg -> dict = 
						{<field_name_по_кот_exe_вычисление>_<имя_класс_агрегатной_fx>:<результат_exe_fx>}
							#min цена объявления
							from django.db.models import Min
							Bb.objects.aggregate(Min('price'))
							>> {'price__min': 10.0}
					#if fx - именованный arg -> ключ = имени параметра
						from django.db.models import Max
						Bb.objects.aggregate(max_price=Max('price'))
						>> {'max_price': 50000000.0}
						#именованные параметры в отличие от позиционных поддерживают вычисления над результатами агрегатных fx
							result  = Bb.objects.aggregate(diff=Max('price')-Min('price'))
							result['diff']	>> 499999990.0
				#примеры
					result = Bb.objects.aggregate(Min('price'), Max('price'))
					result['price__min'], result['price__max']
					>> (10.0, 5000000.0)
			
			
			ВЫЧИСЛЕНИЯ ПО ГРУППАМ ЗАПИСЕЙ
				annotate(<aggregate_fx0>, <aggregate_fx1>, ...) -> <набор_записей>
				#аннотирование, добавление attr(поля)
				#агрегатное вычисление по группам записей сформированных по критерию
					#число объявления ∀ рубрики
					from django.db.models import Count
					for r in Rubric.objects.annotate(Count('bb')):
						print(r.name, ': ', r.bb__count, sep='')
					>> Бытовая техника: 2>> Мебель: 0 >> ...
					#тоже, но с именованным параметром
					for r in Rubric.objects.annotate(cnt=Count('bb')):
						print(r.name, ': ', r.cnt, sep='')
					#min цена объявления ∀ рубрики
					#рубрики без цены вернут None
					for r in Rubric.objects.annotate(min=Min('bb__price')):
						print(r.name, ': ', r.min, sep='')
				#используя именованный параметр мы создаем в наборе записей новое поле =>
					#можно фильтровать по его val
						#исключим рубрики без объявлений
						for r in Rubric.objects.annotate(cnt=Count('bb')),
												min=Min('bb__price')).filter(cnt__gt=0):
							print(r.name, ': ', r.min, sep='')
				#return новый набор записей, ∀ запсь ⊃ attr с именем 
					<field_name_по_кот_exe_вычисление>_<имя_класс_агрегатной_fx>
					#⊃ результат exe fx
				#простейший способ создания ВЫЧИСЛЯЕМОГО ПОЛЯ
					val поля = экземпляр F|conts(int, float, bool)|для str(видимо не только) -> экземпляр Value ⊃ django.db.models
					для вычислений исп операторы
						+
						-
						#мб исп для изм знака val экземпляров F и Value
						*
						/
						//
						#возвращают экз F
					#примеры
						#вычисление половины ∀ цены объявления
						from django.db.models import F
						for b in Bb.objects.annotate(half_price=F('price')/2):
							print(b.title, b.half_price)
						>>
							Лопата 6067.0
							...
						#∀ названия товаров + рубрика
						from django.db.models.functions import Concat
						for b in Bb.objects.annotate(full_name=Concat(F('title'),
							Value(' ('), F('rubric__name'), Value(')'))):
							print(b.full_name)
						>>
							Стиральная машина (Бытовая техника)
							...
				#указание тип результата возвращаемого exp в экз F(нельзя указать это непосредственно в конструкторе F) -> нужен ExpressionWrapper ⊃ django.db.models, exp - экз F а тип данных - экз поля нужного типа
					from django.db.models import ExpressionWrapper, IntegerField
					for b in Bb.objects.annotate(
						half_price=ExpressionWrapper(F('price')/2, IntegerField())):
						print(b.title, b.half_price)
					>>
						Стиральная машина 1500
						...
						
						
			WRAPPERS
			
				django.db.models
					.ExpressionWrapper(<exp>, <тип_возвращаемого_результата>)
					#может исп для указания типа результата exp(см annotate)
					
					
					
			АГРЕГАТНЫЕ FX
			#экз классов ⊃ django.db.models
			#необязательные параметры конструкторов классов допустимы лишь при задании именованных параметров в вызовах aggregate|annotate (иначе -> exept)
				Count(<field_name>[, distinct=False][, filter:<class 'Q'>=None])
				#число записей ⊃ указанное поле
					#подсчет объявлений с ценой > 100 000 по рубрикам
						for r in Rubric.objects.annotate(cnt=Count('bb', filter=Q(bb__price__gt=100000))):
							print(r.name, ': ', r.cnt)
				#if нужно узнать число записей secondary связаных с этой записью -> следует указать имя secodary
					distinct
					#True -> подсчет только уникальных записей
					filter
					#усл фильтрации в виде экз Q
					#по умолч не exe
			
				
				Sum(<field_name|exp> [, ouput_field=None][, filter=None])
				#вычисляет Σ val поля
					<field_name|exp>
					#поле Σ чьих val вычисляется | exp представленное экз F
					output_field
					#задает тип результата экземпляром класса представляющего поле нужного типа
					#умолч: = типу поля
					filter
					#усл фильтрации экз Q
					#по умолч !exe
				
				
				Min(<field_name|exp> [, ouput_field=None][, filter=None])
				#вычисляет min val из ⊂ полю
				#параметры ~Sum
				
				
				Max(<field_name|exp> [, ouput_field=None][, filter=None])
				#~Min
				
				Avg(<field_name|exp> [, output_field=FloatField()][, filter=None])
				#вычисляет среднее арифметическое val ⊂ указанному полю
				#параметры ~Min
				
				
				StrDev(<field_name|exp> [, sample=False][, filter=None])
				#вычисляет стандартное отклонение
					<field_name|exp>
					#~Min
					sample
					#True -> вычисление стандартного отклонения выборки
					#False -> вычисление стандартного отклонения
					filter
					#~Min
					
					
				Variance(<field_name|exp> [, sample=False][, filter=None])
				#вычисление дисперсии
					sample
					#True -> вычисление стандартной дисперсии образца
					#False -> вычисление дисперсии
					<field_name|exp>
					#~Min
					filter
					#~Min
			ВЫЧИСЛЯЕМЫЕ ПОЛЯ
			#модели могут ⊃ fx-поля чьи val вычисляются на основе других данных, а не берутся из бд
				#вычисляемые поля позволяют перенести подобные вычисления в СУБД вместо dj
			#обычно исп для операций не требующих сложных вычислений(тк SQL < мощен чем Python)
				ПРОСТЕЙШИЕ
					annotate()
					#см. annotate()
			
			
			FX СУБД
			#реализуются и exe СУБД а не py|dj, dj при этом предоставляет для них удобный obj-интерфейс
			#вроде классы определены в отдельных ns?, а .functions ⊃ обертки?
				from django.db.models.functions import Coalesce
				Coalesce		
					>> django.db.models.functions.comparison.Coalesce
			#представляются классами(-> имена начинаются с прописных) django.db.models.functions
			django.db.models
			
				.functions
					
					.Coalesce(<val0>, <val1>, ...) -> <первое_!null_val(⊃ ''|0)>
					#на мой взгляд название и функционал не похожи -> но я представляю насколько трудно выбрать подходящее название при таком размере кодовой базы
						<valn>
						#строковое имя поля|экз F|экз Value
					
					#∀ поля должны ⊃ один тип !, иначе err
						from django.db.models.functions import Coalesce
						for b in Bb.objects.annotate(first_not_null=Coalesce(F('content'), F('price'))):
							print(b.first_not_null)
						>> FieldError: exp contains mixed types. You must set output_field
						#РЕШЕНИЕ
							использовать ExpressionWrapper
							#
							ExpressionWrapper + output_field
							использовать output_field для указания типа результата
								for b in Bb.objects.annotate(first_not_null=Coalesce(F('content'), F('price'), output_field=TextField())):
									print(b.first_not_null)
								>> 
									Хороший мощный
									
									asdf
									...
									#очевидно что content ⊃ '' а не null
								
							
					
eng:coalesce:объединяться
					.Concat
					#вроде создает val конкатенацией других val
					#см annotate

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
		
		
ПАРАМЕТРЫ ПОЛЕЙ И МОДЕЛЕЙ::СТР::50
РЕДАКТОР МОДЕЛИ
...

СВЯЗИ МЕЖДУ МОДЕЛЯМИ
сокр:secondary:связанная вторичная модель
сокр:primary:связанная первичная модель

    СОЗДАНИЕ СВЯЗЕЙ МЕЖДУ МОДЕЛЯМИ
    #связи моделей создаются объявлением ⊃ полей формируемых особыми классами django.db.models(полями внешних ключей)
	django.db.models
		.ForeignKey(
			<link_to_class_primary_model>|<string_with_classname_primary_model>,
			on_delete=django.db.models.<model>,
			[limit_choices_to][,
			related_name:'<имя_записи_в_primary>'|'+'=<имя_secondary>_set][,
			related_query_name:<str>=<secondary_class_name>][,
			to_field=<str>][,
			db_constraint:<bool>=True][,
			...]
		)
		#поле внешнего ключа
		#создание связи "один-со-многими"
		#связывание одну запись первичной модели с ∀ числом записей вторичной
		#наиболее применяющаяся
		#представляет поле внешнего ключа, фактических хранящий ключ записи из первичной модели
		#имя поля внешнего ключа должно обозначать связываемую сущность и быть в единственном числе(напр rubric)
		#на уровне бд поле внешнего ключа модели представляется полем таблицы с именем 
			#<имя поля внешнего ключа>_id
		#в веб-форме такое поле представляется раскрывающимся списком ⊃ строковые представления записей первичной модели(?проверить)
		#модель в которой создается - вторичная
		#некоторые детали синтаксиса см ОБРАБОТКА СВЯЗАННЫХ ЗАПИСЕЙ
		#конструктор, первым параметром принимающий класс связываемой первичной модели в виде
			if код объявляющий класс первичной модели распологается перед кодом класса вторичной => ссылки на класс
				#primary
				class Rubric(models.Model):
					...
				#secondary
				class Bb(models.Model):
					rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT)
					...
			if вторичная модель объявлена раньше первичной => строки с именем класса
				#secondary
				class Bb(models.Model):
					rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT)
					...
				#primary
				class Rubric(models.Model):
					...
			if модель ⊂ другому app ⊂ проекту => строки '<app_name>.<model_class_name>'
				class Rubric(models.Model):
					...
				class Bb(models.Model):
					rubric = models.ForeingKey('rubrics.Rubric', on_delete=models.PROTECT)
			рекурсивная связь => 'self'
				parent_rubric = models.ForeignKey('self', on_delete=models.PROTECT)
			on_delete 
			#поведение при удалении записи первичной модели 
			#управляет каскадным удалением записей вторичной модели при удалении связанной записи в первичной
			#if СУБД поддерживает межтабличные связи с сохранением ссылочной целостности, попытка удаления записи ⊂ primary с которыми связаны записи secondary обламается с IntegrityError exept ⊃ django.db.models
			#v ⊃ django.db.models	
				CASCADE
				#удаление ∀ связанных записей вроричной модели(каскадное)
				PROTECT
				#запрет каскадного удаления вызовом ProtectedError exept ⊂ django.db.models
				SET_NULL
				#if поле внешнего ключа объявлено необязательным на уровне бд(null=True) заносит null в поле внешнего ключа ∀ связанных записей вторичной модели
				SET_DEFAULT
				#if поле внешнего ключа объявлено ⊃ default val(default=<default_val>) => заносит заданное default val в поле внешнего ключа ∀ связанных записей вторичной модели
				SET(<value>|<fx_без_параметров_возвращающая_val>)
				#заносит <value> в поле внешнего ключа
					rubric = models.ForeignKey(Rubric, on_delete=models.SET(1))
					def get_first_rubric():return Rubric.objects.first()
					rubric = models.ForeignKey(Rubric, on_delete=models.SET(get_first_rubric))
				DO_NOTHING
				#заглушка, делает ничего
			limit_choices_to=<dict('field_name':value)>|<class Q>
			#позволяет вывести в списке связываемых записей primary только удовлетворяющие заданным критериям фильтрации
			#критерии фильтрации = dict ⊃ имена полей primary по которым должна exe фильтрация с val указывающими val этих полей => выведены будут записи удовлетворяющие ∀ критериям(т.е. критерии объединяются AND)
				#вывод только рубрик чье поле show=True
				rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, limit_choices_to={'show': True})
			related_name:'<имя_записи_в_primary>'|'+'=<имя_secondary>_set
				'+'
				#if доступ из записи ⊂ primary не требуется => можно указать dj не создавать в нем attr
				#снижает издежки perf
			#str ⊃ имя записи primary для доступа к записям secondary
				#secondary
				class Bb(models.Model):
					#по идее это создает attr в primary
					rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, related_name='entries')
				...
				#получаем первую рубрику
				first_rubric = Rubric.objects.first()
				#получаем доступ к связанным объявлениям через attr entries
				#получение доступа к полям secondary через attr primary
				bbs = first_rubric.entries.all()
			related_query_name:<str>=<secondary_class_name>
			#имя фильтра в secondary фильтрующий val ⊂ записи primary
				class Bb(models.Model):
					rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, relate_query_name='entry')
				#получаем ∀ рубрики ⊃ объявления о продаже домов
				rubrics = Rubric.objects.filter(entry__title='Дом')
			to_field
			#str имя (only уникального(unique=True)) поля primary для связывания
			#if не указан => связывание происходит по ключевому полю primary
			db_constraint:<bool>=True
			#True: создание связи в таблице бд позволяющая сохранить ссылочную целостность(?)
			#False: ссылочная целостность поддерживается только на уровне dj
				#используется только if модель создается на основе ∃ бд ⊃ некорректные данные
		#в формах представляется тегом <select>
		#миграции
			#SQLite
				"<field_name>" integer NULL REFERENCES "<to_value>" DEFERABLE INITIALLY DEFERRED
		
		
		.OneToOneField(
			<link_to_class_primary_model>|<string_with_classname_primary_model>,
			on_delete=django.db.models.<model>,
			[...]
		)
		#связь "один-с-одним" 
		#поле внешнего ключа
		#исп для объединения моделей где одна ⊃ данные дополняющие другую модель(по сути JOIN с ограничениями)
		#стандартная подсис-ма разграничения доступа ⊃ список зарегистрированных пользователей исп особую модель, которую можно заменить - ссылка на класс заменяемой модели пользователя указывается в параметре:
			<project>/settings.py
				...
				AUTH_USER_MODEL = <...>
				...
		#создание модели ⊃ доп данные о зарегистрированном пользователе
			from django.db import models
			from django.contrib.auth.models import User
			
			class AdvUser(models.Model):
				is_activated = models.BooleanField(default=True)
				user = models.OneToOneField(User, on_delete=models.CASCADE)
		#на уровне бд такая связь представляется тем-же полем что и связь "один-со-многими"
		#поддерживает доп параметры ~ .ForeignKey и:
			parent_link
			#применяется при наследовании моделей
		
		
		.ManyToManyField(
			<link_to_class_other_model>|<string_with_classname_other_model>[,
			limit_choices_to=][,
			related_name=][,
			related_query_name][,
			db_constraint=][,
			symmetrical][,
			through][,
			through_fields][,		
		...])
		#связь "многие-со-многими"
		#обе модели равноправны(нет primary/secondary)
			модель ⊃ объявление	- вещущая
			связываемая модель	- ведомая
		#самая сложная в реализации для dj(! не для пользователя)
		#∀ число записей одной модели с ∀ числом записей другой
		#на уровне бд представляется таблицей с именем:
			<app_alias>_<имя_класса_ведущей_модели>_<имя_класса_ведомой_модели>
			#связующая таблица ⊃
				ключевое поле:id
				по полю на ∀ связываемую модель: <model_class_name>_id
				#при создании связи с той-же моделью - связующая таблица ⊃ поля:
					id
					from_<model_class_name>_id
					to_<model_class_name>_id
		#объявляется в одной из моделей(но не в обеих)
			#пока не вижу в этом коде двух множеств
			#ведомая, запчасти
			class Spare(models.Model):
				name = models.CharField(max_length=30)
			#ведущая	
			class Machine(models.Model):
				name = models.CharField(max_length=30)
				spares = models.ManyToMayField(Spare)
				#создает таблицы в бд:
					#связующая
					samplesite_machine_spare
						#⊃ поля
							id
							machine_id
							spare_id
		#поле внешнего ключа
		#имя поля образующего эту связь нужно записывать во мн-ом числе(что очевидно т.к. число записей м.б. ∀)
		#доп параметры
			symmetrical:<bool>=True
			#используется только при связывании с собой
			#True: dj создаст симметричную связь(if машина А ⊃ деталь Б <=> деталь Б ⊂ в машину А)
			#False: ассиметричная связь, для этого dj создает в классе attr для доступа к записям связанной модели в обратном направлении
			through:<link_to_binding_model>|'<name_of_binding_model>'=<создается dj>
			#модель(связующая) представляющая связующую таблицу
			#if не указан => связующая таблица создается dj автоматом
			#при использовании
				!поле внешнего ключа для связи объявляется в ведущей и ведомых
				#при создании этих полей нужно указать
					саму связующую модель(through)
					поля внешних ключей по которым будет установлена связь(through_fields)
			through_field:('<имя_поля_ведущей>', '<имя_поля_ведомой>')
			#требует through
			#указывает поля внешних ключей по которым будет устанавливаться связь
			#if не указано -> поля указываются dj
			db_table
			#имя связующей таблицы
			#обычно применяет if связующая модель не исп
			#if не указано -> связующая табл получит имя по умолч
		
		
		.fields.related
			
binding:eng:связующий				
			.RelatedManager
			#диспетчер обратной связи
			#класс представляющий набор связанных записей secondary таблицы
			#в отличие от диспетчера записей работает только с записями связанными с текущей записью primary
				
				<primary>.<secondary_related_name>_set.add(<связываемые_записи_secondary_через_запятую> [, bulk=True])
				#см ОБРАБОТКА СВЯЗАННЫХ ЗАПИСЕЙ & ForeignKey синтаксис вызова
				#связывает записи переданные secondary с текущей записью primary
				#кажется создает только связи "один-со-многими"
					bulk
					#True -> связывание напрямую отдачей SQL-команды в СУБД без манипуляций с obj моделей представляющих связываемые записи
						#увеличивает perf
					#False -> связывание записей exe манипулированием obj модели представлящими связываемые записи
					#может пригодиться if модели ⊃ переопределенные .save()/.delete() (видимо иначе эта логика не будет зайствована)
				#к моменту вызова add(), текущая запись primary должна быть сохранена
					#т.к. в поле внешнего ключа записи secondary сохраняется ключ записи primary, который м.б. получен только после записи(при использовании моделью стандартного автоинкрементного int pk)
				#пример
					r = Rubric.objects.get(name='Сельхозинвентарь')
					b = Bb.objects.get(pk=24)
					#заносим объявление в сельхозинвентарь
					r.bb_set.add(b)
					b.rubric			>> <Rubric: Сельхозинвентарь>
				#"МНОГИЕ-СО-МНОГИМИ"
					#добавление записей в число связанных с текущей записью
					from testapp.models import Spare, Machine
					s1 = Spare.objects.create(name='Болт')
					s2 = Spare.objects.create(name='Гайка')
					s3 = Spare.objects.create(name='Шайба')
					s4 = Spare.objects.create(name='Шпилька')
					m1 = Machine.objects.create(name='Самосвал')
					m2 = Machine.objects.create(name='Тепловоз')
					m1.spares.add(s1, s2)
					m1.spares.all()	
					>> <QuerySet: [<Spare: Spare object (1)>, <Spare: Spare object (2)>, <Spare: Spare object (4)>]>	

					
				.create(<fields_with_values>)
				#унаследован от Manager
				#создает запись secondary и связывает с текущей записью primary
					b2 = r.bb_set.create(title='Лопата', price=10)
					b2.rubric			>> <Rubric: Сельхозинвентарь>
				#"МНОГИЕ-СО-МНОГИМИ"
					#создание записи связанной модели и связывание с текущей записью
					from testapp.models import Spare, Machine
					m1 = Machine.objects.create(name='Самосвал')
					m1.spares.create(name='Винт')		>> <Spare: Spare object (5)>
					#вроде как создает запись как-бы отдельно(проверить что за херь?)
					m1.spares.all()						>> <QuerySet [..., <Spare: Spare object ...]>
					
				
				.set(<{xn} связываемых записей> [, bulk=True][, clear=False])
				#~.add, но не добавляет записи в число связанных с текущей, а заменяет уже связанные
					bulk
					#~.add
					clear
					#True -> сначала exe очистка списка связанных записей -> указанные записи будут связаны с текущей
					#False: добавление указанных записи !⊂ в списке связанных, и удаление отсутсвующих вызове из этого списка
				#пример
					s5 = Spare.objects.get(pk=5)
					m1.spares.set([s2, s4, s5])
					m1.spares.all()
					>> <QuerySet [<Spare: Spare object (2)>, <Spare: Spare object (4)>, <Spare: Spare object (5)>]>
				
				
				.remove(<удаляемая запись 0>, <удаляемая запись 1>, ...)
				#удаляет указанные записи и списка связанных с текущей записью
					m1.spares.remove(s4)
					m1.spares.all()
					>> <QuerySet [<Spare: Spare objec (2)>, <Spare: Spare object (5)>]>
				#удаление ∀ записей
					#по идее ~ clear
					for spare in m1.spares.all():
						m1.spares.remove(spare)
						
				
				.clear()
				#очистка списка связанных с текущей записей
					m2.spares.set([s1, s2, s3, s4, s5])
					m2.spares.all()						>> <QuerySet [<Spare: ...]>
					m2.spares.clear()
					m2.spares.all()						>> <QuerySet []>
					
				
				<primary_запись>.get_<secondary_name>_order()
				#связан с get?-> вряд ли
				#произвольное переупорядочивание записей
				#return список ключей записей secondary связанный с записью
					class Bb(models.Model):
						...
						rubric = models.ForeignKey('Rubric')
						
						class Meta:	
							order_with_respect_to = 'rubric'
					
					r = Rubric.objects.get(name='Мебель')
					r.get_bb_order()					>> [33, 34, 37]
					
					
				<primary_запись>.set_<secondary_name>_order()
				#произвольное переупорядочивание записей
				#задает новый порядок записей secondary согласно указанному списку ключей записей
					class Bb(models.Model):	
						...
						rubric = models.ForeignKey('Rubric')
						
						class Meta:
							order_with_respect_to = 'rubric'
					r = Rubric.objects.get(name='Мебель')
					r.set_bb_order([37, 34, 33])
				.first()
				#return первую запись модели | if набор пуст -> None
					b = Bb.objects.first()
					b.title			>> 'Стиральная машина'
				#учитывает сортировку заданную вызовом .order_by() | параметром модели ordering
				
				
				.all()
				#наследован от Manager
				#!, возвращаемый набор ⊃ лишь связанные записи(что очевидно)
					r = Rubric.objects.get(name='Недвижимость')
					print([bb.title for bb in r.bb_set.all()])		>> ['Дом', 'Дача']
					
		.ProtectedError
		#exept вызваемый при
			удалении записи первичной модели при указании в связанной вторичной on_delete=models.PROTECT
			#models.PROTECT ⊂ django.db.models
			
			
	<class 'Q'>
	#экземпляр может задавать сложные критерии фильтрации для
		django.db
			models.ForeignKey(..., limit_choices_to=<class 'Q'>)
			
			
∀ поля создаваемые в моделях - по умолчанию обязательны к заполнению
	-> добавить новое, обязательное к заполнению поле в модель уже ⊃ записи => нельзя
	#видимо т.к. тогда придется добавлять val этих полей в уже ∃ записи
	#иначе СУБД вернет err
	
	
СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ МОДЕЛИ
...

ОБРАТНОЕ РАЗРЕШЕНИЕ URLS
...

ФОРМЫ СВЯЗАННЫЕ С МОДЕЛЯМИ
#по идее можно добавлять префикс к именам полеи моделеи чтобы можно было просто связать ∀ поля с формои
	
	class Post:
		user_form_title = ...
		user_form_post = ...
		...
	
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
	#вывод формы с эл-тами управления на отдельных абзацах(элементах <p>)
	#генерирует только код создающий эл-ты управления => теги
		<form>
		<input>
		#придется писать вручную
	#пример структуры
		#код шаблона
			<form method="post">{% csrf_token %}
				{{ form.as_p }}
			</form>
		#результат	
			<form method="post">	
				<input type="hidden" name="csrfmiddlewaretoken"
				value="<token">
				<p>
					<label for="id_<field_name>"><titled_field_name>:</label>
					<select id="id_<field_name>" name="fk">
					...
	
				
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
		#в большинстве случаев сайты используют одну бд
		#конфигурирование dj для использования неск. бд и работа с ними: docs.djangoproject.com/en/2.1/topics/db/multi-db/
		#при исп бд для нескольких app кажется требуются доп настройки
		
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
			#требуется создать пользователя(с необходимыми правами(создание/Δ/удаление таблиц/индексов/связей)) от имени которого будет подключаться dj
			#для создания бд/пользователя можно использовать MySQL Workbench(по ⊂ MySQL)
			
			
			PostgreSQL
			#потребуется установить коннектор
				psycorg
				#2.5.4
				#python-коннектор для PostgreSQL
				#psycopg.org/psycopg
			#дистрибутивные пакеты
				openscg
				#openscg.com/bigsql/postgresql/installers.jsp
				#⊃ python-коннектор
				#поддерживает PostgreSQL 9.4+
			#не создается автоматом
			#требуется создать пользователя(с необходимыми правами(создание/Δ/удаление таблиц/индексов/связей)) от имени которого будет подключаться dj
			#для создания бд/пользователя можно использовать средства этой СУБД
			
			
			Oracle
			#СУБД
			
			
			Microsoft SQL Server
			#СУБД
			
			
			Firebird
			#клиент?
			
			
			IBM DB2
			#СУБД?
			
			
			SAP SQL Anywhere
			#СУБД?
			
			
			ODBC
			#механизм
			
			
		подключение к бд
		#docs.djangoproject.com/en/2.1/ref/databases/
		
		
СОЗДАНИЕ, НАСТРОЙКА И РЕГИСТРАЦИЯ ПРИЛОЖЕНИЙ

APPS
#приложения реализуют отдельные части fx проекта
#∀ проект должен ⊃ min одно app
			