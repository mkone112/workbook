ENG
    frame-work - готовый каркас
    verbose:eng:подробно?
    pretend:eng:предваряет?
    exclusion:eng:?
    dense:eng:?
    presence:eng:?
    Werkzeug:eng(а это вообще eng?):(?)
    whenever:eng:(?)



STATRELOADER
    проект написанный на Python(весьма сомнительно что дело в этом) загружает ∀ модули в ram при запуске => при Δ кода требуется перезапуск
    #судя по сообщениям консоли этим занимается StatReloader


COMMON
    framework - ∀-объемлющая библиотека
    django
    #1.0 появился в 2005
    #для него остается только писать код генерирующий страницы на основе данных из базы
    #следует современным стандартам веб-разработки
        архитектура "модель-контроллер-шаблон"
        использование миграций для внесения изменений в бд
        "написанное однажды применяется везде"
    #полно-fx высокоуровневый framefork
        самостоятельно выполняет типовые задачи
            соединение с бд
            обработка данных полученных от пользователя
            сохранение выгруженных пользователем данных
        предоставляет
            полно-fx подсис-му разграничения доступа
            исключительно мощную, удобно настраиваемую админку(в отличие от ∀ других фреймворков)
    #для разработки среднестатического сайта достаточно только его ∃
    #удобен - содержит:
        легкий и быстрый отладочный сервер
        развитый механизм миграций
        дополнительные lib
            вывод граф миниатюр
            аутентификация через соцсети
            поддержка CAPTCHA
        ...
    #можно подвесить добавив ∀ сложное exp вроде a**b(что довольно очевидно)
    #тянет за собой pytz и sqlparse



    UTC
    #всемирное координированное время



    ACL
    #?что-то с сетями?



    DSN
    #



    FQDN
    #Fully Qualified Domain Name



DRONOV
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


	
THIRD PARTY SOFTWARE
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


    pip
    #⊂ в стандартную поставку Python 3.4+
        pip show <packet>
        #просмотр данных пакета ⊃ зависимости
    # требуется запускать с повышенными правами только if он установленн в директорию требующую соотв прав(напр Program Files)

    
    pypi
    #python package index
    #реестр пакетов


    pytz
    #библиотека
    #выполняет обработку val даты и времени с учетом временных зон


    Werkzeug
    #пакет
        pip install Werkzeug
        
        
    boto
    #lib
    #требуется py manage.py sync_s3 ⊂ django_extensions



WSGI
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
					
					TEMPLATES:<list_of_dicts> = [{
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
									'django.contrib.messages.context_processors.messages',],}
							,},]
					#⊃ ∀ настроики шаблонов(см шаблонизатор)
					
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
						
					
					MANAGERS
					#не уверен в ∃
					#вроде исп manage.py sendtestemail
					
					
					ADMINS
					#не уверен в ∃
					#вроде исп manage.py sendtestemail
					
					
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
	#выводит неожиданно много информации о внутреннеи структуре dj
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
		#Δ возможно в realtime на работающем сервере
		#min 8 char ⊃ цифры, буквы в разных регистрах
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--database <database_to_use>]
			[--version]
			[-v {0,1,2,3}] [--settings <python_path_to_settings_module>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[username] = <current_username>
			#current_username - имя профиля в ос
			


		createsuperuser
		#создание зарегистрированного пользователя с max правами
		#очевидно нуждается в ∃ бд
		#email - opt
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
		#ругается при указании pass не удовлетв min 8 char ⊃ цифры, буквы в разных регистрах
		#можно создать мн-во superusers
		#при ∃ пользователя с таким именем -> предлагает ввести другое


	[contenttypes]
		remove_stale_contenttypes
		#?
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--noinput|--no-input] [--database <db_name>] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		
	[django]
		check
		#проверяет ∀ dj проект на потенциальные проблемы
			manage.py check >> System check identified no issues (0 silenced)
			#?silenced(?~warning)
		#запускается автоматом при старте dj? исп подсисмами(напр для вывода err msg на страницах) dj?
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-t|--tag <tags>]
			#run only check labeled with given tag
			[--list-tags]
			#list available tags
				manage.py check --list-tags
				>>
					admin
					caches
					database
					models
					staticfiles
					templates
					translation
					urls
			[--deploy]
			#check deployment settings
			#вывел мне кучу warnings
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
		#требует наличия соотв по
			manage.py dbshell
			>> CommandError: You appear not to have the 'sqlite3' program installed | on your path
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--database <db_name>] = "default"
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]



		diffsettings
		#отображает Δ settings.py от его default вида(вида key = <new_val>)
		#для DEBUG default val = False
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--all]
			#display all settings, regardless of their val. In "hash" mode(hash - видимо имеется в виду предварение '###' !Δ val
			#default val are prefexed  by "###"
			[--default MODULE]
			#settings module to compare the curr settings against
			#leave empty to compare against dj defaut settings
			[--output {hash, unified}]
			#формат вывода
			#def val вроде hash
				'hash'
				#вывод ∀ Δ настроек, with the settings that don't appear in the defaults followed by ###
				#!~ --all
				'unified'
				#prefixes the default settings with a '-', followed by the changed setting with a '+' 
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]

		
		
		dumpdata
		#output the content of the database as a  fixture(?) of the given format(using ∀ model's default manager unless --all is specified)
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--format <format>]
			#specifies the outpet serialization format for fixtures
			#какие val доступны?
			[--indent <indent>]
			#specifies the indent level to use when pretty-printing output
			#какие val доступны?
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

fixtures:eng:арматура

fixtures
#фаилы предварительнои настроики ⊃ набор данных для загрузки в бд
			

		flush
		#УДАЛЯЕТ ∀ ДАННЫЕ ⊂ ∀ бд, ⊂ добавленные миграциями
			manage.py flush
			>>
				You have requested a flush of the db
				This will IRREVERSIBLY DESROY ∀ data currently in the <abs_path_to_db> db & return each table to an empty state
				Are you sure you want to do this
					Type 'yes' to continue,| 'no' to cancel:
				#ответ регистрозависим
		#does not achive a "fresh install" state
		#судя по выводу dumpdata - в бд остается дохрена данных
			[-h|--help] [--noinput|--no-input] [--database <db_name>] [--version] [-v {0,1,2,3}] [--settings <setting>]
			[--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		

		
		inspectdb
		#(sic!) introspects the db tables & outputs a dj model module
		#вроде выводет описание ∀ содержимого бд в виде моделеи
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
		#вроде исп GNU gettext
			py manage.py makemessages -l pt_BR
			>> CommandError: Cant find msguniq. Make sure you have GNU gettext tools 0.15+
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
			#initial ⊃ only "# Generated by Django ... <datetime>"
			[--check]
			#exit with !0 status if model changes are missing migrations
			#вывод сведений о Δ моделей с последней миграции без формирования миграции
			#else >> "No changes detected"
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
			#?создает таблицы для apps без миграций
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<app_alias> [<migration_name>|<номер>]]
			#без указания -> exe ∀ не exe миграции ⊂ ∀ apps
			#без указания <migration_name> => ∀ миграции ⊂ <app>
		migrate <app_alias> zero
		#отмена ∀ миграций ⊂ app с удалением ∀ созданных ими структур из бд
			#НЕЛЬЗЯ ОТМЕНИТЬ ОТДЕЛЬНУЮ МИГРАЦИЮ
		#?~ manage.py flush

			
			
		sendtestemail
		#отправка testemail
			[-h|--help]
			[--managers]
			#исп адреса указанные в settings.MANAGERS(⊄ settings by def)
			[--admins]
			#исп адреса указанные в settings.ADMINS(⊄ settings by def)
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#возм умеет принимать emails в args
			py manage.py sendtestemail >> err: You must specify some email recipients| pass the --managers|--admin opt


		shell
		#запускает консоль dj
		#пытается исп IPython|bpython при наличии
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--no-startup]
			#if using plain python -> ignore env v PYTHONSTARTUP(?) & ~/.pythonrc.py(?)
			[-i|--interface {ipython, bpython,python}]
			#разумеется соотв интерфеис должен ∃
			[-c|--command <command>]
			#exe <command> & exit
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]



		showmigrations
		#просмотр списка миграций отсортированных по алфавиту
		#[x] - exe миграция
		#optional args(вероятно могут стоять в ∀ порядке)
		#-p/-l почти не отличаются
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
			#при !∃ >> ∀ с разбиениям по apps


		sqlflush
		#возвращает sql необходимыи для возвращения ∀ таблиц бд к состоянию fresh install
			[-h|--help]
			[--database <db_name>] = "default"
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#пример
			py manage.py sqlflush
				BEGIN;
				DELETE FROM "auth_group_permissions";
				DELETE FROM <table>;
				...
				COMMIT;
			


		sqlmigrate
		#выводит sql генерируемого миграцией
			#bboard/0001_initial.py
			make migrations bboard 0001
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--database <db_name>] = "default"
			[--backwards]
			#creates sql to UNAPPLY the migration, rather(?) than to apply it
				py manage.py sqlmigrate --backwards app 0001
				>>
					BEGIN;
					--
					-- Create model <model_name>
					--
					DROP TABLE "<app_name>_<model_name>"
					COMMIT;
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<app_label> <migration_name>
			#app ⊃ миграции <number_part_of_migration_file_name>

rather:eng:тоже?


		sqlsequencereset
		#?prints the sql for resetting {xn} for the given apps
		#хз зачем - мне ен вывел ничего
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
		#создание структуры директории проeкта
		#args ~ startapp



		test
		#discover & run tests ⊂ specified modules|current dir
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--noinput|--no-input]
			[--failfast]
			#break test suite after first fail
			[--testrunner <testrunner>]
			#use specified test runner class instead of the one specified by the TEST_RUNNER setting(видимо ⊂ settings.py ⊂ project)
			[-t|--top-level-directory <top_level>]
			#top level of project for unitest discovery
			[-p|--pattern <pattern>] = test*.py
			#the test matching pattern
			[-k|-keepdb]
			#preserves the test db between runs
			[-r|--reverse]
			#reverse test cases order
			[--debug-mode]
			#sets settings.DEBUG = True
			[-d|--debug-sql]
			#prints logged SQL queries on failure
			[--parallel [N]]
			#use up to N processes
			[--tag <tags>]
			#run only tests ⊃ <tags>
			#мб исп неск раз
			[--exclude-tag <tags>]
			#искл тесты ⊃ <tags>
			#мб исп неск раз
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[test_label0 [test_label1 ...]]
			#module paths to test(module name|TestCase|TestCase.test_method)

preserves:eng:предохраняет?

		testserver
		#(?)runs a development server ⊃ data from given fixtures
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--noinput|--no-input]
			[--addrport <addrport>]
			#port|ip:port to run server
			[--ipv6]
			#use ipv6 address
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[fixture0 [fixture0 ...]]
			#path to fixtures to load before server running
	
	[django_extensions]
		admin_generator
		#generate a 'admin.py' for given app(models)
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-s|--search-field <search_field>] = ('name', 'slug')
			#fields named like this will be added to 'search_fields'
			#?может это для admin.site.register(<field>)
			[-d|--date-hierarchy <date_hierarchy>] = ('joined_at', 'updated_at', 'created_at')
			#a field named like this will be set as 'date_hierarchy'
			[-p|--prepopulated-fields <prepopulated_fields>] = ('slug=name',)
			#(?)these fields will be prepopulated by the other field
			#the field names can be specified like	
				'spam=eggA,eggB,eggC'
			[-l|--list-filter-threshold <list_filter_threshold>] = 100
			#if foreign key ⊂ < LIST_FILTER_THRESHOLD items it will be added to 'list_filter'
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			app_name [model_name [model_name ...]]


prepopulated:eng:?

by def pycharm игнорит .pyc и не дает сождавать их в file tree


		clean_pyc
		#remove ∀ py bytecode compiled files ⊂ project(-> противоположна compile_pyc)
		#работает вполне ожидаемым образом
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-o|-O|--optimize]
			#remove ∀ optimized py bytecode files
			#а без него? -> не заметил Δ
			[-p|--path]
			#specify path to recurse into
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		

какова логика порядка альтернативных args в справке утилит manage.py?
#пример: py manage.py help clear cache >> ... [--all, -a ...] ... [-v, --verbosity ...]
#подозреваю - сортировка по читабельности -> на примере sqlcreate так и не скажешь
	#возможно по времени появления

		clear_cache
		#fully clear site-wide cache
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--cache <cache>]
			#name of cache to clear
			[-a|--all]
			#clear ∀ configured caches
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		compile_pyc
		#compile py bytecode files for project(-> противоположна clean_pyc)
		#ничего не выводит
		#разумеется хранит ∀ в __pycache__
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-p|--path]
			#specify path to recurse into
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		create_command
		#creates a dj management dir structure(py packet) for given app name in the app dir
			app/management/
				__init__.py
				commands/
					__init__.py
					sample.py
						from django.core.management.base import BaseCommand
						class Command(BaseCommand):
							help = "My shiny new management command."
							def add_arguments(self, parser):
								parser.add_argument('sample', nargs='+')
							def handle(self, *args, **options):
								raise NotImplementedError()
		#ничего не выводит(по краинеи мере при успехе)
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-n|--name <command_name>]
			#name to use for the management command
			[-b|--base <base_command>]
			#the base class used for implementation of this command
				Base
				App
				Label
				NoArgs
			[--dry-run]
			#don't actually create ∀ files
			#разумеется у меня нихрена не вывел
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			app_label [app_label ...]
		
		
		
		create_jobs
		#creates a dj jobs command dir structure for the given app name in curr dir
			app/jobs/
				daily/
					__init__.py
				hourly/
					__init__.py
				monthly/
					__init__.py
				weekly/
					__init__.py
				yearly/
					__init__.py
				__init__.py
				sample.py
					from django_extensions.management.jobs import BaseJob
					class Job(BaseJob):
						help = "My sample job."
						def execute(self):
							# executing empty sample job
							pass
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<app_label> [<app_label> ...]



		create_template_tags
		#creates a dj template tags dir structure for the given app in the app's dir
			py manage.py create_template_tags app
				app/templatetags
					__init__.py
					app_tags.py
						from django import template
						register = template.Library()
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-n|--name <tag_library_name>] = `appname`_tags	(да - это grave accents)
			#the name to use for the template tag base name
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<app_label> [<app_label> ...]
		
		
		delete_squashed_migrations
		#deletes left over migrations that have been replaced by a
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--noinput|--no-input]
			[--dry-run]
			#don't actually delete|change ∀ files
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			app_label
			[squashed_migration_name] = <first_found_migration>
			#the squashed migration to replace
		


		describe_form
		#outputs the specified model as a form definition to shell
		#adding labels(titled) & Form to form field name!
			py manage.py describe_form app.FieldsTest
				from django import forms
				from app.models import FieldsTest
				class FieldsTestForm(forms.Form):
					cf = forms.CharField(label='Cf')
					t0 = forms.DateTimeField(label='T0')
					t0 = forms.DateTimeField(label='T1')
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--fields <fields>]
			#describe form with these fields only
				py manage.py describe_form app.FieldsTest --fields cf
					...
					class FieldsTestForm(forms.Form):
						cf = forms.CharField(label='Cf')
			#мб исп неск раз, но я не понял как передавать неск val в один --fields
				... --fields cf t0	>> err
				... --fields "cf" "t0"	>> err
				... --fields 'cf' 't0'	>> err
				... --fields cf, t0	>> err
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<label>.<model>
			#app & model names


describe:eng:?


		
		drop_test_database
		#drops test db for this project
		#кладет db?
			py manage.py drop_test_database
			>>
				You have requsted to drop the test database.
				This will IRREVERSIBLY DESTROY
				∀ data in the db "<path>"
				Are you sure you want to do this?
				>> yes
					>> Reset successful
					#но что-то !Δ
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--noinput]
			#вроде !⊃ --no-input
			[-U|--user <user>]
			#use another user for the db then defined in settings.py
			[-P <password>]
			#use another password for the db then defined in settings.py
			[-D|--dbname <db_name>]
			#use another db name for the db then defined in settings.py
			[-R|--router <router>]
			#use another router-db for the db then defined in settings.py
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]

		
		
		dumpscript
		#dumps the data as a customised python script
		#генерит простои скрипт(?не знаю с каким назначением) и выводит его в консоль
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--autofield]
			#include Autofields (like pk fields)
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			appname [appname ...]
		
		
		
		export_emails
		#export user email list in one of a number of formats
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-g|--group <group>]
			#limit to users which are part of the supplied group name
			[-f|--format <format>]
			#output format
				adress
				emails
				google
				outlook
				linkedin
				vcard
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		find_template
		#finds the location of the given template by resolving its path
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<template0> <path0> [<template1> <path1>]

		
		
		generate_password
		#generates a new pass that can be used for a user password
			py manage.py generate_password --length >> BAPCtgaWXx
		#uses dj core's default parrword generator
			`BaseUserManager.make_random_password()`
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--length [<length>]]
			#password length
			#может в справке err? - как val мб optional?(реально opt - видимо для упрощения генерации запросов к manage.py)
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		generate_secret_key
		#generates a new SECRET_KEY that can be used in a project settings file
			py manage.py generate_secret_key >> <new_secret_key>
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		graph_models
		#creates a GraphViz dot file for the specified app names
		#multiple app names will all be combined into a single model
		#output is usually directed to a dot file
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--pygraphviz] [--pydot][--dot][--json]
			#output graph data as [image using PyGraphViz|image uring PyDot(Plus)|raw DOT(graph description lang) text data|JSON]
			[-d|--disable-fields]
			#don't show the class member fields
			[--disable-abstract-fields]
			#don't show the class member fields that were inderited
			[-g|--group-models]
			#group models together respective to their app
			[-a|--all-applications]
			#auto include ∀ apps from INSTALLED_APPS
			[-o|--output <file>]
			#render output file
			#type of output dependend on file extensions
				png|jpg
				#render graph to image
			[-l|--layout <layout>]
			#layout to be used by GraphViz for visualization
				circo
				dot
				fdp
				neato
				nop
				nop1
				top2
				twopi
			[-t|--theme <theme>]
			#supplied are
				'original
				'django2018'
			#i can create my own by creating dot templates ⊂
				'django_extentions/graph_models/themename/'
			[-n|--verbose-names]
			#use verbose_name of models&fields
			[-L|--language <language>]
			#for verbose_name localization
			[-x|--exclude-columns <columns>]
			#exclude columns from the graph
			#can also loadexclude list from file
			[-X|--exclude-models <models>]
			#exclude models from the graph
			#can also load exclude list from file
			#wildcards (*) are allowed
			[-I|--include-models <models>]
			#restrict the graph to specified models
			#wildcards (*) are allowed
			[-e|--inderitance]
			#include inderitance arrows(default)
			[-E|--no-inderitance]
			#do not include inderitance arrows
			[-R|--hide-relations-from-fields]
			#don't show relations as fields in the graph
			[-S|--disable-sort-fields]
			#don't sort fields
			[--hide-edge-labels]
			#don't show relations labels in the graph
			[--arrow-shape {box, crow, curve, icurve, diamond, dot, inv, none, normal, tee, vee}] = dot
			#arrow shape to use for relations
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<app_label0> [<app_label1> ...]]
		
		
		
		mail_debug
		#starts a test mail server for development
			py manage.py mail_debug >> Now accepting mail at 127.0.4.8:1025
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--output <file>]
			#file to send a copy of ∀ msgs(not flush immediately)
			[--use-settings]
			#use EMAIL_HOST & HOST_PORT ⊂ dj settings
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		merge_model_instances
		#removes duplicate model instances(val самих моделеи?) based on a specified model & fields names
		#make sure that any OneToOne|ForeignKey|ManyToMany relationships attached to a deleted model(s) get reattached to the remaining model
		#based on the following:
			https://djangosnippets.org/snippets/2283/
			https://stackoverflow.com/a/41291137/2532070
			https://gist.github.com/edelvalle/01886b6f79ba0c2dce66
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		notes
		#show ∀ annotation ~ TODO | FIXME | BUG | HACK | WARNING | NOTE | XXX ⊂ .py & .html
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--tag <tag>]
			#search for specific tags only
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		passwd
		#clone of the UNIX `passwd` for django.contrib.auth
		#Δ пароля
		#deprecated!
			py manage.py passwd
			>>
				`django_extensions.management.commands.passwd` is deprecated. You shiuld use built-in `changepassword` django command instead
				#но все-же пашет и предлагает сменить pass
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback]
			[--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[username]



		pipchecker
		#scan pip requirement files for out-of-date packages
		#⊅ args что-то вылетел в except
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-t|--github-api-token <token>]
			[-r|--requirement <filename>]
			#check ∀ the packages ⊂ requirements file
			#мб исп неск раз
			#а if без него?
			[-n|--never]
			#also show when newer version then available is installed
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		print_settings
		#print active dj settings
		#название говорит само за себя
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--format <format>]
			#output format
			[--indent <indent>]
			#indent level for JSON & YAML
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<setting> [<setting> ...]]
			#specifies setting to be printed
		
		
		print_user_for_session
		#print the user info for provided session key
		#very helpful when trying to track down the person who experienced a site crash
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<session_id> [<session_id> ...]
			#user session id
		


		reset_db
		#resets the db for this project
			py manage.py reset_db
			>>
				You have requested a db reset.
				This will IRREVERSIBLY DESTROY
				∀ data in the db "<abs_path_to_db>"
				Are you sure you wat to do this? yes|no
		#сносит ∀ кроме служебнои инфы бд
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--noinput]
			#вроде !⊃ --no-input
			[--no-utf8]
			#tells dj to not create a UTF-8 db
			[-U|--user <user>]
			#use another user for the db than ⊂ settings.py
			[-O|--owner <owner>]
			#use anther owner for creating the db than the user dfined in settings| --user
			[-P|--password <password>]
			#use another password for the db than ⊂ settings.py
			[-D|--dbname <db_name>]
			#use another db_name than ⊂ settings.py
			[-R|--router <router>]
			#use another router-db than ⊂ settings.py
			[-c|--close-sessions]
			#close db connections before dropping db
			#PostgreSQL only
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		reset_schema
		#recreates the public schema for this project
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--noinput]
			#вроде !⊃ --no-input
			[-R|--router <router>]
			#router-db instead of the one ⊂ settings.py
			[-S|--schema <schema>]
			#drop this scheam instead of "public"
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		runjob
		#run a single maintenance job
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-l|--list]
			#∀ jobs with thier description
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<app_name>] [<job_name>]



		runjobs
		#runs scheduled maintenance jobs
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-l|--list]
			#∀ jobs with thier description
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<when>]
			#opts
				minutely
				quarter_hourly
				hourly
				daily
				weekly
				monthly
				yearly
		
		
		
		runprofileserver
		#starts a lightweight Web server ⊃ profiling
		#у меня что-то вывалилось в except
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--noreload]
			#no auto-reloader
			[--nothreading]
			[--prof-path <prof_path>]
			#specifies the dir which to save profile information in
			[--prof-file <prof_file>] = "{path}.{duration:06d}ms.{time}"
			#set filename format
			[--nomedia]
			#don't protile MEDIA_URL
			[--use-cprofile]
			#use cProfile if available
			#disabled per default because of incompatibilities
			[--kcachegrind]
			#create kcachegrind compatible lsprof files
			#requires & auto enables cProfile
			[--nostatic]
			#tells dj to not auto serve static files at STATIC_URL
			[--insecure]
			#allows serving static files even if DEBUG = False
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[addport]
			#port|addr:port]
		
		
		runscript
		#runs a script in dj context
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--email-notifications]
			#send email notification for command
			#не очень понял откуда берутся email's
			[--email-exception]
			#send email notification for command exeptions
			[--fixtures]
			#(?)also look in app.fixtures subdir
			[--noscripts]
			#don't look in app.scripts subdir
			[-s|--silent]
			#don't show errs/tracebacks
			[--no-traceback]
			#don't show traceback
			[--script-args [SCRIPT_ARGS [SCRIPT_ARGS ...]]]
			#space separated args list to be passed to the script
			#note that the same args will be passed to ∀ named scripts
			[--dir-policy {none, each, root}]
			#policy of selecting scripts execution dir(for ∀ scripts)
				none
				#curr dir
				each
				#start ∀ scripts in thir dirs
				root
				#in BASE_DIR
			[--chdir <chdir>]
			#if ∃ --dir-policy -> determines execution dir
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<path_to_script> [<path_to_script> ...]
		
		
		
		runserver_plus
		#starts a lightweight web server for dev
		#Werkzeug required
			pip install Werkzeug
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-6|--ipv6]
			[--noreload]
			#not use auto-reloader
			[--browser]
			#open a browser
			[--nothreading]
			#что будет if указать с --threaded? -> не вывел ничего не необычного
			[--threaded]
			#что будет if указать с --nothreading? -> не вывел ничего не необычного
			[--output <file>]
			#file to send a copy ∀ msgs(not flushed immediately)
			[--print-sql]
			#(?)print sql queries as they're executed
			#вывел only запросы что по идее отражено в описании
			[--print-sql-location]
			#(SIC!!!)show location in code where SQL query generated from
			#вернул тонну except, может они ⊃ информацию о источнике, может баг, а может не хватает ∀ модуля
			[--cert <path_to_certificate_file>]
			#deprecated alias for --cert-file
			[--cert-file <path_to_SSL_.crt_certificate_file>]
			#if not provided -> path from --key-file will be selected
			#Either --cert-file|--key-file must be provided to use SSL
			[--key-file <key_SSL_.key_file_path>]
			#if not provided -> path from --cert-file will be selected
			#Either --cert-file|--key-file must be provided to use SSL
			[--extra-file <extra_files>]
			#(?)auto-reload whenever the given file changes too
			#мб исп неск раз
			[--reloader-interval <interval>] = 1
			#secs
			#after how many secs auto-reload should scan for updates in pooler-mode
			[--reloader-type <reloader_type>] = auto
			#werkzeug reloader type
				auto
				watchdog
				stat
			[--pdb]
			#drop into pdb shell at the strt of ∀ view
			[--ipdb]
			#drop into ipdb shell at the strt of ∀ view
			[--pm]
			#drop into (i)pdb shell if an exception is raised in a view
			[--startup-messages <startup_msgs>] = reload
			#when to show startut msgs
				reload
				once
				always
				never
			[--keep-meta-shutdown]
			#keep request.META['werkzeug.server.shutdown'] fx which is auto removed because dj debug pages tries to call the fx and unintentionally shuts down the Werkzeug server
			[--nopin]
			#disable the PIN in werkzeug
			#USE IT WISELY!
			[--nostatic]
			#tells dj to not auto serve static files at STATIC_URL
			[--insecure]
			#allow serving static files even if DEBUG is False
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<[addr:]port>]


		
		set_default_site
		#set params of the default django.contrib.sites Site
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--name <site_name>]
			[--domain <site_domain>]
			[--system-fqdn]
			#use systems FQDN as name & domain as name & domain
			#can be combination with --name
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]



		set_fake_emails
		#DEBUG only
		#give ∀ users a new email based on their account data
		#("%(username)s@example.com") by default
		#possible params:
			username
			first_name
			last_name
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--email <default_email>]
			#new email format
			[-a, --no-admin]
			#don't change admin acc
			#либо я что-то не понимаю|названия параметров слегка не логично
				#нихера - ∀ логично -> (минус)a(dmin)
			[-s]
			#don't change staff acc's
			[--include <regexp>]
			#⊃ user ⊃ matching usernames
			[--exclude <regexp>]
			#!⊃ user ⊃ matching usernames
			[--include-groups <comma_separated_groups>]
			#⊃ user ⊂ matching groups
			[--exclude-group <exclude_groups>]
			#!⊃ user ⊂ matching groups
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]


		
		set_fake_passwords
		#DEBUG ONLY
		#sets ∀ user passwords to a common val
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--prompt]
			#prompts for the new password
			[--password <default_password>] = "password"
			#use this as default password
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		shell_plus
		#~ manage.py shell, but autoloads the models of ∀ instaled dj apps
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--plain]
			#use plain python
			[--idle]
			#use idle
			[--bpython]
			#use bpython
			[--ptpython]
			#use ptpython
			[--ptipython]
			#use ptipython
			[--ipython]
			#use ipython|jupyter
			#в чем отличие от ipython notebook?
			[--notebook]
			#use ipython notebook
			#∃ отличие от --ipython?
			[--kernel]
			#start IPython kernel
			[--connection-file <connection_file>]
			#specifies the connection file to use if uring the --kernel opt
			[--no-startup]
			#if using plain Python -> ignore PYTHONSTARTUP env v & ~/.pythonrc.py
			[--use-pythonrc]
			#(?)=--no-startup
			[--print-sql]
			#print SQL queries as they're exe
			#что-то не сработало
			[--print-sql-location]
			#show location in code wher SQL query generated from
			#что-то не сработало
			[--dont-load DONT_LOAD]
			#ignore autoloading of some apps/models
			#мб исп неск раз
			[--quiet-load]
			#dont display loaded models messages
			[--vi]
			#load vi key bindings for --ptpython & --ptipython
			[--no-browser]
			#don't open notebook in browser after startup
			[-c|--command <command>]
			#instead of opening an interactive shell, run a command & exit
			
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		show_templatetags
		#deprecated in favour of "show_template_tags"
		#displays template tags & filters availabel in the current project
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]



		show_urls
		#displays ∀ of the url matching routes for the project
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-u|--unsorted]
			#show urls unsorted but same order as found in url patterns
			[-l|--language <language>]
			#(?)only show this language code
			#(?)useful for i18n_patterns
			#видимо что-то с unicode urls
			[-d|--decorator <decorator>]
			#(?)show the presence of given decorator on views
			[-f|--format <format_style>]
			#output style
			#choices:
				dict_keys([
					'dense',
					'table',
					'aligned',
					'verbose',
					'json',
					'pretty-json'
				])
			[--urlconf <urlconf>]
			#set the settings URL conf v to use
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]






		sqlcreate
		#(?)generates the SQL to create your db for you, as specified in settings.py
			py manage.py sqlcreate >> -- manage.py syncdb will automatically create a sqlite3 db file
				py manage.py syncdb >> Unknown command: 'syncdb'. Did you mean syncdata?
		#the envisioned use case is something like this
			./manage.py sqlcreate [--router=<routername>] | mysql -u <db_administrator> -p ./manage.py sqlcreate [--router=<routername>] | psql -U <db_administrator> -W
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-R|--router <router>]
			#router-db than ⊂ settings.py
			[-D|--drop]
			#includes commands to drop ∀ ∃ user & db
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		sqldiff
		#prints the (approximated) diff befween models & fields in the db for the given apps
		#(?)indicates how columns ⊂ db are different from the sql that would be generated by dj
		#(?)is NOT a db migration tool (Th[ugh it can certainly help])
		#(?) purpose is to show the curr diff as a way to check/debug ur models compared to the real db tables/columns
		#примеры
			py manage.py sqldiff app
				BEGIN;
				-- Application: <app>
				-- Model: <model>
				-- Table missing: <app>_<model>
				COMMIT;
			py manage.py sqldiff otherapp
				--no differences
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-a|--all-applications]
			#auto include ∀ app ⊂ INSTALLED_APPS
			[-e|--not-only-existing]
			#check ∀ tables that ∃ in db, not only tables that should ∃ based on models
			[-d|--dense-output]
			#(?)output in dense format
			#normally output is spreaded over multiple lines
			[-t|--output_text]
			#outputs the diffs as descriptive text instead of SQL
			[--include-proxy-models]
			#(?) include proxy models in the graph
			[--include-defaults]
			#include default vals in SQL output
			#beta feature(2.2.13)
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<app_label0> [<app_label1> ...]



		sqldsn
		#prints DSN on stdout, as specified in settings.py
			./manage.py sqldsn [--router=<routername>] [--style=pgpass]
		#exaples
			py manage.py sqldsn
			>>
				DSN for router 'default' with engine 'sqlite3':
					<path_to_db_file>
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-R|--router <router>]
			#specified router
			[-s|--style <style>]
			#DSN format style
				keyvalue
				uri
				pgpass
				all
			[-a|--all]
			#show DSN for ∀ db routes
			[-q|--quiet]
			#only show DSN
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]


		
		sync_s3
		#(?)syncs the complete MEDIA_ROOT structure & files to S3 into the given bucket name
			py manage.py sync_s3
			>>
				CommandError: Please instll the 'boto' Python library
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[-p|--prefix <prefix>]
			#prefix to pretend to the path on S3
			[-d|--dir <dir>]
			#custom static root dir to use
			[--s3host <s3host>]
			#enables connecting to other providers/regions
			[--acl <acl>]
            #enables to override default acl(public-read)
			[--gzip]
            #enables gzipping CSS & JS files
			[--renamegzip]
            #enables renaiming of gzipped assets to have '.gz' appended to the filename
			[--expires]
            #enables setting a far future expires header
			[--force]
            #skip the file mtime check to force upload of ∀ files
			[--filter-list <filter_list>]
            #?override default dir & file exclusion filters
			#comma separated lst
			[--invalidate]
			#invalidates the associated obj in CloudFront
			[--media-only]
			#only MEDIA_ROOT files will be uploaded to S3
			[--static-only]
			#only STATIC_ROOT files will be uploaded to S3
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		


		syncdata
		#makes the curr db have the same data as the fixture(s)(!>/!<)
		#у меня ничего не вывело
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--skip-remove]
			#avoid remove ∀ obj from db
			[--database <db_name>]
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[<fixture_labels0> [, <fixture_label1>]]
			#specify the fixture label
			
			
		
		unreferenced_files
		#print a lst of ∀ files ⊂ MEDIA_ROOT that are not referencds in the db
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		update_permissions
		#reloads perm's for specified app|∀ apps if no args are specified
		#требует ∃ бд, у меня ничего не вывело
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--apps <app0> [, <app1> ...]]
			[--create-only]
			#only create missing perm's
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		validate_templates
		#validate templates on syntax & compile err's
		#examples
			py manage.py validate_templates >> 0 errors found
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--no-apps]
			#don't auto include apps
			[-b|--break]
			#break on first err
			[-i|--include <paths_to_template_dirs>]
			#append these paths to TEMPLATE DIRS
			[--ignore-app <ignore_apps>]
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
	[sessions]
		clearsessions
		#can be run as a cronjob|directly to clead out expired sessions
		#у меня ничего не вывело
		#only with the db backend at the moment
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		
	[staticfiles]
		collectstatic
		#collect static in a single location
			py manage.py collectstatic
			>>
				<num> static files copied to '<...>\static'
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help] [--noinput|--no-input]
			[--no-post-process]
			#don't post process collected files
			[-i <glob_pattern>]
			#ignore matching files|dirs
			#can use multiple times
			[-n|--dry-run]
			#do everything except modify fs
			[-c|--clear]
			#?clear ∃ files usind the storage before trying to copy|link the original file
			[-l]
			#create a symbolic link to each file instead of copying
			[--no-defalt-ignore] = ('CVS', '.*' and '*~')
			#don't ignore the common private glob-style patterns
			 [--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		
		
		
		findstatic
		#finds the absolute path for the given static
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--first]
			#only return the first match for each static
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			<staticfile0> [<staticfile1> ...]
		
		
		
		runserver
		#запускает отладочный сервер & also serves static files
		#optional args(вероятно могут стоять в ∀ порядке)
			[-h|--help]
			[--ipv6|-6]
			#использовать IPv6
			#адрес по умолч	::1
			[--nothreading]
			#force one thread
			#по умолчанию режим многопоточный
			[--noreload]
			#отключение автоперезапуска при Δ кода(don't use auto-reloader)
			[--nostatic]
			#dont auto serve static ad STATIC_URL
			[--insecure]
			#allows serving static even if DEBUG=False
			[--version] [-v {0,1,2,3}] [--settings <setting>] [--pythonpath <python_path>] [--traceback] [--no-color] [--force-color]
		#positional arg(вероятно должен стоять в конце)
			[[<adress>][:][<port>]] = 127.0.0.1:8000(TCP)
		#examples
			python manage.py runserver 1.2.3.4
			python manage.py runserver 4000
			

		
		
		
		

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
			#модуль административных настроек и классов редакторов(?)(возм admin.site.registers() создает что-то ~ класса позволяющих редактировать бд?)


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


КОНТРОЛЛЕР
#контроллер - устоявшийся термин для таких программных модулей
#код запускаемый в ответ на поступление клиентского запроса содержащего url в опред формате
#dj не предъявляет к организации кода контроллеров никаких спец требований => можно помещать их в ∀ место ⊃ автоматически создаваемый views.py
#основная часть логики саита
#выполняют ∀ действия по
    выборка из бд
    подготовке данных для вывода
    обработке данных от пользователя
	сохранение в бд
	рендерингу страниц
		
		
		КОНТРОЛЛЕР-FX
		#python fx
		#более универсальны, но трудоемки в разработке
        #view, вьюха, представление(автор считает неудачным)
        #∀ контроллер-fx в качетве единственного обязательного аргумента принимает экземпляр HttpResponse
        #examples
            #вывод страницы ⊃ список объявлении ⊂ выбраннои посетителем рубрике
            #альтернатива - см КОНТРОЛЛЕР-КЛАСС
            from .models import Rubric
            
            def by_rubric(request, rubric_id):
                bbs = Bb.objects.filter(rubric=rubric_id)
                current_rubric = Rubric.objects.get(pk=rubric_id)
                context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
                return render(request, 'bboard/by_rubric.html', context)

        #обязана
            #принимать
                экземпляр HttpRequest
                набор именованных параметров одноименных url-параметрам объявленных в связанном маршруте
            #возвращать
                экземпляр HttpResponse|его производных
                
                НАПИСАНИЕ КОНТРОЛЛЕРОВ FX
                #] нужно вывести страницу ⊃ объявления ⊃ выбраннои user'ом рубрике
                #на практике для таких задач исп многозадачные контроллеры контроллер
                
                    ОДНОЗАДАЧНЫЕ КОНТРОЛЛЕРЫ
                        #if требуется вывод страницы создания объявления & его сохранение в бд -> требуется два контроллера
                        app/views.py
                            #создание формы & вывод страницы создания объявления
                            def add(request):
                                bbf = BbForm()
                                context = {'form': bbf}
                                return render(request, 'bboard/create.html', context)
                            #сохранение объявления
                            def add_save(request):
                                bbf = BbForm(request.POST)
                                if bbf.is_valid():
                                    bbf.save()
                                    return HttpResponseRedirect(reverse('by_rubric',
                                           kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
                                else:
                                    context = {'form': bbf}
                                    return render(request, 'bboard/create.html', context)
                        #объявим маршруты на контроллеры
		                app/urls.py
		                    from .views import add, add_save
		                    ...
		                    urlpatterns = [
		                        path('add/save/', add_save, name='add'),
		                        path('add/', add, name='add'),
		                        ...
		                    ]
		                #исправим <form> ⊂ bboard/create.html создающий форму добавив целевои uri
		                bboard/create.html
		                    <form action="{% url 'add_save' %}" method="post">
		            
		            
		            МНОГОЗАДАЧНЫЕ КОНТРОЛЛЕРЫ
		            #чаще исп на практике
		                bboard/views.py
		                    ...
		                    def add_and_save(request):
		                        #if post -> нужно принять данные
		                        if request.method == 'POST':
		                            bbf = BbForm(requst.POST)
		                            #валидация
		                            if bbf.is_valid():
		                                bbf.save()
		                                
		                                return HttpResponseRedirect(reverse('bboard:by_rubric',
		                                       kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
		                            #иначе -> повторныи вывод страницы с формои ~? оставить содержимое поля? (проверить)
                                    else:
                                        context = {'form': bbf}
                                        return render(request, 'bboard/create.html', context)
                                #иначе -> вывод страницы с пустои формои
                                else:
                                    bbf = BbForm()
                                    context = ('form': bbf)
                                    return render(request, 'bboard/create.html', context)
                        #одна view -> один маршрут
                        bboard/urls.py
                            from .views import add_and_save
                            ...
                            urlpatterns = [
                                path('add/', add_and_save, anme='add'),
                                ...
                            ]
                        #в шаблоне больше не нужно указывать uri по которому отправятся данные - будет исп тот-же uri с которого была загружена текущая страница
                        bboard/create.html
                            ...
                            <form method="post">





		КОНТРОЛЛЕР-КЛАСС
		#позволяют выполнить типовые задачи(вроде вывода списка каких-либо позиций) минимумом кода(следуя ⊂ им соглашениям)
        #в path() ⊂ urls.urlpatterns в случае контроллера-класса передается ссылка на результат возвращаемый .as_view() ⊃ контроллеру класса вместо самого контроллера-класса
        #более высокоуровневый чем контроллер-fx -> сам exe ряд типичных действий
            
            .as_view(<параметры_контроллера_класса>)
            #поддержевается ∀ контроллерами-классами
            #examples
                ...
                path('add/', CreateView.as_view())
                ...
                #указание модели(model) & пути к шаблону(template_name
                path('add/', CreateView.as_view(model=Bb, template_name='bboard/create.html'))
            
            
            БАЗОВЫЕ КОНТРОЛЛЕРЫ-КЛАССЫ
            #самые простые & низкоуровневые
                
                django.views.generic.base
                #⊃ ∀ базовые контроллеры-классы
                
                    .View
                    #диспетчеризация по HTTP-методу
                    #max простой
                    #определяет HTTP-метод посредством которого был exe запрос & exe код соотв этому методу
                    #attrs
                        
                        .http_method_names=['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
                        #⊃ список имен допустимых методов
                        #by def ⊃ ∀ методы поддерживаемые HTTP
                        
                        .request
                        #⊃ запрос
                        #экз Request
                        
                        
                        .kwargs
                        #dict ⊃ полученные из uri параметры
                        
                        .as_view()
                        #см .as_view()
                        
                        
                        .dispatch(<запрос> [, <val_url_parameters>])
                        #должен(напр при реализации пользовательских классов) exe обработку полученного запроса & val url-параметров извлеченных из uri
                            <запрос>
                            #экземпляр HttpRequest
                            
                            <val_url_parameters>
                            #передаются через именованные параметры метода ~ контроллерам-fx
                        #должен(напр при реализации пользовательских классов) возвращать ответ представленный экз HttpResponse | его подклассом
                        #в изначальнои реализации
                            извлекает обозначение HTTP-метода
                            вызывает метод класса с именем = извлеченному обозначению
                            передает этому методу <запрос> & <val_url_parameters>
                            >> результат возвращенный методом
                            #if запрос получен с исп GET -> вызывает .get(), if с исп POST -> вызывает .post()
                            #if !∃ метода класса одноименного с HTTP-методом с исп которого был получен запрос(кроме HEAD) -> ничего не делает
                                #при отсутствии .head() вызывается .get()
                        
                        
                        .http_method_not_allowed(<request> [,<val_url_parameters>])
                        #вызывается if запрос был exe с исп неподдерживаемого HTTP-метода
                        #в изначальной реализации
                            >> ответ типа HttpResponseNotAllowed ⊃ список допустимых методов
                        
                        
                        .options(<request> [, <val_url_parameters>])
                        #должен(напр при реализации пользовательских классов) обрабатывать запрос с исп HTTP-метода OPTIONS
                        #в изначальнои реализации
                            >> ответ ⊃ заголовок Allow ⊃ ∀ поддерживаемые HTTP-методы
                    #краине редко исп как есть - обычно исп производные от него классы(как примесь?)
                    
                    
                    .ContextMixin()
                    #примесь
                    #создание контекста шаблона
                    #добавляет контроллеру-классу средства формирования контекста шаблона(attrs):
                        .extra_context:<dict>
                        #задает содержимое контекста шаблона
                        #создается при первом обращении к контроллеру классу, и в дальнейшем остается const(⊃ собственные копии, а не ссылки на сами элты
                            #if один из элтов - набор записеи -> он также !Δ даже if в исходный добавляются записи
                            -> добавлять в контекст шаблона элты ⊃ наборы записеи следует только через .get_context_data()
                        
                        .get_context_data([<элты_контекста_шаблона>])
                        #должен(напр при реализации пользовательских классов) создавать & возвращать контекст данных
                        #в изначальнои реализации
                            создает пустои контекст
                            добавляет в него
                                элт view ⊃ ссылку на текущии экз контроллера класса(?self)
                                элты контекста шаблона полученные через именованные параметры
                                элты .extra_context
                            #-> при исп вместо .extra_context для добавления контекста, будет получать актуальный набор данных, даже if контекст ⊃ набор с изменившимися с последнего вызова записями
                    
                    
                    .TemplateResponseMixin() -> <TemplateResponse>
                    #примесь
                    #добавляет наследнику средства рендеринга шаблонов
                    #attrs
                        .template_name:<str>
                        #template path
                        
                        
                        .get_template_names()
                        #должен(напр при реализации пользовательских классов) >> список путеи к шаблонам заданных в виде строк
                        #в изначальнои реализации >> список ⊃ один элт ⊂ .template_name
                        
                        
                        .content_type
                        #задает MIME-type ответа и его кодировку
                            .content_type=None
                            #исп default MIME-type & encoding (видимо заданные в settings)
                        
                        
                        .render_to_response(<template_context>) -> <TemplateResponse>
                        #рендерит шаблон
                        #нужно вызывать явно
                    
                    
                    
                    .TemplateView
                    #наследник View, ContextMixin & TemplateResponseMixin
                    #при получинии GET-запроса -> рендерит шаблон исп контекст ⊃ ∀ url-параметры ⊂ маршруту и отправляет ответ
                    #может исп в практическои работе
                        #вывод главной страницы ⊃ объявления
                        from django.views.generic.base import TemplateView
                        from .models import Bb, Rubric
                        ...
                        class BbIndexView(TemplateView):
                            template_name = 'bboard/index.html'
                            ...
                            #переопределяем формирование контекста
                            def get_context_data(self, *args, **kwargs):
                                context = super().get_context_data(*args, **kwargs):
                                context['bbs'] = Bb.objects.all()
                                context['rubrics'] = Rubric.objects.all()
                                return context
                    
                    
                    
                    КЛАССЫ ПЕРЕНАПРАВЛЕНИЯ
                        RedirectView
                        #перенаправляет на указанныи uri
                            url:<str>
                            #задает url перенаправления
                            #может ⊃ спецификаторы поддерживаемые оператором форматирования python %(https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting) в которых следует указывать имена url-params, вместо которых будут подставленны их val
                            
                            pattern_name
                            #задает имя именованного route
                            #обратное разрешение url будет exe с url-params полученными контроллером
                            
                            query_string:<bool>=False
                                True
                                #добавление ∀ GET-params ⊂ текущему uri к uri перенаправления
                                False
                                #GET-params не передаются
                            
                            get_redirect_url(<vals_url_params>) -> <str>
                            #должен >> uri перенаправления
                            #в исходный реализации
                                извлекает val .url
                                форматирует его передавая полученные params в %
                                if url=None -> производит обратное разрешение на основе val .pattern_name & url-params Else If неудачно отправляет ответ ⊃ код 410(запрошенная str !∃)
                            
                            permanent:<bool>=False
                                True
                                #будет exe постоянное перенаправление(status 301)
                                False
                                #будет exe временное перенаправление(status 302)
                        #examples
                            #организуем redirect с uri вида
                                /detail/<year>/<month>/<day>/<key>/
                                #на
                                /detail/<key>/
                            .../urls.py
                                ...
                                path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
                                path('detail/<int:year>/<int:month>/<int:day>/<int:pk>', BbRedirectView.as_view(), name='old_detail'),
                                ...
                            .../views.py
                                ...
                                class BbRedirectView(RedirectView):
                                    #для формирования целевого uri исп .url & str ⊃ спецификатор обрабатываемыи оператором %
                                    #вместо спецификатора в str будет подставлено val url-param pk(ключ записи)
                                    url = '/detail/%(pk)d/'
                        #наследник
                            View
                        
        
                    
                    
                                    
            КЛАССЫ ВЫВОДЯЩИЕ СВЕДЕНИЯ О ВЫБРАННОЙ ЗАПИСИ
            #обобщенные классы
            #exe типовые задачи и мб исп в разных ситуациях
            #пример просмотр сведений о товаре
            
                django.views.generic.detail
                #⊃ более высокоуровневые классы чем базовые контроллеры
                
                    SingleObjectMixin
                    #примесь
                    #наследник ContextMixin
                    #получает val ключа|слага модели из url-params & извлекает по нему запись модели & помещает ее в контекст шаблона
                    #attrs
                        .model
                        #задает модель для извлечения записи
                        
                        .queryset
                        #указывает диспетчер записеи|<QuerySet>(набор записей) в которых ищутся записи
                        
                        .get_queryset()
                        #должен(напр при реализации пользовательских классов) >> <QuerySet> в котором ищутся записи
                        #в исходной реализации >> val attr queryset if оно не задано, | набор записей извлеченных из модели извлеченной из attr model
                        
                        .pk_url_kwarg="pk"
                        #задает имя url-параметра, через который контроллер получит val ключа записи
                        
                        .slug_field="slug"
                        #задает имя поля модели ⊃ слаг
                        
                        .get_slug_field()
                        #должен(напр при реализации пользовательских классов) >> str ⊃ имя поля модели ⊃ слаг
                        #в исходнои реализации >> val ⊂ slug_field
                        
                        .slug_url_kwarg="slug"
                        #задает имя url-param через который контроллер-класс получит val слага
                        
                        .query_pk_ang_slug=False
                        #
                            query_pk_ang_slug=False
                            #поиск записи only by key
                            query_pk_ang_slug=False
                            #поиск записи по ключу и слагу
                        
                        
                        .context_object_name
                        #задает имя v контекста шаблона для сохранения наиденнои записи
                        
                        
                        .get_context_object_name(<record>)
                        #должен(напр при реализации пользовательских классов) >> имя v контекста шаблона для сохранения наиденнои записи в виде str
                        #в исходнои реализации >> имя ⊂ context_object_name else if context_object_name=None >> lowercase имя модели
                            #пример
                            #if model=Rubric & context_object_name=None -> v контекста получит имя rubric
                            
                        
                        .get_object([queryset=None]) -> <наиденная_запись>
                        #ищет записи по указанным критериям
                            queryset
                            #набор записей где будет exe поиск
                                queryset=None
                                #поиск в наборе возвращаемом .get_queryset()
                        #val ключа & слага можно получить из dict ⊃ ∀ полученные контроллером url-params и сохраненного в атрибуте экземпляра kwargs, имена нужных параметров можно получить из attrs pk_url_kwarg & slug_url_kwarg
                        #if запись не наидена >> exept Http404 ⊂ django.http
                        
                        
                        .get_context_data([<дополнительные_элты_контекста_шаблона>])
                        #переопределенный метод, создающий и возвращающии контекст данных
                        #в исходнои реализации требует чтобы в экз текущего контроллера-класса ∃ attr object ⊃ наиденную запись|None (if она не была наидена|контроллер используется для создания новой записи). В контексте шаблона создаются v object и v с именем возвращаемым .get_context_object_name(), которые ⊃ наиденную запись
                    
                    
                    SingleObjectTemplateResponseMixin
                    #примесь
                    #рендерит шаблон на основе наиденнои в модели записи
                    #наследник TemplateResponseMixin
                    #требует ∃ в контроллере-классе attr object ⊃ наиденная запись(в виде model obj)|None(if запись не была наидена|контроллер исп для создания новой записи)
                    #attrs
                        .template_name_field=None
                        #⊃ имя поля модели ⊃ путь к шаблону
                            template_name_field=None
                            #путь к шаблону не будет извлекаться из записи
                        
                        .template_name_suffix="_detail"
                        #⊃ str ⊃ суффикс добавляемыи к автоматом сгенерированному пути к шаблону
                        
                        .get_template_names()
                        #переопределенный метод
                        #>> список путеи к шаблонам в виде str
                    #в исходнои реализации >> список:
                            пути извлеченного из унаследованного attr template_name(if указан)
                        or
                            пути извлеченного из поля модели с именем ⊂ attr template_name_field
                                #if ∀ нужные данные указаны
                                   имя поля
                                   запись модели
                                   путь в поле этои записи
                            пути вида
                                <app_alias>\<model_name><suffix>.html
                                #пример
                                    #для модели bboard будет сформирован путь bboard\bb_detail.html
                    
                    
                    DetailView
                    #примесь
                        автоматом ищет запись по val ключа/слага
                        заносит наиденную запись в attr object
                        #чтобы успешно работали наследуемые им примеси
                        выводит страницу ⊃ сведения о записи
                    #наследует
                        View
                        TemplateResponseMixin
                        SingleObjectMixin
                        SingleObjectTemplateResponseMixin
                    #examples
                        #вывод сведении о выбранном посетителем объявлении
                        .../views.py
                            #путь к шаблону не указан -> класс ищет шаблон со сформированны by def путем bboard\bb_detail.html
                            from django.views.generic.detail import DetailView
                            from .models import Bb, Rubric
                            ...
                            class BbDetailView(DetailView):
                                model = Bb
                                
                                def get_context_data(self, *args, **kwargs):
                                    context = super().get_context_data(*args, **kwargs)
                                    context['rubrics'] = Rubric.object.all()
                                    return context
                        .../urls.py
                            #следуя соглашениям указав для url-param ключа записи имя pk исп классом DetailView by def
                            from .views import BbDetailView
                            urlpatterns = [
                                ...
                                path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
                                ...
                            ]
                        bboard/bb_detail.html
                            #by def класс BbDetailView создает в контексте шаблона v bb ⊃ наиденную запись(этот fx унаследован от DetailView) -> исп эту v
                            {% extends "layout/basic.html" %}
                            
                            {% block title %}{{ bb.title }}{% endblock %}
                            
                            {% block content %}
                            <p>Рубрика: {{ bb.rubric.name }}</p>
                            <h2>{{ bb.title }}</h2>
                            <p>{{ bb.content }}</p>
                            <p>Цена: {{ bb.price }}</p>
                            {% endblock %}
                        #добавим код создающии ссылки на страницы выбранных объяв
                        bboard/index.html
                            ...
                            <h2><a href="{% url 'detail' pk=bb.pk %}">{{ bb.title }}</a></h2>
                            ...
                        bboard/by_rubric.html
                            ...
                            <h2><a href="{% url 'detail' pk=bb.pk %}">{{ bb.title }}</a></h2>
                            ...
                
                
            КЛАССЫ ВЫВОДЯЩИЕ НАБОРЫ ЗАПИСЕИ
                
                django.views.generic.list
                
                    MultipleObjectMixin
                    #извлечение набора записей из модели и помещает результат в контекст шаблона
                    #номер части которую нужно извлечь - int 1+|"last" else >> exept Http404 ⊂ django.http
                        "last"
                        #обозначает последнюю часть
                    #может исп
                        фильтрацию
                        сортировку
                        разбиение на части посредством пагинатора
                    #наследует ContextMixin
                    #attrs
                        .model
                        #задает модель для извлечения записей
                        
                        .queryset
                        #указывает диспетчер записей|исходныи <QuerySet> из которого будут извлечены записи
                        
                        .get_queryset()
                        #должен возвращать <QuerySet> в котором ищутся записи
                        #в исходной реализации >> val attr queryset if оно не задано, | набор записей извлеченных из модели извлеченной из attr model
                        
                        
                        .ordering
                        #задает параметры сортировки записеи
                        #val
                            str ⊃ field_name
                            #сортирока только по этому полю (by def по возрастанию)
                            #для сортировки по убыванию нужно предварять имя поля "-"
                            seq ⊃ str имена полеи
                            #сортировка по нескольким полям
                        #if !∃ exe сортировка заданная в параметрах модели
                            #else if модель ⊅ указания сортировки -> сортировка !exe
                        
                        
                        .get_ordering()
                        #должен >> параметры сортировки записеи
                        #в исходной реализации >> val attr .ordering
                        
                        
                        .paginate_by
                        #задает int кол-во записеи в однои части пагинатора
                        #if !∃|=None => набор записеи не разбивается на части
                        
                        
                        .get_paginate_by(<набор_записей>)
                        #должен >> кол-во записеи полученного набора, помещающихся в однои части пагинатора
                        #в исходной реализации >> val attr paginate_by
                        
                        
                        
                        .page_kwarg:<str>="page"
                        #указывает имя URL|GET-параметра через который будет передаваться номер выводимои части пагинатора
                        
                        
                        
                        .paginate_orphans=0
                        #задает int min число записеи которые могут ⊂ последнеи части пагинатора
                        #if последняя часть пагинатора ⊃ меньше записеи -> оставшиеся записи будут выведены в предыдущеи части
                            .paginate_orphans=0
                            #последняя часть может ⊃ ∀ число записеи
                            
                            
                            
                        .get_paginate_orphans()
                        #должен >> min число записеи помещающихся в последнеи части пагинатора
                        #в исходнои реализации >> val attr paginate_orphans
                        
                        
                        .allow_empty=True
                        #
                            allow_empty=True
                            #разрешает извлечение пустои(⊅ ни однои записи) части пагинатора
                            allow_empty=False
                            #>> exept Http404 при попытке извлечения пустои части пагинатора
                        
                        
                        .get_allow_empty()
                        #должен >> True if разрешено извлечение "пустои" части пагинатора|>>False if запрещено
                        #в исходнои реализации >> val .allow_empty
                        
                        
                        .paginator_class
                        #указывает класс используемого пагинатора
                        #by def указывает Paginator ⊃ django.core.paginator
                        
                        
                        .get_paginator(<набор_записей>, <число_записеи_в_части> [, orphans=0][, allow_empty_first_page=True])
                        #должен создавать и возвращать obj пагинатора
                            <набор_записей>
                            #набор записеи для разбивки на части
                            orphans
                            #min число записеи в последнеи части пагинатора
                            allow_empty_first_page:<bool>
                            #разрешение извлечения "пустои" части
                        #в исходнои реализации создает экз пагинатора указанного в .paginator_class передавая его конструктору ∀ полученные параметры
                        
                        
                        .paginate_queryset(<набор_записей>, <число_записеи_в_части>)
                        #должен разбивать <набор_записей> на части размером <число_записеи_в_части> и >> кортеж ⊂ 4 элта:
                            obj самого пагинатора
                            obj его текущеи части, с номером полученным с URL|GET параметром
                            набор записеи из текущеи части
                            True if извлеченныи набор записеи был разбит на части с исп пагинатора Else False
                            #имеется в виду успешность операции?
                            
                        
                        .context_object_name
                        #задает имя v контекста шаблона для хранения извлеченного набора записеи
                        
                        
                        
                        .get_context_object_name(<набор_записей>) >> str
                        #должен >> имя v контекста шаблона для хранения извлеченного набора записей
                        #в исходнои реализации >> имя ⊂ context_object_name If оно указано Else lowercase имя модели полученное из <набора_записеи> + суффикс _list
                        
                        
                        .get_context_data([object_list=None][,<доп_элты_контекста_шаблона>])
                        #переопределенныи метод
                        #создает & >> контекст данных
                            object_list
                            #набор записей
                            #if !∃ -> исп набор ⊂ .object_list
                        #в исходнои реализации >> контекст ⊃ 5 v:
                            object_list
                            #набор ∀ записей|only набор ⊂ текущеи части пагинатора
                            v возвращаемое .get_context_object_name()
                            #~object_list
                            is_paginated
                            #True If применялся пагинатор Else False
                            paginator
                            #obj пагинатора If применялся пагинатор Else None
                            page_obj
                            #obj текущеи страницы пагинатора If применялся пагинатор Else None
                    
                    
                    
                    MultipleObjectTemplateResponseMixin
                    #примесь
                    #наследник TemplateResponseMixin
                    #рендерит шаблон на отнове извлеченного из модели набора записеи
                    #требует ∃ в контроллере-классе .object_list ⊃ набор записеи
                    #attrs
                        .template_name_suffix:<str>="_list"
                        #суффикс добавляемыи к авто сгенерированному пути к шаблону
                        
                        
                        .get_template_names()
                        #переопределенныи метод
                        #>> список str ⊂ пути к шаблонам
                        #в исходнои реализации >> список ⊃:
                            путь полученныи из унаследованного .template_name(if путь указан)
                            путь <app_alias>\<model_name><suffix>.html
                            #пример: для модели Bb ⊂ bboard app сформирует "bboard\bb_list.html"
                    
                    
                    
                    ListView
                    #наследник
                        View
                        TemplateResponseMixin
                        MultipleObjectMixin
                        MultipleObjectTemplateResponseMixin
                    #автоматом
                        извлекает набор записеи из модели
                        записывает его в .object_list
                        #для успешнои работы наследуемых примесеи
                        выводит страницу ⊃ список записеи
                    #examples
                        #вывод страницы ⊃ список объявлении ⊂ выбраннои посетителем рубрике
                        from django.views.generic.list import ListView
                        from .models import Bb, Rubric
                        ...
                        class BbByRubricView(ListView):
                            template_name = 'bboard/by_rubric.html'
                            context_object_name = 'bbs'
                            
                            def get_queryset(self):
                                return Bb.object.filter(rubric=self.kwargs['rubric_id'])
                            
                            def get_context_data(self, *args, **kwargs):
                                context = super().get_context_data(*args, **kwargs)
                                context['rubrics'] = Rubric.objects.all()
                                context['current_rubric'] = Rubric.objects.get(
                                    #получаем val url-param 'rubric_id', обратившись к словарю ⊂ attr .kwargs экземпляра
                                    #.kwargs ⊃ ∀ url-params указанные в маршруте
                                    pk=self.kwargs['rubric_id'])
                                return context
                        #больше кода чем у написанного ранее контроллера-fx by_rubric()(см контроллеры-fx) тк:
                            в контекст шаблона нужно добавить список рубрик & текущую рубрику; для их добавления в контекст шаблона нужно переопределить get_context_data()
                            
                            исп ∃ шаблон -> нужно указать:
                                его имя
                                имя v контекста для хранения списка объяв



            КЛАССЫ РАБОТАЮЩИЕ С ФОРМАМИ
            #обобщенные классы для работы
                формами связанными с моделями
                обычными формами

                django.views.generic.edit
                #⊃ ∀ классы для работы с формами
                
                    КЛАССЫ ДЛЯ ВЫВОДА И ВАЛИДАЦИИ ФОРМ
                    #lowlevel классы, могут лишь:
                        вывести форму
                        валиднуть данные
                        if данные не валидны -> повторно вывести их с warn msg
                    #-> не всегда удобны
                        #не предусматривают длительного хранения obj формы ->
                            нельзя извлечь ⊃ данные в ∀ момент
                            перенос данньх из формы в модель придется exe самостоятельно
                            #альтернатива: см КЛАССЫ ДЛЯ РАБОТЫ С ЗАПИСЯМИ
                        FormMixin
                        #производная примесь от ContextMixin, может:
                            создать форму
                            #∀(связанную с моделью|обычную
                            валиднуть данные
                            exe перенаправление If данные валидны Else инициировать повторныи вывод формы
                        #attrs
                            .form_class
                            #⊃ link to класс формы используемой наследуемым контроллером
                            
                            .get_form_class()
                            #должен >> link to класс используемой формы
                            #в исходнои реализации >> val .form_class
                            
                            .initial={}
                            #⊃ dict ⊃ исходные данные для занесения в только что созданную форму вида {field:val,...}
                            
                            .get_initial()
                            #должен >> dict ⊃ исходные данные для занесения в только что созданную форму
                            #в исходнои реализации >> val .initial
                            
                            .success_url
                            #⊃ url для перенаправления if данные формы валидны
                            
                            
                            .get_success_url()
                            #должен >> url для перенаправления if данные формы валидны
                            #в исходнои реализации >> val .success_url
                            
                            
                            .prefix=None
                            #задает str префикс имени формы, которыи будет ∃ в создающем форму HTML-коде
                            #стоит исп only if планируется поместить несколько однотипных форм в одном теге <form>
                                prefix=None
                                #без префикса                        
                            
                            
                            .get_prefix()
                            #должен >> префикс для имени формы
                            #в исходнои реализации >> val .prefix
                            
                            
                            .get_form([form_class=None])
                            #>> obj используемои контроллером формы
                            #в исходнои реализации >> экз класса формы указанный в .form_class If .form_class указан Else экземпляр класса возвращаемыи .get_form_class(); при этом конструктору класса формы передаются параметры возвращаемые .get_form_kwargs()
                            
                            
                            .get_form_kwargs()
                            #должен создавать и >> dict ⊃ params для передачи конструктору класса формы при создании его экземпляра в .get_form()
                            #в исходнои реализации создает dict ⊃:
                                initial:<dict>
                                #⊃ исходные данные возвращаемые .get_initial()
                                prefix
                                #префикс для имени формы возвращаемыи .get_prefix()
                                data:<dict>
                                #⊃ данные занесенными в форму посетителем
                                #создаeтся only if для отправки запроса применялись POST/PUT
                                files
                                #⊃ фаилы отправленные посетителем через форму
                                #создаeтся only if для отправки запроса применялись POST/PUT
                        
                        
                            .get_context_data([<доп_элты_контекста_шаблона>])        
                            #переопределенныи метод
                            #создает & >> контекст данных
                            #в исходнои реализации добавляет в контекст шаблона v form ⊃ созданную форму
                            
                            
                            .form_valid(<форма>)
                            #должен exe обработку данных if данные валидны
                            #противоположен .form_invalid()
                            #в исходнои реализации exe перенаправление на url возвращаемыи .get_success_url()
                            
                            
                            .form_invalid(<форма>)
                            #противоположен .form_valid()
                            #в исходнои реализации повторно выводит форму на экран
                        
                        
                        ProcessFormView
                        #производныи View
                            выводит форму
                            принимает введенные данные
                            валидирует данные
                        #переопределяет три метода View
                            .get(<запрос> [, <val_url_params>])
                            #вывод формы
                            .post(<запрос> [, <val_url_params>])
                            #получает & валидирует введенные данные
                            #вызывает .form_valid() if данные валидны Else .form_invalid()
                            .put(<запрос> [, <val_url_params>])
                            #~ post()
                        
                        
                        FormView
                        #производныи
                            View
                            FormMixin
                            ProcessFormView
                            TemplateResponseMixin
                        #предоставляет ∀ инструменты обработки форм
                            создает форму
                            валидирует занесенные в форму данные
                            выводит страницу формы повторно if данные не валидны
                        #остается только реализовать обработку корректных данных переовределив .form_valid()
                            #examples
                                #добавление объявления
                                from django.views.generic.edit import FormView
                                from django.urls import reverse
                                from .models import Bb, Rubric
                                #для формирования url перенаправления нужно получить val ключа рубрики ⊃ объяву -> переопределяем .get_form() где сохраняем созданную форму в .object
                                #затем в .get_success_url() получаем доступ к форме и занесенным в нее данным
                                class BbAddView(FormView):
                                    template_name = 'bboard/crete.html'
                                    form_class = BbForm
                                    initial = {'prics': 0.0}
                                    
                                    def get_context_data(self, *args, **kwargs):
                                        context = super().get_context_data(*args, **kwargs)
                                        context['rubrics'] = Rubric.objects.all()
                                        return context
                                    #сохранение данных
                                    def form_valid(self, form):
                                        form.save()
                                        return super().form_valid(form)
                                    
                                    def get_form(self, form_class=None):
                                        self.object = super().get_form(form_class)
                                        return self.object
                                    
                                    def get_success_url(self):
                                        return reverse('bboard:by_rubric', kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk})
                    
                    
                    
            КЛАССЫ ДЛЯ РАБОТЫ С ЗАПИСЯМИ
            #в отличие от не всегда удобных КЛАССОВ ДЛЯ ВЫВОДА И ВАЛИДАЦИИ ФОРМ которые не всегда удобны тк:
                не предусматривают длительного хранения obj формы ->
                    нельзя извлечь ⊃ данные в ∀ момент
                    перенос данньх из формы в модель придется exe самостоятельно
                #сами
                    сохраняют|исправляют|удаляют запись
                
                        ModelFormMixin
                        #примесь создания формы связанной с моделью
                        #наследует
                            SingleObjectMixin
                            FormMixin
                        #~FormMixin, но предназначен для работы с формами связанными с моделями
                            .model
                            #задает link to класс модели на чьеи основе будет создана форма
                            #требует .fields -> else exept
                            #model & field конфликтуют с указанием непосредственно класса формы в .form_class унаследованным от FormMixin
                            
                            .fields
                            #указывает ₓ имен полеи модели на чьеи основе будет создана форма
                            #?требует .model
                            #model & field конфликтуют с указанием непосредственно класса формы в .form_class унаследованным от FormMixin
                            
                            .get_form_class()
                            #переопределенныи метод
                            #должен >> link to class используемой формы
                            #в исходнои реализации >> val .form_class If (он ∃ в классе) Else >> link to class формы автоматом созданныи на основе модели ⊂ ( .model|унаследованным .queryset)
                                #для создания класса формы исп список полеи ⊂ .fields
                            
                            
                            .success_url
                            #⊃ url для перенаправления в случае валидности данных
                            #Δ от FormMixin.success_url - поддерживает указание непосредственно в str ⊃ url, спец charₓ вида
                                {<имя_поля_таблицы_бд_обрабатываемои_моделью>}
                                #вместо такой ₓ класс подставит val этого поля
                                #поле бд, а не модели(напр для получения ключа и внешнего ключа нужно исп поля id & rubric_id, а не pk & rubric
                            #examples
                                #
                                class BbCreateView(CreateView):
                                    ...
                                    success_url = '/bboard/detail/{id}'
                                
                                
                            .get_success_url()
                            #переопределенныи метод
                            #>> url для перенавравления if данные валидны
                            #в исходнои реализации >> val .success_url в котором последовательности вида {<имя_поля_таблицы_бд_обрабатываемои_моделью>} заменены val соотв полеи If .success_url ∃ Else пытается получить url возвращаемыи <model>.get_absolute_url()
                            
                            
                            .get_form_kwargs()
                            #переопределенныи метод
                            #создает & >> dict ⊃ params для передачи конструктору класса формы при создании его экземпляра в .get_form()
                            #в исходнои реализации добавляет в dict(сформированныи унаследованным методом) элемент instance ⊂ обрабатываемую формои запись модели (if форма ∃ - те исп не для добавления записи) которая извлекается из .object
                            
                            
                            .form_valid(<form>)  
                            #переопределенныи метод
                            #должен обработать данные формы if данные валидны
                            #в исходнои реализации 
                               сохраняет ⊂ формы в модели, тем самым создавая|исправляя запись
                               присваивает новую запись .object
                               вывывает унаследованныи .form_valid()
                            
                     
                
                    .CreateView
                    #создание новои записи
                    #наследник
                        View
                        ModelFormMixin
                        ProcessFormView
                        SingleObjectMixin
                        SingleObjectTemplateResponseMixin
                        TemplateResponseMixin
                    #⊃ ∀ небходимую fx для:
                        создания формы
                        валидации формы
                        вывода формы с исп указанного шаблона
                        создания записи на основе данных из формы
                        перенаправления в случае успеха
                    #args
                        .template_name
                        #путь к шаблону используемому для вывода страницы с формой
                        
                        
                        .template_name_suffix:<str>="_form"
                        #⊃ suffix добавлямыи к авто-сгенерированному пути к шаблону
                        
                        .object
                        #⊃ созданная в модели запись(if запись ∃) Else None
                        
                        .form_class
                        #класс формы связанной с моделью
                        
                        .success_url
                        #url по кот. будет выполнен переход после успешного сохранения данных
                        
                        .get_context_data()
                        #формурует контекст шаблона
                    #examples
                        from django.views.generic.edit import CreateView
                        from .forms import BbForm
                        ...
                        class BbCreateView(CreateView):
                            template_name = 'bboard/create.html'
                            form_class = BbForm
                            success_url = '/bboard/'
                            ...
                            def get_context_data(self, **kwargs):
                                context = super().get_context_data(**kwargs)
                                context['rubrics'] = Rubric.objects.all()
                                return context
                    
                    
                    
                    .UpdateView
                    #исправление записи
                        автоматом ищет запись в модели по полученному из url-параметра ключу|слагу
                        выводит страницу ⊃ форму для ее Δ
                        проверит и сохранит Δ данные
                    #наследник
                        View
                        ModelFormMixin
                        ProcessFormView
                        SingleObjectTemplateResponseMixin
                        TemplateResponseMixin
                    #attrs
                        .template_name_suffix:<str>="_form"
                        #⊃ suffix добавлямыи к авто-сгенерированному пути к шаблону
                        
                        .object
                        #⊃ Δ запись модели
                        
                        остальные
                        #унаследованы
                    #examples
                        #шаблон bboard\bb_form.html ~ bboard\create.html 
                        from django.views.generic.edit import UpdateView
                        from .models import Bb, Rubric
                        ...
                        class BbEditView(UpdateView):
                            model = Bb
                            form_class = BbForm
                            success_url = '/'
                            ...
                            def get_context_data(self, *args, **kwargs):
                                context = super().get_context_data(*args, **kwargs)
                                context['rubrics'] = Rubric.object.all()
                                return context
                    
                    
                    .DeletionMixin
                    #удаление записи
                        добавляет наследнику инструменты удаления записеи
                        #предпологает что запись уже наидена и сохранена в .object
                    #примесь
                    #attrs
                        .success_url
                        #~ModelFormMixin.success_url
                        .get_success_url()
                        #~ModelFormMixin.success_url
                    
довольно интересно посмотреть на названия и назначение примесеи .DeletionMixin & .DeleteView
                    
                    .DeleteView
                    #удаление записи с подтверждением
                        автоматом находит запись в модели по полученному и url-param ключу|слагу
                            -> требует указания:
                                модели в .model
                                набор записеи в queryset|переопределить .get_queryset()
                        выведет страницу подтверждения ⊃ форму с кнопками удаления
                        удалит запись(видимо при подтверждении)
                    #наследник
                        View
                        DeletionMixin
                        DetailView
                        SingleObjectMixin
                        SingleObjectTemplateResponseMixin
                        TemplateResponseMixin
                    #attrs
                        .template_name_suffix:<str>="_confirm_delete"
                        #⊃ suffix добавлямыи к авто-сгенерированному пути к шаблону
                        
                        .object
                        #⊃ удаляемую запись модели
                    #examples
                        #удаляет объявы
                        .../views.py
                        from django.views.generic.edit import DeleteView
                        from .models import Bb, Rubric
                        ...
                        class BbDeleteView(DeleteView):
                            model = Bb
                            success_url = '/'
                            
                            def get_context_data(self, *args, **kwargs):
                                context = super().get_context_data(*args, **kwargs)
                                context['rubrics'] = Rubric.objects.all()
                                return context
                        #шаблон страницы подтверждения удаления формы
                            {% extends "layout/basic.html" %}
                            
                            {% block title %}Удаление объявления{% endblock %}
                            
                            {% block content %}
                            <h2>Удаление объявления</h2>
                            <p>Рубрика: {{ bb.rubric.name }}</p>
                            <p>Товар: {{ bb.title }}</p>
                            <p>{{ bb.content }}</p>
                            <p>Цена: {{ bb.price }}</p>
                            <form method="post">
                                {% csrf_token %}
                                <input type="submit" value="Удалить">
                            </form>
                            {% endblock %}
            
            
БУДУЩИЕ ЗАПИСИ
#записи ⊃ поля ⊃ (даты записанные в возвращенное .get_date_field() поле) > текущего


думаю переопределенные методы - в данном случае говорят об отличиях от базовых

             
            КЛАССЫ ВЫВОДА ХРОНОЛОГИЧЕСКИХ СПИСКОВ
            #за определенныи год/месяц/дату/...
                
                django.views.generic.dates
                #⊃ ∀ классы вывода хронологических списков
                    
                    ВЫВОД ПОСЛЕДНИХ ЗАПИСЕИ
                    #хронологического списка max свежих записеи
                    
                        DateMixin
                        #фильтрация записеи по дате
                        #позволяет наследникам фильтровать записи по дате(|дате&времени) ⊂ заданном поле
                        #attrs
                            .date_field:<str>
                            #указывает имя поля модели типа DateField|DateTimeField для фильтрации
                            
                            .get_date_field()
                            #должен >> имя поля модели ⊃ дату для фильтрации
                            #в исходнои реализации >> val .date_field
                            
                            
                            .allow_future:<bool>=False
                            #?включение в результирующии набор записеи "будущие записи"


                            .get_allow_future() -> <bool>
                            #должен >> val указывающее включение/запрет включения в результирующии набор "будущие записи"
                            #в исходнои реализации >> val .allow_future

                        
>> - return|throw exept

                        
                        BaseDateListView
                        #базовыи класс
                        #дает базовую fx для более специализированных классов
                        #examples
                            #может задавать сортировку записеи по убыванию val поля возвращенного .get_date_field() класса DateMixin
                        #наследник
                            DateMixin
                            MultipleObjectMixin
                        #attrs
                            allow_empty:<bool>=False
                            #разрешение извлечения пустои(⊅ записеи) части пагинатора
                                .allow_empty=False
                                #предписывает >> Http404 ⊃ django.http при попытке извлечения пустои части пагинатора
                                
                            .date_list_period:<str>="year"
                            #указывает часть для урезания даты
                            #val
                                "year"
                                "month"
                                "day"
                                #дата не урезается
                            
                            .get_date_list_period()
                            #должен >> обозначение части для урезания даты
                            #в исходнои реализации >> val date_list_period
                            
                            .get_dated_items()
                            #должен >> tuple ⊃ 3 элта:
                                lst ⊃ дат для которых ∃ записи в наборе
                                набор записеи
                                dict ⊃ контекст шаблона
                            #в исходнои реализации >> except NotImplementedError
                            #предназначен для переопределения в подклассах
                            
                            
                            .get_dated_queryset(<условия_фильтрации>)
                            #>> набор отфильтрованных записеи
                                <условия_фильтрации>
                                #думаю задаются ~ другои фильтрации в orm
                                
                            
                            .get_date_list(<набор_записеи> [, dat_type=None][, ordering='ASC'])
                            #>> lst ⊃ vals даты, урезаннои по [части указаннои в param date_type (if date_type ∃) Else val возвращенное get_date_list_period()] для которых ∃ записи в <набор_записеи>
                                ordering:<str>="ASC"
                                #задает направление сортировки
                                    ordering="ASC"
                                    #по возрастанию
                                    ordering="DESC"
                                    #по убыванию
                        #добавляет в контекст шаблона два элта
                            object_list
                            #результирующии набор записеи
                            date_list
                            #список урезанных val дат для которых набор ⊃ записи
                        
                                        
                        ArchiveView
                        #вывод последних записеи(хронологически отсортированных по убыванию val заданного поля)
                        #наследник
                            View
                            DateMixin
                            BaseDateListView
                            TemplateResponseMixin
                            MultipleObjectMixin
                            MultipleObjectTemplateResponseMixin    
                        #создает в контексте шаблона v
                            latest
                            #attr?
                           
                            date_list
                            #⊃ список val дат урезанных до года
                            
                        #к авто-сгенерированному пути шаблона by def добавляется суффикс _archive
                        #examples
                            #вывод разделенных пробелами годов, за которые в наборе ∃ записи
                            .../views.py
                                from django.views.generic.dates import ArchiveView
                                from .models import Bb, Rubric
                                ...
                                class BbIndexView(ArciveIndexView):
                                    model = Bb
                                    date_field = 'published'
                                    template_name = 'bboard/index.html'
                                    context_object_name = 'bbs'
                                    allow_empty = True
                                    
                                    def get_context_data(self, *args, **kwargs):
                                        context = super().get_context_data(*args, **kwargs)
                                        context['rubrics'] = Rubric.objects.all()
                                        return context
                            #используем ⊂ v date_list контекста шаблона lst дат урезанных до года
                                <p>
                                    {% for d in date_list %}
                                    {{ d.year }}
                                    {% endfor %}
                                </p>
                    
                    
                    ВЫВОД ЗАПИСЕИ ПО ГОДАМ
                    #вывод lst записеи относящихся к определенному году
                    
                        YearMixin
                        #примесь
                        #извлечение года для последующеи фильтрации записеи
                        #attr
                            year_format:<str>="%Y"
                            #указывает формат val года поддерживаемыи python strftime() для форматирования после извлечения года из uri 
                                "%Y"
                                #XXXX год
                            
                            get_year_format()
                            #должен >> str ⊃ формат года
                            #в исходнои реализации >> val year_format
                            
                            year:<str>=None
                            #задает val года
                                year=None
                                #год извлекается из uri
                            
                            get_year()
                            #должен >> str ⊃ год
                            #в исходнои реализации пытается >> val .year (If .year ∃) Else url-param year (If url-param year ∃) Else get-param year (If get-param year ∃) Else >> django.http.Http404
                            
                            get_previous_year(<date>)
                            #>> дату = первому дню года перед <date>
                            #в зависимости от val
                                .allow_empty
                                .allow_future
                                #может >> django.http.Http404
                            
                            
                            get_previous_year(<date>)
                            #>> дату = первому дню года после <date>
                            #в зависимости от val
                                .allow_empty
                                .allow_future
                                #может >> django.http.Http404
                        
                        
                        YearArchiveView
                        #вывод хронологического списка записеи за год
                        #наследник
                            View
                            DateMixin
                            YearMixin
                            BaseDateListView
                            TemplateResponseMixin
                            MultipleObjectMixin
                            MultipleObjectTemplateResponseMixin
                        #⊃ 2 доп attr
                            make_object_list:<bool>=False
                            #
                                make_object_list=True
                                #формирует и добавляет в контекст шаблона набор ∀ записеи за год
                                
                                make_object_list=False
                                #добавляет в контекст шаблона "пустои" набор записеи
                            
                            get_make_object_list()
                            #должен >> bool признак формировать ли полноценныи набор записеи относящихся к заданному году
                            #в исходнои реализации >> val .make_object_list
                            #создает в контексте шаблона v
                                date_list
                                #lst дат за которые в наборе ∃ записи урезанные до месяца в порядке возрастания
                                
                                year:<date>
                                #заданныи год
                                
                                previous_year:<date>
                                #предыдущии год
                                
                                
                                next_year:<date>
                                #следующии год
                        #набор записеи за заданныи год будет ⊂ v контекста шаблона ⊂ имя by def object_list
                        #by def к автосгенерированному пути шаблона добавляется суффикс _archive_year
                    
                    
                    ВЫВОД ЗАПИСЕИ ПО МЕСЯЦАМ
                    #классы выводящие lst записеи ⊂ конкретному месяцу конкретного года
                        
                        MonthMixin
                        #примесь
                        #извлечение месяца из [url/get]-param month исп для последующеи фильтрации записеи
                            .month_format:<str>='%b'
                            #указывает формат val извлеченного месяца поддерживаемыи python strftime()
                                '%b'
                                #сокращенное наименование записанное согласно текущим языковым настроикам
                                
                                '%m'
                                #порядковыи номер месяца
                            
                            .get_month_format() -> <str>
                            #должен >> формат месяца
                            #в исходнои реализации >> ⊂ .month_format
                            
                            .month:<str>=None
                            #задает месяц
                                None
                                #месяц извлекается из uri
                            
                            .get_month() -> <str>
                            #должен >> месяц
                            #в исх реализации пытается >> ∃ val .month | url-param month|get-param month| Http404 ⊂ django.http
                            
                            .get_previous_month(<date>)
                            #>> дату ⊃ первыи день месяца перед <date>
                            #в зависимости от val .allow_empty & .allow_future может >> Http404 ⊂ django.http
                            
                            .get_next_month(<date>)
                            #>> дату ⊃ первыи день месяца после <date>
                            #в зависимости от val .allow_empty & .allow_future может >> Http404 ⊂ django.http
                        
                        
                        MonthArchiveView
                        #вывод хронологического lst записеи конкретного месяца & конкретного года
                        #наследник
                            View
                            DateMixin
                            MonthMixin
                            YearMixin
                            BaseDateListView
                            TemplateResponseMixin
                            MultipleObjectMixin
                            MultipleObjectTemplateResponseMixin
                        #создает в контексте шаблона v
                            date_list
                            #lst дат для которых набор ⊂ записи, урезанных до числа, в порядке возрастания
                            
                            month:<date>
                            #представляет заданныи месяц
                            
                            previous_month:<date>
                            #представляет месяц перед заданным
                            
                            next_month:<date>
                            #представляет месяц после заданного
                        #набор записеи за месяц будет ⊂ v контекста шаблона ⊂ имя by def object_list
                        #к авто-сгенерированному пути к шаблону by def добавляется суффикс _archive_month
                        #examples
                            urlpatterns = [
                                #пример uri:/2018/06/
                                path('<int:year>/<int:month>/', BbMonthArchiveView.as_view()),
                            ]
                            ...
                            class BbMonthArchiveView(МonthArchiveView):
                                model = Bb
                                date_field = "published"
                                month_format = '%m'
                    
                    
                    
                    ВЫВОД ЗАПИСЕИ ПО НЕДЕЛЯМ
                    #записи за неделю ⊂ заданныи порядковыи номер
                    
                        WeekMixin
                        #примесь
                        #извлечение номера недели из [url|get]-param week, для фильтрации записеи
                            .week_format:<str>="%U"
                            #указывает формат номера недели поддерживаемыи python strftime() для преобразования после извлечения
                                "%U"
                                #номер недели начинающеися с вс
                                
                                "%W"
                                #номер недели начинающеися с пн
                            
                            .get_week_format() -> <str>
                            #должен >> формат недели
                            #в исходнои реализации >> val ⊂ .week_format
                            
                            .week:<str>=None
                            #задает неделю
                                None
                                #извлечение из uri
                                
                            .get_week() -> <str>
                            #должен >> неделю
                            #в исходнои реализации пытается >> ∃ val .week | url-param week|get-param week|>> exept Http404 ⊂ django.http
                            
                            .get_previous_week(<date>)
                            #>> дату ⊃ первыи день недели перед заданнои даты
                            #в зависимости от vals .allow_empty & .allow_future может >> Http404
                            
                            .get_next_week(<date>)
                            #>> дату ⊃ первыи день недели после заданнои даты
                            #в зависимости от vals .allow_empty & .allow_future может >> Http404
                        
                        
                        
                        WeekArchiveView
                        #вывод хронологического списка записеи указаннои недели & года
                        #наследник
                            View
                            DateMixin
                            WeekMixin
                            YearMixin
                            BaseDateListView
                            TemplateResponseMixin
                            MultipleObjectMixin
                            MultipleObjectTemplateResponseMixin
                        #создает в контексте шаблона v:
                            week:<date>
                            #заданная неделя
                            
                            previous_week:<date>
                            #предыдущая неделя
                            
                            next_week:<date>
                            #следующая неделя
                        #набор записеи за указанную неделю будет ⊂ v контекста шаблона ⊂ имя by def object_list
                        #к авто-сгенерированному пути к шаблону by def добавляется суффикс _archive_week
                        #examples
                            urlpatterns = [
                                #пример uri: /2018/week/24
                                path('<int:year>/week/<int:week>/', WeekArchiveView.as_view(model=Bb, date_field="published"))
                            ]
                        
                    ВЫВОД ЗАПИСЕИ ПО ДНЯМ
                    #вывод списка записеи за определенныи день конкретного года
                    #реализуется 2 классами
                    
                        DayMixin
                        #извлечение заданного числа из [url|get]-param ⊃ имя day, для фильтрации записеи
                            .day_format:<str>="%d"
                            #указывает формат числа поддерживаемыи python strftime() для форматирования после извлечения
                                "%d"
                                #число с начальмым нулем
                            
                            .get_day_format() -> <str>
                            #должен >> формат числа
                            #в исходнои реализации >> val .day_format
                            
                            .day:<str>=None
                            #задает число
                                None
                                #извлекается из uri
                            
                            .get_day() -> <str>
                            #должен >> число
                            #в исходнои реализации пытается >> ∃ val .day|url-param day|get-param day|>> Http404 ⊃ django.http
                        
                        
                        DayArchiveView
                        #вывод хронологического lst записеи за заданныи день конкретного месяца & года
                        #наследник
                            View
                            DateMixin
                            DayMixin
                            MonthMixin
                            YearMixin
                            BaseDateListView
                            TemplateResponseMixin
                            MultipleObjectMixin
                            MultipleObjectTemplateResponseMixin
                        #создает в контексте шаблона v:
                            day:<date>
                            #представляет заданныи день
                            
                            previous_day:<date>
                            #представляет предыдущии день
                            
                            next_day
                            #предыдущии следующии день
                        #набор записеи за заданныи день будет ⊂ v контекста шаблона с именем by def object_list
                        #к авто-сгенерированному пути к шаблону by def добавляется суффикс _archive_day
                        #examples
                            urlpatterns = [
                                #пример uri: /2018/06/24/
                                path('<int:year>/<int:month>/<int:day>/',
                                      DayArchiveView.as_view(model=Bb, date_field="published", month_format='%m')),
                            ]
                        
                        
                        TodayArchiveView
                        #вывод хронологического lst записеи за текущее число
                        #наследник
                            View
                            DateMixin
                            DayMixin
                            MonthMixin
                            YearMixin
                            BaseDateListView
                            DayArchiveView
                            TemplateResponseMixin
                            MultipleObjectMixin
                            MultipleObjectTemplateResponseMixin
                        #создает в контексте шаблона v:
                            day:<date>
                            #представляет текущее число
                            
                            previous_day:<date>
                            #предыдущии день
                            
                            next_day
                            #представляет следующии день
                        #набор записеи за текущее число будет ⊂ v контекста шаблона ⊂ имя by def object_list
                        #к авто-сгенерированному пути к шаблону by def добавляется суффикс _archive_today
                        
                        
                        DateDetailView
                        #вывод однои записи за указанное число
                        #может быть полезен if поле даты по которому ищется запись ⊃ уникальные vals
                        #наследник
                            View
                            DateMixin
                            DayMixin
                            MonthMixin
                            YearMixin
                            DetailView
                            TemplateResponseMixin
                            SingleObjectMixin
                            SingleObjectTemplateResponseMixin
                        #запись за текущее число будет ⊂ v контекста шаблона ⊂ имя by def object
                        #к авто-сгенерированному пути к шаблону by def добавляется суффикс _detail
                        #examples
                            .../views.py
                                from django.views.generic.dates import DateDetailView
                                from .models import Bb, Rubric
                                
                                class BbDetailView(DateDetailView):
                                    model = Bb
                                    date_field = 'published'
                                    month_format = '%m'
                                    
                                    def get_context_data(self, *args, **kwargs):
                                        context = super().get_context_data(*args, **kwargs)
                                        context['rubrics'] = Rubric.object.all()
                                        return context
                            #к сожалению в route на DateDetailView|производные классы требуется указывать url-param ключа(pk)|слага(slug), тк наследник SingleObjectMixin требующего один из них
                                #-> сильно ограничен областью применения(?как)
                            .../urls.py
                                ...
                                    path('detail/<int:year>/<int:month>/<int:day>/<int:pk>', BbDetailView.as_view(), name='detail'),
                        
            СМЕШИВАНИЕ ПРИМЕСЕИ            
                КОНТРОЛЛЕРЫ-КЛАССЫ СМЕШАННОИ FX
                #большая часть fx контроллеров-классов наследуется от примесеи
                #дронов избегает контроллеров смешаннои fx - удобнее создать класс ⊃ ∀ нужную логику
                    ВЫВОД СВЕДЕНИИ О ЗАПИСИ И НАБОРА СВЯЗАННЫХ С НЕИ ЗАПИСЕИ
                        #вывод сведении о записи наследуем от SingleObjectMixin, вывод набора записеи связанных с текущеи наследуем от ListView
                        from django.views.generic.detail import SingleObjectMixin
                        from django.views.generic.list import ListView
                        from .models import Bb, Rubric
                        
                        class BbByRubricView(SingleObjectMixin, ListView):
                            template_name = 'bboard/by_rubric.html'             
                            #имя url-param через которыи передается ключ рубрики
                            pk_url_kwarg = 'rubric_id'
                            
                            #переопределяем
                            def get(self, request, *args, **kwargs):
                                #вызываем .get_object() унаследованныи от SingleObjectMixin для извлечения рубрики с заданным ключем
                                self.object = self.get_object(queryset=Rubric.objects.all())
                                return super().get(request, *args, **kwargs)
                            
                            def get_context_data(self, **kwargs):
                                context = super().get_context_data(**kwargs)
                                #заносим наиденную в .get() рубрику в v контекста шаблона
                                context['current_rubric'] = self.object
                                #добавляем ∀ рубрики
                                context['rubrics'] = Rubric.objects.all()
                                context['bbs'] = context['object_list']
                                return context
                            
                            def get_queryset(self):
                                return self.object.bb_set.all()
                            #PS здесь мы сталкиваемся с проблемои шаблон за набором v обращается к v контекста шаблона bbs
                                #в пред версии контроллера (см ListView) мы указали имя для этои v записав ее в .context_object_name, но здесь это не сработает - указав новое имя для v в .context_object_name мы зададим новое имя v в которои будет ⊃ рубрика, а не набор объяв(ввиду особенностеи работы множественного наследования python)
                                    #-> в результате получим трудно диагностируемую err
                                        #-> делаем иначе в .get_context_data() создаем v bbs контекста шаблона, присваиваем еи val object_list by def ⊃ набор записеи выводимых ListView
                                            #и в переопределенном .get_queryset() >> набор объяв(полученныи через диспетчер обратнои связи) связанных с наиденнои рубрикои


по идее GET-param != url-param
#один передается в GET-запросе, а второи через парсинг routes                            

orphan:eng:сирота, висящая str



        ЗАДАНИЕ VAL ПАРАМЕТРОВ КОНТРОЛЛЕРОВ КЛАССОВ
            .as_view()
            #см as_view()
            #менее мощен чем создание производного класса -> исп реже
            
            
            создание производного класса с указанием val в соотв attr класса
            #позволяет более радикально Δ поведение переопределением методов -> исп чаще .as_view()
                class BbCreateView(CreateView):
                    template_name = 'bboard/create.html'
                    model = Bb
                ...
                path('add/', BbCreateView.as_view()),
            


        ФОРМИРОВАНИЕ ОТВЕТА КОНТРОЛЛЕРОМ
        #основная задача контроллера, отправляется user'у
        #обычно ⊃ web-page
            
            НИЗКОУРОВНЕВЫЕ СРЕДСТВА ФОРМИРОВАНИЯ ОТВЕТА КОНТРОЛЛЕРОМ
            #см HttpResponse
            #исп краине редко
            
            ВЫСОКОУРОВНЕВЫЕ СРЕДСТВА ФОРМИРОВАНИЯ ОТВЕТА КОНТРОЛЛЕРОМ
                ФОРМИРОВАНИЕ ОТВЕТА НА ОСНОВЕ ШАБЛОНА
                #исп гораздо чаще низкоуровневых средств формирования ответа
                #см шаблонизатор
        
        ПОЛУЧЕНИЕ СВЕДЕНИЙ О ЗАПРОСЕ
        #см HttpRequest

ПРИМЕСИ
#mixin's
#реализует большую часть функционала контроллеров-классов
#базовые для контроллеров-классов
#класс только для расширения fx других классов
#см контроллеры-классы

ПАГИНАТОР
#может исп для разбиения на части при извлечении набора записеи из модели посредством MultipleObjectMixin ⊃ django.views.generic.list
    django.core.paginator
        .Paginator
        #by def указывается MultipleObjectMixin.paginator_class ⊃ django.views.generic.list

МАРШРУТЫ И МАРШРУТИЗАТОР
	связываем(объявляем связь) url определенного формата(шаблонного url) с контроллером
	#объявляем маршрут
	#шаблонный url должен ⊃ только относительный путь без
		названия протокола
		адреса хоста|доменного имени
		порта(tcp)
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



path(<template_url>:str, <view>|<вложенныи_список_маршрутов> [,...][, name=<route_name>])
#в качестве второго параметра может принимать список маршрутов уровня приложения	
	#связывает "admin/" со списком маршрутов возвращаемый св-вом urls экземпляра(?а выглядит как класс) AdminSite который хранится в var(?а я думал это модуль) site и представляет текущую административный веб-сайт dj => при переходе по <host>:port/admin/ загружается админка 
	path('admin/',admin.site.urls)
#
    <template_url>
    #начинается не с '/', но заканчивается '/'
    #формат обьявления в шаблоне url-параметров(параметризованныи маршрут)
        < [<format>:]<param_name> >
            <format>
            #очевидно что при несовпадении с url -> маршрут считается не совпавшим
                str
                #∀ непустая ⊅ слеши
                int
                #positive int ⊃ 0
                slug
                #строковыи слаг ⊃ latin chars,nums, '-', '_'
                #короче слово
                uuid
                #уникальныи универсальныи id
                #дб правильно форматирован ⊃ '-', ∀ буквы lowercase
                path
                #∀ непустая str ⊃ слеши
                #обычно исп для сравнения с целым фрагментом полученного url
            <param_name>
            #задает имя параметра view через которое он может получить val
            #должно удовлетворять правилам именования python v
    <view>
    #ссылка на fx|результата .as_view() ⊃ контроллера-класса
    name
    #создание именованного маршрута
    #исп для обратного разрешения uri
        ulrpatterns = [
            path('<int:rubric_id>/', by_rubric, name='by_rubric'),
        ]
        #теперь можно исп обратное разрешение uri указав имя маршрута & ⊃ val url-параметров(if это параметризованныи маршрут)
        #в контроллере
            from django.urls import reverse
            ...
            url = reverse('by_rubryc', kwargs={'rubric_id': 2})
        #в шаблоне
            <a href="{% url 'by_rubric' rubric_id=2 %">...</a>
        
        

#example
    #исп контроллера-класса
    from django.urls import path
    from .views import index, by_rubric, BbCreateView
    urlpatterns = [
        path('add/', BbCreateView.as_view()),
        path('<int:rubric_id>/', by_rubric),
        path('', index),
    ]



создатели dj настоятельно не рекомендуют использовать для формирования списка маршрутов тупое добавление шаблонов и контроллеров в /<project>/urls.urlpatterns
#т.к. при большом числе маршрутов его будет сложно поддерживать(вообще делать что-либо вручную это очевидно хреново) =>
	вместо этого
		маршрутизатор dj при просмотре списка маршрутов не требует полного совпадения url из клиентского запроса и шаблона, достаточно лишь совпадения с началом реального(?полученный от клиента?существующий - просто полученный адрес!) тогда шаблонизатор удаляет из реального адреса его начальную часть(префикс) совпавшую с шаблоном и запускает указанный в маршруте контроллер
			,но path() позволяет указать вторым параметром другой список маршрутов вместо view => можно указать для ∀ маршрута другой вложенный в него список маршрутов
				тогда маршрутизатор выполнит просмотр маршрутов ⊃ вложенному списку используя для сравнения адрес с уже удаленным префиксом
					=> можно создать иерархию списков маршрутов, 
						в списке маршрутов уровня проекта укажем маршруты указывающие на вложенные списки записанные в отдельных app(списки маршрутов уровня app)
							в списках маршрутов уровня app запишем контроллеры ⊂ логику сайта
вложенный список маршрутов передаваемый path() должен представлять собой результат django.urls.include()
if полученныи url не совпал ни с одним шаблоном -> клиенту отправляется стандартная страница 404
#маршрутизатор считает url совпавшим с шаблоном if шаблон находится в начале url
    #может привести к коллизии
        ] ∃
        urlpatterns = [
            path('create/', views.wrong),
            path('create/comment/', views.right)
        ]
        #url /create/comment/ будет отправлен во views.wrong
        РЕШЕНИЕ - распологать маршруты в обратном порядке
        #более вложенныи -> менее вложенныи(верхнего уровня)
            urlpatterns = [
                path('create/comment'), views.wrong),
                path('create/', views.right)
            ]
через запрашиваемыи url во входящем в его состав пути мб передано val
    для его получения нужно поместить в нужное место шаблона в соотв маршруте обозначение url-параметра
    #маршрутизатор извлечет val и передаст его в контроллер|вложенныи список маршрутов(-> val будет доступно контроллерам объявленным во вложенном списке
по возможности маршруты должны ⊃ уникальные шаблонные url
#иное бессмысленно тк ∀ кроме первого будут отброшены

django.urls

	.include(<module_path>|<список_маршрутов> [, namespace:<префикс_uri>=None)
	#two arg
	#исп для указания вложенного списка маршрутов ⊃ urlpatterns
	#принимает строку с путем к модулю ⊃ список маршрутов
	#examples
	    from djanog.contrib import admin
	    from django.urls import path, include
	    ...
	    urlpatterns = [
	        #вложенный список в виде пути к модулю
	        path('bboard/', include('bboard.urls')),
	        #вложенныи список в виде списка маршрутов ⊃ свву urls ⊂ экземпляра AdminSite ⊂ site v ⊂ django.contrib.admin
	        path('admin/', admin.site.urls),
	    ]
	
	
	.reverse_lazy("<route_name>"[,<val_of_url_param>]) -> готовый url
	#возм синтаксис ~ .reverse ⊂ django.urls
	#генерация url путем обратного разрешения
	#examples
		from django.urls import reverse_lazy
		...
		class BbCreateView(CreateView):
			...
			success_url = reverse_lazy('index')
			...
    #other examples(см path)
    #в отличие от .reverse() ⊂ django.urls , соотв названию не требует полнои загрузки и обработки списка маршрутов -> можно исп не only in контроллерах



ОБРАТНОЕ РАЗРЕШЕНИЕ URLS
#механизм
#требует именованных маршрутов
#авто формирование готового uri по имени маршрута & набору параметров
#реализуется .reverse() ⊂ django.urls

django.urls
    .reverse([<ns>:]<route_name>:<str> [[, args=None]|[, kwargs=None]] [, urlconf=None])
    #см обратное разрешение urls
        <route_name>
        #if ∃ неск app для которых указаны ns исп вид
            <ns>:<route_name>
        args:<seq_val_url_params>
        #if маршрут исп для формирования uri - параметризованныи
            #исп для указания val URL-параметров для вставки в этот uri
        #первыи элт <seq_val_url_params> задает val первого url-параметра, второй - второго, etc
        #при исп с kwargs >> exept
        kwargs:{'URL_param_name':<val>,...}
        #~ args
        #при исп с kwargs >> exept
        urlconf
        #путь к модулю ⊃ список маршрутов
        #if !∃ исп модуль ⊃ список маршрутов уровня проекта указанныи в ROOT_URLCONF
        #if указан модуль ⊃ список маршрутов уровня app -> указывать ns в <route_name> не нужно
            url1 = reverse('index', urlconf='bboard.urls')
            url2 = reverse('bboard:by_rubric', args=(current_rubric.pk,))
            url3 = reverse('bboard:by_rubric', kwargs={'rubric_id': current_rubric.pk})
    #главныи недостаток - работает only после загрузки и обработки списка маршрутов -> ее можно исп only in контроллерах
        #if нужно записать uri не в контроллерах
            attr контроллера-класса
            ...
            #нужно исп reverse_lazy() ⊂ django.urls

    #examples
        .reverse('bboard:by_rubric', kwargs={'rubric_id': 2})
        #формирует uri '/bboard/2/'
    
    
    
			
МАРШРУТИЗАЦИЯ
#процесс выяснения какои контроллер exe при получении в клиентском запросе url определенного формата

МАРШРУТИЗАТОР
#работает основываясь на списке маршрутов
#∀ элт(маршрут) устанавливает связь шаблонныи url <> view



СПОСОБЫ ПЕРЕДАЧИ ДАННЫХ В КОНТРОЛЛЕРЫ
    0. через одноименные url-параметры
        #by_rubric() получает val url-параметра rubric_id через параметр rubric_id
        urls.py
            ...
            urlpatterns = [
                path('<int:rubric_id>/', by_rubric),
            ]
            ...
        views.py
            ...
def by_rubric(request, rubric_id):
...


    1. {<val_name0>:<val1>,...} в третьем параметре path()
    #val контроллер получит через одноименные параметры
    #if маршрут ⊃ url-параметр именем = имени доп val передаваемому через dict -> контроллеру будет передано val ⊂ dict. Извлечь val url-параметра в данном случае не выидет
        urls.py
            ...
            #передача контроллеру val mode
            vals = {'mode': 'index'}
            urlpatterns = [
                path('<int:rubric_id>/', by_rubric, vals),
            ]
            ...
        views.py
            ...
            def by_rubric(request, rubric_id, mode):
            ...

СПИСКИ МАРШРУТОВ УРОВНЯ PROJECT/APP
#маршрутизатор поддерживает объявление вложенных списков маршрутов
    маршруты на отдельные app(разделы саита) объявляются на уровне проекта
    #маршруты уровня project
    #в модуле конфигурации
    #в качестве шаблонных адресов должны ⊃ префиксы с которых начинаются url разных apps
    
    маршруты на views одного app объявляются на его уровне
    #маршруты уровня app
    #могут ⊂ модулю пакета app ⊃ ∀ имя(модуль не создается manage.py startapp автоматом)
    #обычно ⊅ вложенных списков, а указывают на views



ОБЪЯВЛЕНИЕ МАРШРУТОВ
#список маршрутов - python list присваиваемыи v urlpatterns(где их ищет router)
#∀ элт res path() ⊃ django.urls



NS
#if project ⊃ неск app ⊃ = шаблонные uri(напр index/ ⊂ bboard, testapp) -> можно дать понять dj какои uri нужно сформировать обратным разрешением задав ns ∀ app
#ns - область ⊃ свои список маршрутов
#указывается в v app_name ⊂ модулю ⊃ список маршрутов app
#а разве и так не очевидно к какому app это относится?
    bboard/urls.py
        ...
        app_name = 'bboard'
        urlpatterns = [
            ...
        ]
#требуется задать для ∀ app(?что-то сомневаюсь - раньше же работало)
#для доступа к ns - маршрут предваряется '<ns>:'
    url = reverse('bboard:index')
    ...
    <a href="{% url 'bboard:index' %}">...</a>
#задает префикс uri формируемого обратным разрешением
    url = reverse('bboard:by_rubric', kwargs={'rubric_id': 2})
    #сформирует uri '/bboard/2/'
    
    
    
ROOT APP
#чтобы ∀ app было доступно по uri ⊅ префикс(/2 вместо /bboard/2/)(связано с корнем проекта(корневое app))
    указать '' шаблонным uri в соотв маршруте проекта
    задать для маршрута уровня проекта новыи пустои префикс
        urlpatterns = [
            #∀ uri ⊃ bboard ns будут начинаться с корня
            #можно попасть на index.html ⊂ app по uri вида http://localhost:8000/
            path('', include('bboard.urls', namespace='')),
            ...
        ]


PATTTERNS AS RE
#исп if путь очень сложен|при переносе кода dj 1.11-
#исп re_path() ⊂ django.urls
#дает полныи контроль над exe сравнения
    r'^...'
    #default
    #шаблон должен ⊂ началу uri
    r'...$'
    #шаблон должен ⊂ концу uri


    django.urls
        re_path(<re>:str, <view>|<вложенныи_список_маршрутов> [, ...][, name=<route_name>])
        #исп if путь очень сложен|при переносе кода dj 1.11-
            <re>
            #передается python re -> должна ⊃ соотв формат
        #other args ~ path ~ django.urls
        #examples
            from django.urls import re_path
            from .views import index, by_rubric, BbCreateView
            ...
            urlpatterns = [
                re_path(r'^add/$', BbCreateView.as_view(), name='add'),
                re_path(r'^(?P<rubric_id>[0-9]*)/$', by_rubric, name='by_rubric'),
                re_path(r'^$', index, name='index'),
            ]


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
#при создании модели для !∃ таблицы требуется генерация и и примерынение миграции
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
		#return последнюю запись набора | if набор пуст >> None
			b = Bb.objects.last()
			b.title >> 'Дача'
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
		#if набор ⊃ записи >> True
		#else	>> False
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
		#вызов без параметров -> сбрасывает параметры сортировки
			#?проверить
			
			
			
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




вызов exept ?= кинуть exept
	ВАЛИДАТОРЫ
	#exe валидацию val ⊂ отдельным полям
	#реализуются классами|fx
	#тк у меня backend очевидно что валидация происходит после отправки данных из формы -> по сути это реально тупо callable
	
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


ВЫВОД СООБЩЕНИЙ ОБ ОШИБКАХ И ОБРАБОТКА ОСОБЫХ СИТУАЦИИ
#выдача посетителю
    404
    ...
#уведомление браузера
    страница !Δ с посл вызова и можно исп кеш
    ...
    
    django.http
        HttpResponseNotFound([<content>][, content_type=None][, status=404][, reason=None])
        #производныи HttpResponse
        #мб исп для самостоятельнои обработки нештатных/специфичных ситуации
            #dj в большинстве случаев справляется сам
                #by def отправляет клиенту краткое msg о ошибке(мб Δ)
        #запрашиваемая страница не наидена
        #examples
            def detail(request, bb_id):
                try:
                    bb = Bb.objects.get(pk=bb_id)
                except Bb.DoesNotExist:
                    return HttpResponseNotFound('Такой страницы нет')
                return HttpResponse(...)
        #альтернатива бросить Http404
            def detail(request, bb_id):
                try:
                    bb = Bb.objects.get(pk=bb_id)
                except Bb.DoesNotExist:
                    raise Http404('Такой страницы нет')
                return HttpResponse(...)
        
        
        HttpResponseBadRequest([<content>][, content_type=None][, status=400][, reason=None])
        #клиентскии запрос сформирован некорректно
        #исп ~ HttpResponseNotFound
        
        
        HttpResponseForbidden([<content>][, content_type=None][, status=403][, reason=None])
        #доступ к странице запрещенн
        #обычно if user не залогинился
        #исп ~ HttpResponseNotFound
        #альтернатива - бросить PermissionDenied ⊂ django.core.exceptions
        
        
        HttpResponseNotAllowed(<seq_обозначении_разрешенных_методов>[,content_type=None][, status=405][, reason=None])
        #клиентскии запрос был exe с исп недопустимого метода
        #возвращается в том числе декораторами устанавливающими набор разрешенных HTTP-методов
        #examples
            return HttpResponseNotAllowed(['GET'])
        
        
        HttpResponseGone([<content>][, content_type=None][, status=410][, reason=None])
        #запрошенная страница больше !∃
        
        
        HttpResponseServerError([<content>][, content_type=None][, status=500][, reason=None])
        #ошибка в коде сайта
        
        
        
        HttpResponseNotModified([<content>][,content_type=None][, status=304][, reason=None])
        #страница !Δ и мб извлечена из кеша
        
        

ИСКЛЮЧЕНИЯ
    NotImplementedError
    #бросается исходнои реализациеи BaseDateListView.get_dated_items()
    django.http
        Http404
        #запрашиваемая страница не наидена
        #см HttpResponseNotFound
    django.core.exceptions
        PermissionDenied
        #альтернатива HttpResponseForbidden
        
        MultipleObjectsReturned
        #бросается if callable расчитан на возврат одного val а условиям удовл неск


СПЕЦИАЛЬНЫЕ ОТВЕТЫ
#if нужно отправить клиенту данные != html/text -> HttpResponse не подоидет
    #dj ⊃ 3 класса спец ответов ⊂ django.http
    
    
    
        StreamHttpResponse(<content> [, content_type=None][, status=200][, reason=None])
        #в отличие от HttpResponse полностью формирующегося в mem перед отправкой
            <content>
            #seq ⊃ str | iterator -> bytes's
            content_type
            #MIME-type ответа & кодировку
                content_type=None
                #ответ получит MIME-type text/html и кодировку ⊂ DEFAULT_CHARSET
            status
            #int code response status
                200
                #файл успешно отправлен
            reason
            #str обозначение статуса
        #attr
            <streaming_content>
            #iterator выдающий фрагменты <content> в <bytes>
            status:<int>
            #status code
            reason_phrase
            #str status
            streaming
            #всегда True(ответ - потоковыи)
        #examples
            from django.http import StreamHttpResponse
            ...
            def index(request):
                resp_content = ('Here', 'will', 'be', 'site', 'main', 'page')
                resp = StreamHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
                resp['keywords'] = 'Python, Django'
                return resp
            #?>> dict
            
        #if нужно отправить клиенту данные != html/text | if V слишком большои
        #потоковыи ответ, формируется & отправляется небольшими частями
    
    
        .FileResponse(<file_obj> [, as_attachment=False][, filename=''][, content_type=None][, status=200][, reason=None])
        #отправка фаилов
        #examples
            #
            from django.http import FileResponse
            filepath = r'c:/images/image.png'
            ...
                return FileResponse(open(filepath, 'rb'))
        #производный StreamHttpResponse
            as_attachment
                as_attachment=False
                #отправленный фаил откроется в браузере
                as_attachment=True
                #отправленный фаил будет сохранен на диске
                #if файл ⊅ имени(напр был сформирован в mem и еще не был записан на диск) -> требует ∃ filename
            filename
            #указание имени отправляемого фаила
            #см as_attachment
        
        
        
        .JsonResponse(<data> [, safe=True][, encoder=DjangoJSONEncoder])
        #отправка данных в формате JSON
            <data>:<dict>
            #кодируемые данные
            #if требуется отправить данные ⊄ dict -> safe
            safe
            #
                safe=False
                #if требуется закодировать & отправить не dict
            encoder
            #кодировщик в JSON
        #examples
            data = {'title': 'Motorcycle', 'content': 'Old', 'price': 10000.0}
            return JsonResponse(data)
        #производный StreamHttpResponse
    




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
	
	CUSTOM ВАЛИДАТОР-FX
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
	
	
	CUSTOM ВАДИДАТОР-КЛАСС
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
#ps вывод при запуске idle
# Shell Plus Model Imports
	from app.models import FieldsTest
	from django.contrib.admin.models import LogEntry
	from django.contrib.auth.models import Group, Permission, User
	from django.contrib.contenttypes.models import ContentType
	from django.contrib.sessions.models import Session
	# Shell Plus Django Imports
	from django.core.cache import cache
	from django.conf import settings
	from django.contrib.auth import get_user_model
	from django.db import transaction
	from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
	from django.utils import timezone
	from django.urls import reverse


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
			#необязательные параметры конструкторов классов допустимы лишь при задании именованных параметров в вызовах aggregate|annotate (иначе >> exept)
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
					#examples
						Coalesce('content', 'addendum', Value('--пусто--'))
						#if val ⊂ 'content' field != null -> будет возвращено оно, etc пока не доидет до '--пусто--'
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
									...
									#очевидно что content ⊃ '' а не null
								
							
					
eng:coalesce:объединяться


					
					.Greatest(<val0>, <val1>, ...) -> max val
						<valn>
						#строковое имя поля|экз F|экз Value
						#∀ поля должны ⊃ один тип, иначе err(см .Coalesce)
					
					
					
					.Least(<val0>, <val1>, ...) -> min val
						<valn>
						#строковое имя поля|экз F|экз Value
							
							
					
					.Cast(<val>, <type>)
					#принудительно преобразует <val> -> <type> и возвращает результат
						<valn>
						#строковое имя поля|экз F|экз Value
						#∀ поля должны ∀ один тип, иначе err(см .Coalesce)
						<type>
						#instance ⊃ type
						
						
						
					.Concat(<val0>, <val1>, ...) -> "vals_concatenated_to_str"
					#объединяет vals в str и возвращает ее
						<valn>
						#строковое имя поля|экз F|экз Value ⊃ строковый|текстовый тип
						
						
						
					.Lower(<val>) -> str
					#str to lower case
						<val>
						#строковое имя поля|экз F|экз Value ⊃ строковый|текстовый тип
						
						
						
					.Upper(<val>) -> str
					#str to upper case
						<val>
						#строковое имя поля|экз F|экз Value ⊃ строковый|текстовый тип
					
					
					
					.Length(<val>) -> число char
						<val>
						#строковое имя поля|экз F|экз Value ⊃ строковый|текстовый тип|Null
						#if val = Null >> None
						
						
						
					.StrIndex(<val>, <substr>) -> int
					#номер вхождения указаннои <substr> в строковое <val>
					#(wtf?)нумерация chars в str начинается с 1
						<substr>
						#if ⊄ <val> >> 0
						<val>
						#строковое имя поля|экз F|экз Value ⊃ строковый|текстовый тип
						
						
						
					.Substr(<val>, <position> [, <length>]) -> substr
					#извлечение подстроки из <val> с указанной <position>/<length>
					#(wtf?)нумерация chars в str начинается с 1
						<length>
						#if !∃ -> излекается ∀ оставшаяся часть val
						<val>
						#строковое имя поля|экз F|экз Value ⊃ строковый|текстовый тип
						
						
						
					.Left(<val>, <length>) -> str
					#>> подстроку начинающуюся с заданного <val> ⊂ <length>
					
					
					
					.Right(<val>, <length>) -> str
					#>> подстроку заканчивающуюся в конце <val> ⊂ <length>
					
					
					
					.Replace(<val>, <substr>[, <newsubstr> = '']) -> str
					#>> str ⊃ замененные substr
					#учитывает регистр
					
					
					
					.Repeat(<val>, <n>)
					#>> <val> повторенное <n> раз
					
					
					
					.LPad(<val>, <length>[, <char-заполнитель>=' ')
					#>> <val> дополненное до <length>
					
					
					
					.Trim(<val>)
					#>> <val> с удаленными начальными & конечными пробелами(?|пробельными символами)
					
					
					
					.LTrim(<val>)
					#>> <val> с удаленными начальными пробелами(?|пробельными символами)
					
					
					
					.RTrim(<val>)
					#>> <val> с удаленными конечными пробелами(?|пробельными символами)
					
					
					
					.Chr(<char_code>)
					#~ python chr()
					#>> char с указанным кодом
					
					
					
					.Ord(<val>)
					#~ python ord()
					#>> int код первого char указанного <val>
					
					
					
					.Now() -> <curr_datetime>
					#
					
					
					
					.Extract(<val>, <извлекаемая_часть_val>[, tzinfo=None])
					#извлекает часть val date|time и возвращает его в виде чисва
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
						<извлекаемая_часть_val>
						#
							"year"
							"quarter"
							"month"
							"day"
							"week"
							#номер недели
							"week_day"
							"hour"
							"minute"
							"second"
						tzinfo
						#исп крайне редко
					#examples
						Extract('published', 'year')
					
					
					.ExtractYear(<val>[, tzinfo=None])
					#проще .Extract в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						ExtractYear('published')
						
					
						
					.ExtractQuarter(<val>[, tzinfo=None])
					#проще .Extract в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						ExtractQuarter('published')
						
					
						
					.ExtractMonth(<val>[, tzinfo=None])
					#проще .Extract в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						ExtractMonth('published')
						
					
						
					.ExtractDay(<val>[, tzinfo=None])
					#проще .Extract в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						ExtractDay('published')
						
					
						
					.ExtractWeek(<val>[, tzinfo=None])
					#проще .Extract в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						ExtractWeek('published')
						
					
						
					.ExtractWeekDay(<val>[, tzinfo=None])
					#проще .Extract в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						ExtractWeekDay('published')
						
					
						
					.ExtractHour(<val>[, tzinfo=None])
					#проще .Extract в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						ExtractHour('published')
						
					
						
					.ExtractMinute(<val>[, tzinfo=None])
					#проще .Extract в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						ExtractMinute('published')
						
					
						
					.ExtractSecond(<val>[, tzinfo=None])
					#проще .Extract в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						ExtractSecond('published')
						
					
						
					
					.Trunc(<val>, <конечная_часть>[, output_field=None][, tzinfo=None])
					#сбрасывает в 0 <val> до конечнои части справа
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
						<конечная_часть>:str
						#
							"year"
							"quarter"
							"month"
							"week"
							"day"
							"hour"
							"minute"
							"second"
						output_field
						#тип возвращмого val даты&|времени
						#представляется экземпляром DateField|TimeField|DateTimeField
						#if !∃ -> тип результата = типу <val>
						tzinfo
						#исп краине редко
					#examples
						#] published ⊂ datetime(05.06.2018 08:62:28.366947
						Trunc('published', 'year')			# 01.01.2018 00:00:00
						Trunc('published', 'quarter')		# 01.04.2018 00:00:00	# второи квартил
						Trunc('published', 'month')			# 01.06.2018 00:00:00
						Trunc('published', 'week')			# 04.06.2018 00:00:00
						Trunc('published', 'day')			# 05.06.2018 00:00:00
						Trunc('published', 'hour')			# 05.06.2018 08:00:00
						Trunc('published', 'minute')		# 05.06.2018 08:02:00
						Trunc('published', 'second')		# 05.06.2018 08:02:28
					
					
					
					.TruncYear(<val>[, output_field=None][, tzinfo=None])
					#сбрасывает в 0 <val> кроме year (сбрасывает до года)
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time?|datetime
					#examples
						TruncYear('published')
					
					
					
					.TruncQuarter(<val>[, output_field=None][, tzinfo=None])
					#сбрасывает до квартала
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time?|datetime
					#examples
						TruncQuarter('published')
					
					
					
					.TruncMonth(<val>[, output_field=None][, tzinfo=None])
					#сбрасывает до месяца
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time?|datetime
					#examples
						TruncMonth('published')
					
					
					
					.TruncWeek(<val>[, output_field=None][, tzinfo=None])
					#сбрасывает до полуночи понедельника текущеи недели
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time?|datetime
					#examples
						TruncWeek('published')
					
					
					
					.TruncDay(<val>[, output_field=None][, tzinfo=None])
					#сбрасывает до числа
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time?|datetime
					#examples
						TruncDay('published')
					
					
					
					.TruncHour(<val>[, output_field=None][, tzinfo=None])
					#сбрасывает до часов
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date?|time|datetime
					#examples
						TruncHour('published')
					
					
					
					.TruncMinute(<val>[, output_field=None][, tzinfo=None])
					#сбрасывает до минут
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date?|time|datetime
					#examples
						TruncMinute('published')
					
					
					
					.TruncSecond(<val>[, output_field=None][, tzinfo=None])
					#сбрасывает до секунд
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date?|time|datetime
					#examples
						TruncSecond('published')
					
					
					
					.TruncDate(<val>[, output_field=None][, tzinfo=None])
					#извлекает дату
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time?|datetime
					#examples
						TruncDate('published')
					
					
					
					.TruncTime(<val>[, output_field=None][, tzinfo=None])
					#извлекает время
					#проще Trunc в применении
						<val>
						#представляется экземпляром F и должно принадлежать date|time|datetime
					#examples
						TruncTime('published')
					
			УСЛОВНЫЕ ВЫРАЖЕНИЯ СУБД
			#менее мощны чем ⊂ python
			#exe проверки сообразуясь с переданными условиями
			#когда очередное усл exe -> он возвращается как результат(по сути or)
			#для записи условного exp исп класс django.db.models.Case
				django.db.models
				
				
					.Case(<усл0>, <усл1>, ..., <услN>[, default=None][,output_field=None])
					#класс исп для записи условного выражения
					#∀ <усл> - экз When ⊃ django.db.models
					#<усв> проверяются в порядке записи, if усл exe -> возвращается val ⊂ then ⊂ .When(), осталяные усл отбрасываются
					#if ∀ val !exe -> >> default
						output_field
						#тип возвращаемого val в виде экз класса поля нузного типа
						#лучше указывать несмотря на неомязателяность
					#выведем список рубрик с пометкои ⊃ ~ число объявлении
						from django.db.models import Case, When, Value, Count, CharField
						for r in Rubric.objects.annotate(cnt=Count('bb'),
						         cnt_s=Case(When(cnt__gte=5, then=Value('Too much')),
						                    When(cnt__gte=3, then=Value('Middle')),
						                    When(cnt__gte=1, then=Value('Too few')),
						                    default=Value('Nothing'),
						                    output_field=CharField())):
						    print('%s:\t\t%s' % (r.name, r.cnt_s))
					    >>
					        Бытовая техника:    Too few
					        Мебель:             Nothing
					        Недвижимость:       Too much
					        Растения:           Nothing
					        Сантехника:         Nothing
					        Сельхозинвентарь:   Nothing
					        Транспорт:          Too much
					        
					        
					        
					.When(<усл>, then=None)
					#мб записано в формате (<field> = val|<field>__<filter>=<val>) | экземпляром Q
						then
						#val возвращаемое при exe <усл>
			ВЛОЖЕННЫЕ ЗАПРОСЫ
			#могут исп в усл фильтрации|для расчета результов вычисляемых полеи
			#dj позволяет создавать вложенные запросы двух видов
			    ПОЛНО-FX ВЛОЖЕННЫЕ ЗАПРОСЫ
			    #возвращают какои-либо результат
			    #создаются классом Subquery ⊃ django.db.models
			        
			        Subquery(<вложенныи_набор_записеи>[, output_field=None])
			        #класс
			        #создает полно-fx вложенные запросы возвращающие какои-либо результат
			            <вложенные_набор_записеи>
			            #формируется с исп упоминавшихся ранее инструментов
			            output_field
			            #тип возвращаемого val if этот результат представлен единичным val
			        #example
			            #список рубрик с датои и временем публикации последнего объявления
			            from django.db.models import Subquery, OuterRef, DateTimeField
			            #во вложенном запросе нужно сравнить val поля rubric объявления с val ключевого поля pk рубрики ⊂ "внешнему" запросу(ссылку на которое оформляем как OuterRef)
			            sq = Subquery(Bb.objects.filter(
			            rubric=OuterRef('pk')).order_by('-published').values(
			            'published')[:1])
			            for r in Rubryc.objects.annotate(last_bb_date=sq):
			                print(r.name,'\t\t', r.last_bb_date)
			            >>
			                Бытовая техника     2018-06-13 11:05:59.421877+00:00
			                Мебель              None
			                Недвижимость        2018-06-12 07:41:14.050001+00:00
			                ...
			            
			            
                    OuterRef(<поле_"внешнего_набора_записеи">)
                    #if во вложенном наборе записеи нужно ссылаться на поле "внешнего набора записеи -> ссылка на это поле записываемая в условиях фильтрации вложенного набора записеи оформляется как экземпляр OuterRef
                    #examples(см Subquery)
				ВЛОЖЕННЫЕ ЗАПРОСЫ ВТОРОГО ВИДА
				#проверяют ∃ ли в этом запросе записи
				#создаются классом Exists ⊂ django.db.models
				
					Exists(<вложенныи_набор_записеи>)
					#проверка на ∃ записеи в запросе
						#выведем рубрики ⊃ объявления ⊂ цену > 100000
						from django.db.models import Exists
						from app.models import Bb
						subquery = Exists(Bb.objects.filter(rubric=OuterRef('pk'),
						                                    price__gt=100000))
						for r in Rubric.objects.annotate(is_expensive=subquery).filter(is_expensive=True):
							print(r.name)
						>>
							Недвижимость
			
			
			ОБЪДИНЕНИЕ НАБОРОВ ЗАПИСЕИ
			
				union(<набор_записеи_0>,<набор_записеи1>,...[, all=False]) -> <набор_записеи>
				#объединение наборов записеи в один(объединение ∀ заданных с текущим)
					all
					#
						True
						#результат ⊃ дубли
				#у наборов записеи не следует задавать сортировку(можно убрать сортировку вызвав order_by() без параметров)
					#сформируем набор из объявлении с ценои > 100000 и объявлении о продаже бытовои техники
					bbs1 = Bb.objects.filter(price__gte=100000).order_by()
					bbs2 = Bb.objects.filter(rubric__name='Бытовая техника').order_by()
					for b in bbs1.union(bbs2):
						print(b.title, sep=' ')
					>>
						Дача
						Дом
						Земельный участок
						Пылесос
						Стиральная машина
						
				
				
				intersection(<набор_записеи_0>,<набор_записеи1>,...)
				#>> набор ⊃ записи ⊂ ∀ наборах
				
				
				difference(<набор_записеи_0>,<набор_записеи1>, ...)
				#>> набор ⊃ записи ⊂ только одному из переданных наборов, а не нескольким сразу
				#?symmetric difference
		
		ИЗВЛЕЧЕНИЕ VAL ТОЛЬКО ИЗ ЗАДАННЫХ ПОЛЕИ
		#извлечение из модели только val определенного поля/полеи хранящихся там записеи
		
			values([<field0>, <field1>, ...])
			#извлекает из модели val указанных полеи
			#>> <QuerySet_instance> ⊃ {'<field0>':<val>,'<field1>':<val>,...}
			#if ∀ val хранятся в одном dict -> нафига неск dict?
			#поле мб задано
				positional_arg
				#str ⊃ field_name
				named_arg
				#экз F, имя параметра станет именем поля
			#при передаче в качестве одного из args поля внешнего ключа -> элт результирующего dict соотв этому полю будет ⊃ val ключа связанной записи, а не саму запись
			#examples
				Bb.objects.values('title', 'price', 'rubric')
				>>
					<QuerySet [
						{'title': 'Стиральная машина', 'price': 3000.0, 'rubric': 3},
						{'title': 'Пылесос', 'price': 1000.0, 'rubric': 3},
						...
					]>
				Bb.objects.values('title', 'price', rubric_id=F('rubric'))
				>>
					<QuerySet [
						{'title': 'Стиральная машина', 'price': 3000.0, 'rubric_id': 3},
						{'title': 'Пылесос', 'price': 1000.0, 'rubric_id': 3},
						{},
						{},
						
					]>
			#при вызове без параметров >> набор dicts ⊃ ∀ поля таблицы бд обрабатываемои этои моделью
				#обрати внимание на имена полеи -> это имена полеи таблицы бд, а не модели
				Bb.objects.values()
				>>
					<QuerySet [
						{'id': 23, 'title': 'Стиральная машина',
						'content': 'Автоматическая', 'price': 3000.0,
						'published': datetime.datetime(2018, 6, 13, 11, 5, 59, 421877, tzinfo=<UTC>),
						'rubric_id': 3},
						...
					]>
			
			
			
			values_list([<field0>, <field1>, ...][, flat=False][, named=False])
			#~ values, но возвращает набор tuples вместо dict
			    flat
			    #имеет смысл исп only if возвращается одного поля
			        flat=False
			        #val поля оформляются как кортежи ⊃ один элт
			            Bb.objects.values_list('id')
			            >>
			                <QuerySet [(23,), (22,), (8,), (17,), (16,), (13,), (12,), (10,), (11,), (4,), (3,), (1,)]>
			        flat=True
			        #набор ⊃ непосредственно val поля
			            Bb.objects.values_list('id')
			            >>
			                <QuerySet [23, 22, 8, 17, 16, 13, 12, 10, 11, 4, 3, 1]>
			        named
			        #
			            named=True
			            #исп именованные кортежи вместо обычных
			#examples
				Bb.objects.values_list('title', 'price', 'rubric')
				>>
					<QuerySet [
						('Стиральная машина', 3000.0, 3),
						('Пылесос', 1000.0, 3),
						...
					]>
			
			
			
			dates(<field_name>, <part_of_date> [, order='ASC']) -> <QuerySet [...]>
			#возвращает набор записеи ⊃ уникальные val даты ⊂ полю и урезаны до заданнои <part_of_date>
			    <part_of_date>
			    #
			        "year"
			        "month"
			        "day"
			        #число те дата не будет урезаться
			    order
			    #упорядочивание
			        'ASC'
			        #по возрастанию
			        'DESC'
			        #по убыванию
			#examples
			    Bb.objects.dates('published', 'day')
			    >>
			        <QuerySet [datetime.date(2018, 5, 30), datetime.date(2018, 6, 4),
			        datetime.date(2018, 6, 5), datetime.date(2018, 6, 12),
			        datetime.date(2018, 6, 13)]>
			    Bb.objects.dates('published', 'month')
			    >>
			        <QuerySet [datetime.date(2018, 5, 1), datedime.date(2018, 6, 1)]>
			
			
			
			datetimes(<field_name>, <datetime_part> [, order='ASC'][,tzinfo=None])
			#~dates(), но манипулирует vals date & time
			    <datetime_part>
			    #
			        "year"
			        "month"
			        "day"
			        "hour"
			        "minute"
			        "second"
			        #val вообще не урезается
			    tzinfo
			    #timezone
			    #values
			        <UTC>
			#examples
			    Bb.objects.datetimes('published', 'day')
			    >>
			        <QuerySet [datetime.datetime(2018, 5, 30, 0, 0, tzinfo=<UTC>),
			        datetime.datetime(2018, 6, 4, 0, 0, tzinfo=<UTC>),
			        ...
			        ]>
			
			
			in_bulk(<val_seq> [, field_name='pk'])
			#ищет в модели записи, чье поле field_name ⊃ val ⊂ <val_seq>
			#>> dict(<val_⊃<val_seq>>: <obj_модели_представляюшие_наиденные_записи>
			#заданное поле(видимо field_name) должно ⊃ уникальные val(конструктору поля модели передано unique=True)
			#examples
			    Rubric.objects.in_bulk([1, 2, 3])
			    >>
			        (1: <Rubric: Недвижимость>, 2: <Rubric: Транспорт>, 3: <Rubric: Бытовая техника>)
			    Rubric.objects.in_bulk(['Транспорт', 'Мебель'], field_name='name')
			    >>
			        {'Мебель':<Rubric: Мебель>, 'Транспорт': <Rubric: Транспорт>}
			
			
			ПОЛУЧЕНИЕ VAL ПОЛЕИ СО СПИСКОМ
			#if обратиться к полю ⊂ список -> val непосредственно ⊂ полю, вместо выводящегося
			    Bb.objects.get(pk=1).kind   >> 's'
			#для получения val выводящегося user исп <model>.get_<field_name>_display()
			    
			    <model>.get_<field_name>_display()
			    #возвращает val поля ⊃ список выводимое пользователю
			        b = Bb.objects.get(pk=1)
			        b.kind   >> 's'
			        b.get_kind_display()    >> 'Продам'
			
			
ШАБЛОНЫ
#образец для формирования документа(который затем можно отдать клиенту)
	HTML
	XML
	PDF
	...
	
	
ШАБЛОНИЗАТОР
#подсис-ма dj
#загружает шаблон, объединяет его с данными(излеченными из моделей|полученными от клиента|сгенерированными при работе)(template context >> контроллером) и возвращает клиенту
#по умолчанию ищет шаблоны в <app>/templates/
	#можно Δ в настройках
#очевидно что шаблоны веб-страниц должны быть в *.html(т.к. затем отсылаются клиенту(браузеру))

#поддерживает мн-во директив/тегов/фильтров(max часто используемые - встроенны в программное ядро шаблонизатора)(встроенная библиотека) остальные реализованы в загружаемых модулях расширения
	

#почти ∀ одновременно исп only один шаблонизатор
    #исп < 1 шаблонизатора - специфическая ситуация не рассматриваемая дроновым
#∀ настроики шаблонов ⊂<list_of_dicts> ⊂ TEMPLATES ⊂ settings.py
    #∀ dict ⊂ list задает params одного из доступных шаблонизаторов
        BACKEND:<str>
        #путь к шаблонизатору
        #dj ⊃ 2:

            СТАНДАРТНЫИ ШАБЛОНИЗАТОР DJANGO
                django.template.backends.django.DjangoTemplates
                #def, исп в большинстве случаев
                #не поддерживает вызов методов ⊅ args в шаблонах
            django.template.backends.jinja2.Jinja2
            #шаблонизатор Jinja2
        
        NAME
        #псевдоним шаблонизатора для обращения
        #if !∃ ->исп последняя часть пути к его модулю
        
        
        DIRS:<list>=[]
        #список путеи к dirs где шаблонизатор будет искать шаблоны
        
        APP_DIRS:<bool>=False
        #при создании проекта устанавливается в True
            True
            #шаблонизатор дополнительно ищет шаблоны в app dirs
            False
            #поиск only in путях ⊂ DIRS
        
        OPTIONS:<dict>
        #доп params конкретного шаблонизатора
        #∀ элт задает отдельные params
            django.template.backends.django.DjangoTemplates
            #поддерживает params
                autoescape:<bool>=True
                    True
                    #∀ недопустимые HTML chars
                        "
                        <
                        >
                        #при выводе преобразуются в ~ спец символы(по идее &...)
                    False
                    #без преобразования
                
                string_if_invalid:<str>=""
                #выводится при неудаче доступа к v шаблона|вычисления expr
                
                file_charset:<str>
                #кодировка фаилов шаблонов
                #if !∃ -> исп val параметра проекта FILE_CHARSET
                
                context_processors
                #lst ⊃ str ⊃ имена модулеи реализуюших обработчики контекста, используещихся с шаблонизатором
                #val:см обработчики контекста
                
                debug:<bool>
                #if !∃ -> исп project param DEBUG
                    True
                    #вывод развернутых msg об err в шаблоне
                    False
                    #вывод кратких msg об err в шаблоне
                
                loaders
                #lst ⊃ имена модулеи загружающих шаблоны
                #dj сам выбирает загрузчики шаблонов для исп в зависимости от vals DIRS & APP_DIRS
                    #-> обычно не нужно указывать
                #vals: https://docs.djangoproject.com/en/2.1/ref/templates/api/#template-loaders
                
                builtins
                #lst ⊃ str ⊃ пути к СТОРОННИХ(only) встраиваемым lib's тегов шаблонизатора
                
                libraries:<dict>={}
                #перечень СТОРОННИХ(only) загружаемых lib шаблонов вида {<alias_библиотеки_тегов>:<str_⊃_пути_к_их_модулям>
                
                    
        
#формирование ответа на основе шаблона - высокоуровневое средство формирования ответа контроллером
    #для загрузки нужного шаблона dj предоставляет fx .get_template() & .select_template() ⊃ django.template.loader
        django.template
        #⊃ модули -> по идее lib
        
        
            .response
            #модуль
            
                .TemlateResponse(<request>:<HttpRequest>, <template_path> [,context=None][,content_type=None][,status=200])
                #формирует ответ пользователю
                #схож по fx с HttpResponse
                #осн преимущество - при исп Middlewares добавляющих в context доп данные
                #examples
                    from django.template.response import TemlateResponse
                    ...
                    def index(request):
                        bbs = Bb.objects.all()
                        rubrics = Rubric.objects.all()
                        context = {'bbs': bbs, 'rubrics': rubrics}
                        return TemlateResponse(request, 'bboard/index.html', context=context)
                #поддерживает отложенный рендеринг - exe only после прохождения ∀ цепи зарегистрированных в проекте посредников, непосредственно перед отправкой ответа клиенту - благодаря этому посредники вообше могут добавлять данные в context
                    <request>
                    #доступен в контроллере-fx через его первый параметр
                    <context>
                    #контекст шаблона
                    content_type=None
                    #ответ получит MIME-type text/html и кодировку ⊂ DEFAULT_CHARSET
                    status
                    #int status code
                #attr
                    .template_name
                    #⊃ template path
                    #не очень то ~ названию
                    .context_data
                    #⊃ контекст шаблона
                    
                    
            Template
            #класс представляющий шаблон
            
                .render([context:<dict>=<контекст_данных>] [, request=<request>])
                #рендерит шаблон(объедининяя текущий шаблон и контекст данных
                    context
                    #dict ⊃ val которые должны быть доступны в шаблоне
                    request
                    #if ∃ -> добавляется в context
                #>> str ⊃ html страницы
                #examples
                    from django.http. import HttpResponse
                    from django.template.loader import get_template
                    ...
                    def index(request):
                        bbs = Bb.objects.all()
                        rubrics = Rubric.objects.all()
                        context = {'bbs': bbs, 'rubrics': rubrics}
                        template = get_template('bboard/index.html')
                        return HttpResponse(template.render(context=context, request=request))
                
                
                
            TemplateDoesNotExist
            #exept
            
            TemplateSyntaxError
            #exept
            #см django.template.loader
            
            
            
            django.template.loader
            
                .get_template(<template_path>)
                #загружает шаблон & >> представляющии его экз Template ⊃ django.template
                #if шаблон не удалось загрузить >> exept TemplateDoesNotExist
                #if шаблон ⊃ err >> exept TemplateSyntaxError
                    <template_path>
                    #пути указываются относительно dir ⊃ templates
                
                
                .select_template(<seq_of_temlates_path>) -> <django.template.Template>
                #перебирает пути пытаясь загрузить шаблон и >> первыи загруженныи
                #if шаблон не удалось загрузить >> exept TemplateDoesNotExist
                #if шаблон ⊃ err >> exept TemplateSyntaxError
                    <seq_of_temlates_path>
                    #пути указываются относительно dir ⊃ templates


                
    ВЫВОД ДАННЫХ
                    
        ДИРЕКТИВЫ
        #исп для вывода данных
        #~include c++
        #поддерживает
            исп литералов
            извлечение val и помещение в это место
                {{ <context_var> }}
            обращение к
                    элту коллекции по
                        индексу
                        ключу
                    attr класса|экземпляра
                    вызывать fx ⊅ args
                исп одинаковую dot notation
                    #элт list
                    {{ rubrics.0 }}
                    #элт dict/attr класса|экземпляра
                    {{ current_bb.kind }}
                    #вызов метода
                    {{ rubric.get_absolute_url }}
        #не поддерживает
            вызов методов с args
            #см СТАНДАРТНЫИ ШАБЛОНИЗАТОР DJANGO
            expr

        ТЕГИ ШАБЛОНИЗАТОРА DJ
        #поддерживают исп литералов
        #obj ⊃ в состав контекста шаблона(формируется программистом)
        #syntax
            {% <tag> [<params>] %}[<СОДЕРЖИМОЕ>][{% end<tag> %}]
        #управляют генерированием содержимого результирующего документа
            ОДИНАРНЫЕ ТЕГИ ШАБЛОНИЗАТОРА    
            #обычно вставляет val вычисленное dj
            
                {% csrf_token %}
                #тег шаблонизатора
                #создает в форме скрытое поле, хранящее токен, получение которого контроллером - гарантия того что данные получены с текущего сайта и им "можно доверять"
                #часть подсис-мы безопасности dj/исп еи
                
            
            {% url <[ns:]route_name> <val_параметров_через_пробел> [as <v>] %}
            #формирует uri обратным разрешением в шаблонах
                <val_параметров_через_пробел>
                #позиционные|именованные
                as <v>
                #сохранение uri в v вместо втыкания в шаблон
            #examples
                <a href="{% url 'bboard:detail' bb.pk %}">{{ bb.title }}</a>
                <a href="{% url 'bboard:by_rubric' rubric_id=bb.rubric.pk %}">{{ bb.rubric.name }}</a>
                #сохранение uri в v вместо втыкания в шаблон
                    {% url 'bboard:detail' bb.pk as detail_url %}
                    <a href="{{ detail_url }}">{{ bb.title }}</a>
            
            
            {% cycle <space_separated_vals> [as <v>]%}
            #ₓ помещает в шаблон vals
            #вроде исп в циклах 
            #inf -> при достижении конца начинает сначала
            #число vals неограниченно
            #examples
                #на ∀ итерации for, cycle вставляет 'bb1'-'bb3' в 'div class=' 
                {% for bb in bbs %}
                <div class="{% cycle 'bb1' 'bb2' 'bb3' %}">
                    <h2>{{ bb.title }}</h2>
                    <p>{{ bb.content }}</p>
                    <p>{{ bb.published|date:"d.m.Y H:i:s" }}</p>
                </div>
                {% endfor %}
                #текущее val можно помещать в v шаблона для исп в ∀ его месте
                {% for bb in bbs %}
                {% cycle 'bb1' 'bb2' 'bb3' as currentclass %}
                <div class="{{ currentclass }}">
                    <h2>{{ bb.title }}</h2>
                    <p>{{ bb.content }}</p>
                    <p class="{{ currentclass }}">{{ bb.published|date:"d.m.Y H:i:s"}}</p>
                </div>
                {% endfor %}
                
                
                {% resetcycle [<v>] %}
                #сбрасывает {% cycle ...%} (by def последнии записанныи в шаблоне) и начинает перебирать его vals с начала
                #для сброса конкретного тега нужно указать v записанную в нужном {% cycle %}
                
            {% firtsof <space_separated_vals> %} 
            #помещает в шаблон первое "не пустое" val(!= False)
            #examples
                {% firstof bb.phone bb.email 'cat' %} 
            
            
            {% regroup <seq> by <key|attr> as <v> %}
            #группировка seq ⊃ dicts|obj по val элта с заданным ключом|attr и помещает созданныи list в v
            #∀ элт list - namedtuple ⊃ элты
                grouper
                #val элта/attr по которому выполнена группировка
                list
                #list ⊃ dict|obj группы
            #examples
                #группировка объяв по рубрике
                {% regroup bbs by rubric.name as groupsd_bbs %} 
                {% for rubric_name, gbbs in groupsd_bbs %}
                    <h2>{{ rubric_name }}</h3>
                    {% for bb in gbbs %}
                    <div>
                        <h7>{{ bb.title }}</h2>
                        <p>{{ bb.content }}</p|
                        <p>{{ bb.published|date:"d.mY H:i:s" }}</p>
                    </div>
                    {% endfor %}
                {% endfor %}
                
                
            {% now <format> %}
            #вставляет в шаблон текущие время & дату
                <format>
                #~ фильтру date(см ФИЛЬТРЫ)
            #examples
                {% now 'SHORT_DATETIME_FORMAT' %}
            
            
            {% csrf_token %}
                #вставляет токен используемыи под-сисмои безопасности dj
                #исп only in <form>
            
            
            {% templatetag <обозначение_ₓ_chars> %}
            #вставка в шаблон ₓ chars которые иначе вставить нельзя
             <обозначение_ₓ_chars>
                openblock:      {%
                closeblock:     %}
                openvariable:   {{
                closevariable:  }}
                openbrace:      {
                closebrace:     }
                opencomment:    {#
                closecomment:   #}
            
            
            
<псевдонимы библиотек тегов> ~ псевдонимы через пробел
            
            
            
		    {% load <псевдонимы библиотек тегов> %}
            #предварительная загрузка модуля расширения в шаблон
		    #может исп напр для загрузки загружаемых libs тегов  
		    #examples
				{% load static %}
				...
				<head>
					...
					<link rel="stylesheet" type="text/css" href="{% static 'bboard/style.css' %}">
					...
			
			
			{% widthratio <current_val> <max_val>  <max_width> %}
			#исп для создания диаграмм
			#(<current_val> / <max_val>) * <max_width> -> вставляется в шаблон
			#examples
			    <img src="bar.png" style="height:10px;width:{% widthratioc current_value 200 100 %}px">
			
			
		    КОММЕНТАРИИ
		        
		        {% comment [<header>] %}<content>{% endcomment %}
		        #вставляет в шаблонизатор многострочныи комментарии игнорируемыи шаблонизатором 
		        #examples
                    {% comment 'доделать' %}
                    <p>Здесь будет список объяв</p>
                    {% endcomment %}
                
                
                {# <comment> #}
                #однострочныи комментарии
                #examples
                    {# <p>{{ bb.published /date:"d.m.Y H:i:s"}}</p> #}
                    
        	    
			
			
			{% debug %}
			#вывод отладочнои информации ⊃
			    контекст шаблона
			    список отладочных модулеи
			#не очень удобен на практике
			
			
			
            {% static 'link_to_static_relative_from_static' %}
			#походу генерирует ссылки на static
			#examples
				{% load static %}
				...
				<head>
					...
					<link rel="stylesheet" type="text/css" href="{% static 'bboard/style.css' %}">
					...

        
            ПАРНЫЕ ТЕГИ ШАБЛОНИЗАТОРА
            #охватывают фрагмент шаблона
            #исп для обработки шаблона
                
                {% for <v> in <obj> %}[<CONTENT>][{% empty %}<content_if_empty>]{% endfor %}
                #
                    <content_if_empty>
                    #помещатся в шаблон if <obj> ⊅ элтов
                    <CONTENT>
                    #допускает исп v создаваемых самим тегом
                        forloop.counter
                        #текущая итерация цикла начиная с 1
                        
                        forloop.counter0
                        #текущая итерация цикла начиная с 0
                        
                        forloop.revcounter
                        #число оставшихся итерации(нумерация с 1)
                        
                        forloop.revcounter0
                        #число оставшихся итерации(нумерация с 0)
                        
                        forloop.first
                            True
                            #это первая итерация
                        
                        forloop.last
                            True
                            #это последняя итерация
                        
                        forloop.parentloop
                        #у вложенного указывает на внешнии цикл
                        #examples
                            #номер итерации внешнего цикла
                            ...
                            forloop.parentloop.counter
                            ...
                #~ python for
                    перебирает элты коллекции(iterable?)
                    заносит их val в v
                    помещает в шаблон 
                #examples
                    #0
                    {% for bb in bbs %}
                    <div>
                        <h2>{{ bb.title }}</h2>
                        <p>{{ bb.content }}</p>
                        <p>{{ bb.published|date:"d.m.Y H:i:s"}}</p>
                    </div>
                    {% endfor %}
                    #1
                    {% for bb in bbs %}
                    <div>
                        <p>{{ bb.title }} №{{ forloop.counter }}</p>
                        ...
                    </div>
                    {% endfor %}
                    
                
                {% if <cond> %}[<content>]{% elif <cond> %}[<content>]...{% else %}[<content>]{% endif %}
                #~ python if
                    <cond>
                    #допускает исп
                        ==
                        !=
                        <
                        >
                        <=
                        >=
                        in
                        not
                        in
                        is
                        is not
                        and
                        or
                        not
                #examples
                    {% if bbs %}
                    <h2>Список объявлении</h2>
                    {% else %}
                    <p>Обьявлении нет</p>
                    {% endif %}
                
                {% ifchanged %}<content>{% endifchanged %}
                or
                {% ifchanged <space_separated_vals>%}<content>{% endifchanged %}
                #исп в циклах
                #выводит <content> only if оно Δ с предыдущеи итерации
                #вывод <content> if Δ одно из val ⊂ <space_separated_vals>
                #examples
                    #вывод название рубрики ⊃ текущую рубрику, только if название Δ(те if текущая рубрика вложена в другую рубрику нежели предыдущая
                    {% for rubric in rubrics %}
                    {% ifchanged %}{{ rubric.parent.name }}{% endifchanged %}
                    ...
                    {% endfor %}
                    #второи формат
                    {% for rubric in rubrics %}
                    {% ifchanged rubric.parent %}
                    {{% endifchanged %}}
                    ...
                    {% endfor %}
            
                
                {% with <присваивания_разделенные_пробелами> %}<content>{% endwidth %}
                #может исп для временного хранения вычисленого val(напр обращение к attr класса) в v, чтобы не считать его снова
                #присваивания записываются ~ python
                #examples
                    {% with bb_count = bbs.count %}
                    {% if bb_count > 0 %}
                    <p>Всего {{ bb_count }} объявлении.</p>
                    {% endwith %}
                      
                
                
                
                {% block <block_name> %}...{% endblock %}
                #реализует наследование шаблонов
                #начало объявляемого блока
                #может быть пустым|⊃ содержимое - которое
                    #будет использовано if производный шаблон не задаст для него содержимое
                    #будет заменено if производный шаблон задаст для него содержимое
                
                
                {% filter <filters> %}<content>{% endfilter %}
                #фильтрация <content>
                #?не очень понял синтаксис
                #examples
                    #?что делает
                    {% filter force_escape|upper %}
                    <p>Текст тега filter</p>
                    {% endfilter %}
                
                
                
                {% autoescape on|off %}<content>{% endautoescape %}
                #управляет авто-преобразованием недопустимых HTML chars("><) в ~ спец символы при выводе
                
                
                {% spaceless %}<content>{% endspaceless %}
                #удаление пробельных символов(space,tab,\b,\n)
                #examples
                    {% spaceless %}
                    <h3>
                        <em>Последние объявы</em>
                    </h3>
                    {% endspaceless %}
                
                {% verbatim %}<content>{% endverbatim %}
                #вставка <content> как есть, без обработки:
                    директив
                    тегов
                    фильтров
                #examples
                    {% verbatim %}
                    <p>Текущие время & дата помещаются на страницу тегом {% now %}.</p>
                    {% endverbatim %}
                    



verbatim:eng:?

        ФИЛЬТРЫ
        #поддерживают исп литералов
        #записывается в директивах после v ⊃ val для обработки, с отделением |
        #можно {Xₙ} исп неск фильтров
            {{<v>|<filter>:<val>[|<filter>:<val>[...]]}}
        #преобразуют val из obj в формат указанный после ":" перед выводом
        
            date:<format>
            #форматирование даты & времени ~ <format>
                <format>
                    j       число ⊅ начальныи 0
                    d       число ⊃ начальныи 0
                    n       месяц ⊅ начальныи 0
                    m       месяц ⊃ начальныи 0
                    F|N     полное название месяца в именительном с большои буквы
                    E       полное название месяца в родительном lowercase
                    M       сокращение месяца с большои буквы
                    b       сокращение месяца lowercase
                    Y|o      
            #examples
                #<число>.<номер_месяца>.<год из 4х цифр> <часы в 24ч формате>:<минуты>:<секунды>
                {{ bb.published|date:"d.m.Y H:i:s" }}
            
            
            force_escape
            
            
            upper
        
            lower
            #examples
                {{ bb.content|lower|default:'--описания нет'}}
            
            
            default
            #examples
                {{ bb.content|lower|default:'--описания нет'}}
            

ШАБЛОН
#образец для формирования страницы (напр веб отправляемои посетителю в ответ на его запрос|текстовых документов для отправки по email
#⊃команды шаблонизатора


		
	

РЕНДЕРИНГ ШАБЛОНОВ
#объединение шаблонов & данных

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
#см .render() ⊂ django.shortcuts


ОБРАБОТЧИКИ КОНТЕКСТА
#программныи модуль добавляющии в контекст шаблона v после его формирования контроллером
#указываются в settings.py TEMPLATES OPTIONS['context_processors']
#обработчики контекста доступные в dj
    django.template.context_processors.request
    #add to context v request ⊃ obj текущего запроса(экз Request)
    
    django.template.context_processors.csrf
    #add to context v csrf_token ⊃ электронныи жетон использующиися тегом шаблонизатора csrf_token
    
    django.contrib.auth.context_processors.auth
    #add to context v user ⊃ текущии user & perms ⊃ права текущего user'а
    
    django.template.context_processors.static
    #add to context v MEDIA_URL ⊃ val одноименного параметра project
    
    django.contrib.messages.context_processors.messages
    #add to context v messages ⊃ lst всплывающих msg & DEFAULT_MESSAGES_LEVELS ⊃ dict сопоставляющии str обозначения уровнеи msgs с их числовыми кодами
    
    django.template.context_processors.tz
    #add to context v TIME_ZONE ⊃ обозначение текущеи tz
    
    django.template.context_processors.debug
    #add to context v
    #исп при отладке
        debug
        #⊃ val project param DEBUG
        
        sql_queries
        #⊃ данные о запросах к бд выполненных ПРИ ОБРАБОТКЕ ЗАПРОСА
        #lst ⊃ dicts - ∀ dict - представляет один запрос, {'sql':<код_запроса>,'time':<execution_time>} 


context ~ контекст ~ контекст шаблона

БИБЛИОТЕКА ТЕГОВ
#модуль python расширяющая набор доступных тегов шаблонизатора
    ВСТРАИВАЕМАЯ БИБЛИОТЕКА ТЕГОВ
    #загружается в mem при запуске проекта -> ее теги доступны ∀
    #⊂ ядру dj
    
    ЗАГРУЖАЕМАЯ БИБЛИОТЕКА ТЕГОВ
    #в Δ от встраиваемои перед исп должна быть явно загружена с исп тега:
        load <lib_alias>
СОКРАЩЕНИЯ
#сокращение(~fx-сокращения ~ shortcuts) - fx exe неск деиствии
#предназначена для exe типичных задач
#сокращает V работы
#⊂ django.shortcuts
#high-level средства
    
    django.shortcuts
    
            .render(request, <template_path>:<str> [,context=None][, content_type=None][, status=200])
            #exe рендеринг шаблона & отправку результата клиенту в одном exp
                request
                #экз HttpRequest(?|Request)
                context:<dict>
                #подготовленный контекст шаблона(данных)
                content_type
                #MIME-type ответа & кодировку
                    content_type=None
                    #ответ получит MIME-type text/html и кодировку ⊂ DEFAULT_CHARSET
                status
                #int code response status
            #возвращает строку с HTML готовой страницы(?|экз HttpResponse)
            #examples
                from django.shortcuts import render
                from .models import Bb
                ...
                def index(request):
                    bbs = Bb.objects.order_by('-published')
                    return render(request, 'bboard/index.html', {'bbs': bbs})
            
            
            .redirect(<target>, [, permanent=False][, <val_url_params>])
            #формирует uri для redirect & exe его
                <target>
                #
                    <Model_obj>
                    #тогда uri будет получен от <Model>.get_absolute_url()
                    [ns:]<route_name>
                    #с <val_url_params> -> uri будет сформирован обратным разрешением
                    <abs_uri>
                permanent
                #тип перенавравления
                <val_url_params>
                #мб указаны как именованные|позиционные args
            #>> полностью сформированный экз HttpResponseRedirect(а могло быть иначе?)
            #examples
                ...
                    return redirect('bboard:by_rubric', rubric_id=bbf.cleaned_data['rubric'].pk)
            
            
            .get_object_or_404(<source> [,<условия_поиска>])
            #>> запись|бросает Http404 ⊃ django.http
                <source>
                    <Model_obj>
                    #видимо >> uri будет получен от <Model>.get_absolute_url()
                    экз <Manager>
                    #диспетчер записеи
                    экз <QuerySet>
                    #набор записеи
            #if условиям удовл неск записеи бросает MultipleObjectsReturned ⊂ django.core.exceptions
            #examples
                def detail(request, bb_id):
                    bb = get_object_or_404(Bb, pk=bb_id)
                    return HttpResponse(...)
            
            
            .get_list_or_404(<source>, <условия_фильтрации>)
            #>> экз <QuerySet>
            #if ни одна запись не подходит -> бросает Http404 ⊂ django.http
                    <Model_obj>
                    #видимо >> uri будет получен от <Model>.get_absolute_url()
                    экз <Manager>
                    #диспетчер записеи
                    экз <QuerySet>
                    #набор записеи
            #examples
                def by_rubric(request, rubric_id):
                    bbs = get_list_or_404(Bb, rubric=rubric_id)
                    ...
    
            
            
            
ДОПОЛНИТЕЛЬНЫЕ НАСТРОИКИ КОНТРОЛЛЕРОВ
#dj ⊃ декораторы для доп настроики контроллеров
    
    django.views.decorators
        
        ДЕКОРАТОРЫ УСТАНАВЛИВАЮЩИЕ НАБОР ДОПУСТИМЫХ HTTP-МЕТОДОВ
        #при попытке доступа с исп запрещенного метода -> декоратор >> экз HttpResponseNotAllowed
            .http
                
                .require_http_methods(<SEQ_METHODS_NOTATIONS>)
                #запрещает для контроллера остальные методы
                #examples
                    from Django.views.decorators.http import require_http_methods
                    ...
                    @require_http_methods(('GET', 'POST'))
                    def add(request):
                        ...
                request
                
                .require_get()
                #запрещает ∀ методы кроме GET
                
                
                .require_post()
                #запрещает ∀ методы кроме POST
                
                
                .require_safe()
                #запрещает ∀ методы кроме GET и HEAD
                
                
    ДЕКОРАТОРЫ EXE СЖАТИЕ
        
        .gzip
            .gzip_page()
            #сжимает ответ контроллера исп алг GZIP
            #требует поддержки соотв алг браузером



UploadFile
#класс представляющии фаилы переданные в запросе



django.http
    .HttpResponsePermanentRedirect(<target_uri>:<str> [, status=301][, reason=None])
    #производный HttpResponse
    #исп для exe постоянного перенаправления
        #создаем экз HttpResponsePermanentRedirect
        #возвращаем из контроллера-fx
    
        ...
        return HttpResponsePermanentRedirect('http://www.new_address.com/')

    .HttpResponseRedirect(<target_uri>:<str> [, status=302][, reason=None])
    #производный HttpResponse
        <target_uri>
        #полныи|сокращенныи
    #исп для exe временного перенаправления
        #создаем экз HttpResponseRedirect
        #возвращаем из контроллера-fx
            ...
            return HttpResponseRedirect(reverse{'bboard:index'})




    .HttpRequest
    #предоставляет(⊃ данные) клиентский запрос
    #традиционно называется request
    #доступен в контроллере-fx через его первыи параметр
    #attr
        .GET
        #dict ⊃ ∀ GET-параметры ⊂ запросу вида {'GET_param_name':<val>,...}
        .POST
        #~ .GET
        .FILES
        #dict ⊃ ∀ выгруженные фаилы
        #ключи = имена POST-параметров посредством которых передается содержимое фаилов
        #val ключеи - фаилы представленные экземплярами UploadFile
        .method
        #обозначение метода отправки данных в виде UPPERCASE str
            "GET"
            "POST"
            ...
        .scheme
        #обозначение протокола
            "http"
            "https"
        .path
        #путь
        #?Δ .path_info
        .path_info
        #путь
        #?Δ .path
        .encoding
        #обозначение кодировки запроса
            .encoding ⊃ None
            #запрос закодирован в DEFAULT_CHARSET
        .content_type
        #обозначение MIME-типа полученного запроса извлеченное из HTTP-заголовка Content-Type
        .content_params
        #dict ⊃ доп параметры MIME-типа полученного запроса извлеченные из HTTP-заголовка Content-Type
        #keys - имена параметров, val - val параметров
        .META
        #dict ⊃ доп параметры в виде элтов:
            .CONTENT_LENGTH:<str>
            #длинна тела запроса в chars
            .CONTENT_TYPE
            #MIME-тип тела запроса
                "appication/x-www-form-urlencoded"
                "multipart/form-data"
                "text/plain"
            .HTTP_ACCEPT:<str>
            #⊃ перечень поддерживаемых браузером MIME-типов данных
            #comma separated
            .HTTP_ACCEPT_ENCODINGS:<str>
            #⊃ перечень поддерживаемых браузером кодировок
            #comma separated
            .HTTP_ACCEPT_LANGUAGES:<str>
            #⊃ перечень поддерживаемых браузером языков
            #comma separated
            .HTTP_HOST
            #(домен|ip) & порт (if он Δ default) сервера отдавшего страницу
            .HTTP_REFERER
            #uri страницы с которои был exe переход на текущую
            #!∃ if текущая - первая открытая в браузере
            .HTTP_USER_AGENT:<str>
            #⊃ user agent браузера
            .QUERY_STRING:<str>
            #⊃ необработанные GET-параметры
            .REMOTE_ADDR
            #ip клиента
            .REMOTE_HOST:<str>
            #доменное имя клиентского пк
            #if не удалось получить -> ""
            .REMOTE_USER
            #username пользователя exe вход на сервер
            #!∃ if вход не был exe|исп другои способ аутентификации
            .REQEUST_METHOD
            #обозначение метода отправки данных в виде UPPERCASE str
                "GET"
                "POST"
            .SERVER_NAME
            #доменное имя сервера
            .SERVER_PORT:<str>
            #tcp-port
        #может ⊃ & другие элты формируюшиеся на основе ∀ нестандартных заголовков ⊂ запросу клиента,
           его имя uppercase имя заголовка
           с '-' замененными на '_'
           с префиксом "HTTP_"
           #пример
                UPGRADE_INSECURE_REQUESTS -> HTTP_UPGRADE_INSECURE_REQUESTS
        .body:<bytes>
        #raw content запроса
    #методы
        .get_host()
        #>> str ⊃ [ip|домен(if удается получить)] & tcp-port сервера
        .get_port()
        #>> str ⊃ tcp-port сервера
        .get_full_path()
        #>> full path to curr page
        .build_absolute_uri(<path>)
        #строит полныи uri на основе домена|ip и <path>
        #examples
            print(request.build_absolute_uri('/test/url/'))
            >>
                http://localhost:8000/test/uri/
        .is_secure()
        #>> True if обращение исп HTTPS
        #>> False if обращение исп HTTP
        .is_ajax()
        #>> True if это AJAX-запрос
        #>> False if это обычныи запрос
        #AJAX-запросы выявляются dj по ⊂ запросу заголовка HTTP_X_REQUESTED_WITH:"XMLHttpRequest"
    
    
    
    
    
    
    .HttpResponse([<content>:<str>][, content_type=None][, status:<int>=200][,reason:<str>=None("OK")])
    #класс
    #в отличие от например StreamHttpResponse полностью формирует ответ в mem перед отправкои
        #и в отличие от него вроде не подходит для отправки данных в формате != html/text или if V слишком велик(формирование заимет слишком много mem/time)
    #низкоуровневое средство формирования ответа клиенту(исп в этои роли чаще всего)
        content_type
        #MIME-type ответа & кодировку
            content_type=None
            #ответ получит MIME-type text/html и кодировку ⊂ DEFAULT_CHARSET
        status
        #int code response status
            200
            #файл успешно отправлен
        reason
        #str обозначение статуса
    #?класс ответа ⊃
        Атрибуты:
            .content:<bytes>
            #содержимое ответа
            .charset
            #обозначение кодировки
            .status_code:<int>
            #код ответа
            .reason_phrase
            #str обозначение статуса
            .streaming
            #потоковость ответа
            #у HttpResponse всегда возвращает False
                streaming=True
                #ответ - потоковый
                streaming=False
                #ответ - не потоковый
            .closed
            #закрытость ответа
                closed=True
                #ответ закрыт
                closed=False
                #ответ еще не закрыт
        Методы:
            .write(<str>)
            #добавляет str в ответ
            writelines(<seq_str>)
            #добавляет str ⊂ seq без разделителей в ответ
            flush()
            #?принудительно переносит содержимое буфера записи(?) в ответ
            has_header(<header>)
            #>> True if <header> ⊂ ответу else >> False
            setdefault(<header>, <val>)
            #создает в ответе <header> ⊃ <val> if таковой ⊄ ответу
    #поддерживает fx dicts которую можно исп для указания/получения val заголовков
        response['pragma'] = 'no-cache'
        age = response['Age']
        del response['Age']
    #examples
        #простой контроллер исп низкоуровневые средства для создания ответа и выводящего str
            from django.http import HttpResponse
            ...
            def index(request):
                resp = HttpResponse("Здесь будет", content_type='text/plain; charset=utf-8')
                resp.write(' главная')
                resp.writelines((' страница', ' сайта'))
                resp['keywords'] = 'Python, Django'
                return resp
    #при передаче контроллеру по традиции называется request
    #предоставляет ответ клиенту
        .html
        текстовыи фаил
        данные в json
        redirect
        err msg
    #при получении контроллером хранит различные сведения о полученном запросе
        запрашиваемый url
        данные полученные от пользователя
        служебная информация от браузера


ПЕРЕНАПРАВЛЕНИЕ
#отсылка браузеру предписании переити на uri ⊃ ответе
    ВРЕМЕННОЕ ПЕРЕНАПРАВЛЕНИЕ
    #пример
        после добавления объявления перенаправление на страницу ⊃ ∀ объявления
    #для exe временного перенаправления исп HttpResponseRedirect ⊂ django.http производныи HttpResponse
    ПОСТОЯННОЕ ПЕРЕНАПРАВЛЕНИЕ
    #исп при переезде на другои домен
    #(?это так)браузер получив уведомление о постоянном перенаправлении заменяет uri в истории, закладках, etc
    #реализуется HttpResponsePermanentRedirect ⊂ django.http
#см redirect() ⊂ django.shortcuts
    
        
	
	
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

ФОРМЫ

<form>
#создание формы

    ОБЫЧНЫЕ ФОРМЫ
    #
    
    
    ФОРМЫ СВЯЗАННЫЕ С МОДЕЛЯМИ
    #по идее можно добавлять префикс к именам полеи моделеи чтобы можно было просто связать ∀ поля с формои
        
        class Post:
            user_form_title = ...
            user_form_post = ...
            ...
        
            
            
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
	
				



<input>
#кнопка отправки данных



"цифровой жетон"= токен




НАСЛЕДОВАНИЕ ШАБЛОНОВ
#для сокращения кода шаблонов
#упрощение сопровождения
#механизм dj
#~наследованию классов
#базовый шаблон объявляет в себе блоки
	#блоки определяют место в шаблоне для вставки содержимого из производных(по отношению к базовому) шаблонов
	#∀ блок ⊃ уникальное в пределах шаблона имя
#реализуется {% block %}(см ТЕГИ ШАБЛОНИЗАТОРА)
	
	



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
#∀ проект должен ⊃ min одно apps
