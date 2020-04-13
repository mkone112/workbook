server(serve-облуживание)
submarinacablemap.com - карта подводных кабелей
cli(command line interface)/prompt - текстовое приложение
whoami  >> user name
pwd
#print working directory
#работает в ps
cd
#Без параметров ~ pwd
#change directory
powershell поддерживает кучу unix команд
rm
#
    #удалить файл
        rm
    #удалить каталог
        rm -r
mv
#перемещение файлов
    mv <currentPath> <newPath>
mkdir
#Unix|Win
rmdir
#удаление файла Win
del
#удаление win
copy
#копирование файла win
    copy <currentPath> <newPath>
cp
#копирование файлов Unix
python появился в конце 80x
dfn
#менеджер пакетов fedora
zypper
#менеджер пакетов openSUSE
%HomePath%
#домашняя dir
CLOUDS IDE
    https://paiza.cloud/
    https://aws.amazon.com/cloud9/
python3.8-venv
#пакет venv
venv
#набор файлов
СОЗДАНИЕ VENV
    cd dj
    python3.8-venv -mvenv myvenv
    #py -3.7 -m venv venv
    source myvenv/bin/activate #активация
	#myvenv/scripts/activate
    pip install <packets>~=2.2.4
  UBUNTU
  #может требовать
    virtualenv --python=python3.6 myvenv
pythonanywhere.com
#связан с публикацией(деплоем)
#сервис для запуска Python-кода в облаке
#создать аккаунт уровня beginer
    python/bash/mysql consoles 2
    no ssh
    доступ на сторонние ресурсы:ограничен и http(s) only
    scheduled tasks  1 daily task
    no always on tasks
    ограничения на cpu/mem
#пароль:djangogirls
#url блога имеет вид: username.pythonanywhere.com
#создание API токена:dashboard=>account=>
#хранится в $API_TOKEN
#ПРИМЕР ИСПОЛЬЗОВАНИЯ
    import requests
    username = 'mkone112'
    token = 'ad7ad16d07988428944e95401ac70585bb425080'

    response = requests.get(
      'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
          username=username
      ),
      headers={'Authorization': 'Token {token}'.format(token=token)}
    )
    if response.status_code == 200:
      print('CPU quota info:')
      print(response.content)
    else:
      print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
имя venv
#короткое
#строчное
#без пробелов
АКТИВАЦИЯ venv
win
myvenv\Scripts\activate
#~
#. myvenv/bin/activate
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned >> A
linux
    source myvenv/bin/activate
    #~
    #. myvenv/bin/activate
включение global-site-packages устанавливается в конфиге
в venv команда python будет авмоматически обращаться к правильной версии
pip install --upgrade pip
УСТАНОВКА LIB ЧЕРЕЗ УКАЗАНИЕ ТРЕБОВАНИЙ
requirements.txt
#файл с требованиями хранит список зависимостей которые нужно установить pip
#создается в папке проекта
djangogirls/requirements.txt
    Django~=2.2.4
pip install -r requirements.txt
ИСПРАВЛЕНИЕ УСТАНОВКИ PIP в virtualenv
    python -m pip install -U --force-reinstall pip
git-scm.com
#таки офф сайт
УСТАНОВКА GIT
    Adjusting your PATH env >> Use Git & optional Unix tools from win prompt
    Checkout Windows-style, commit Unix-style line endings
Mechanize, BeautifulSoup, pycrypto
#libs
ФРЕЙМВОРК
#набор готовых компонентов(шаблонов)
django
 способ аутентификации пользователей
    вход
    выход
    регистрация

 панель управления сайтом
 формы
 инструменты для загрузки файлов
 url(Uniform Resource Locator - единый указатель ресурсов)
 resolver(распознаватель)
сервер слушает порт на наличие запросов
    запрос адресуется Django
        urlresolver
        #сопоставляет url со списком шаблонов последовательно
		#переправляет совпадение view
		view выполняет работу, генерит ответ
			django возвращает результат отправителю
venv использует абсолютные пути => нуждается в пересоздании при перемещении проекта(конечно можно и отредактировать файлы)
СОЗДАНИЕ БЛОГА
запустим несколько стандарных скриптов django создающих скелет проекта
создание проекта
	django-admin
		startproject <projectName> <directory>
		#создание проекта
			#установка Django в текущем(.) каталоге
			django-admin startproject mysite .
СТРУКТУРА
	djangogirls
		manage.py
		mysite
			settings.py
			urls.py
			wsgi.py
			__init__.py
		requirements.txt
		venv
ИЗМЕНЯЕМ НАСТРОЙКИ
	часовые пояса обозначаются как регион/город
		Europe/Paris
		...
		#возможно есть и другие форматы поддерживаемые django
	LANGUAGE_CODE  = 'язык-страна'
	#РАСПОЛОЖЕНИЕ СТАТИЧЕСКИХ ФАЙЛОВ
	STATIC_URL = ...
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	ALLOWED_HOSTS
if DEBUG = TRUE и ALLOWED_HOSTS = [] => имя хоста сверяется с ['localhost', '127.0.0.1','[::1]']
		ни одно из этих val не соотв имени хоста на PythonAnywhere
			ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
chromebook:
	settings.py
		MANAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
НАСТРОЙКА БД
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
	}
}
СОЗДАНИЕ БД
	python manage.py migrate
ЗАПУСК СЕРВЕРА
при ошибке UnicodeDecodeError: python manage.py runserver 0:8000
стоит добавить localhost в allowedhosts
МОДЕЛИ DJANGO
	ООП - моделирование объектов с указанием их взаимодейсвий
	obj - поведение + св-ва
mood - настроение
purr - мурчать
scratch - царапать
ОПИСАНИЕ ЗАПИСИ
	title
	text
	author
	created_date
	published_date
	.publish
модели хранятся в бд
python manage.py startapp blog
	djangogirls
		blog
			__init__.py
			admin.py
			apps.py
			migrations
				__init__.py
			models.py
			tests.py
			views.py
settings.py
	INSTALLED_APPS += ['blog']
blog/models.py
	from django.conf import settings	#для AUTH_USER_MODEL
	from django.db import models
	from django.utils import timezone	#видно для получения fx возвращающей текущую datetime в UTC

	class Post(models.Model):	#теперь Post - модель Django и dj сохранит его в бд
		author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
		title = models.CharField(max_length=200)
		text = models.TextField()
		created_date = models.DateTimeField(default=timezone.now)
		published_date = models.DateTimeField(blank=True, null=True)

		def publish(self):
			self.published_date = timezone.now()
			self.save()

		def __str__(self):
			return self.title

dunder( from double underscore)
ТИПЫ ПОЛЕЙ
	models
		.CharField(max_length=<int>)
		#текстовое поле с ограниченным числом символов
		.TextField()
		#текстовое поле без ограничений на число символов(выглядит как уязвимость)
		.DateTimeField([default=<datetime>, blank=<bool>, null=<bool>)
		#datetime
		.ForeignKey(<model>,on_delete)
		#ссылка на другую модель
ДОБАВЛЕНИЕ МОДЕЛЕЙ В БД
#dj берет модели из бд
	#создание файлов миграций
	python manage.py makemigrations blog
	#первая миграция походу имеет attr initial = True
	МИГРАЦИЯ
		py manage.py migrate blog
АДМИНИСТРИРОВАНИЕ DJ
#регистрируем модель в админке
blog/admin.py

	from django.contrib import admin
	from .models import Post

	admin.site.register(Post)
py manage.py createsuperuser
	admin
	mkone112@gmail.com
	pass:a
static в том числе для админки хранятся в соотв папке
можно создавать пользователей без перезагрузки
СОЗДАНИЕ ЗАПИСЕЙ
#пара записей(дата публикации потребуется позже)
ДЕПЛОЙ(развертывание/публикация)
	git config --global user.name #отдельные настройки для конкретного репозитория
	git config --list #просмотреть конфиг
	git init
НАСТРОЙКА .gitignore
		.gitignore
			*.pyc
			*~
			__pycache__
			myenv		#не уверен что это правильное указание директории
			db.sqlite3	#Т.к. будет заменена
			/static
			.DS_Store	#?
MySQL выдерживает большие нагрузки чем SQLite
	git status
	#возвращает информацию о ВСЕХ ранее
		неотслеживаемых
		изменненных
		добавленных
		#в git файлах, и
			статус ветки
	git add --all
	git commit -m "ititial"
ЗАГРУЗКА НА GITHUB
	создаем репозиторий
		name:my-first-blog
		initialize with Readme:no
		Add .gitignore:no
		Add a license:no
	копируем ссылку на репозиторий
СВЯЗЫВАНИЕ ЛОКАЛЬНОГО РЕПОЗИТОРИЯ С GITHUB
	git remote add origin <link_to_github.git>
	git push -u origin master
РАЗМЕЩЕНИЕ НА PYTHONANYWHERE.COM
dashboard=>bash консоль
попытка_использовать_pa_autoconfigure_django==============================================
	загрузка кода на pythonanywhere и его настройка для распознования кода и запуска web-приложения
		pwd
		git clone <path_to_root_project_from_github>
		mkvirtualenv --python=/usr/bin/python3.5 venv
		#установка программы помощника
		cd my-first-blog
		pip install -r requirements.txt
		cd ..
		pip install django virtualenvwrapper
		manage.py -> #!/usr/bin/env python3.6
		pip install --user pythonanywhere #без --user
		#ее запуск
		pa_autoconfigure_django.py https://github.com/mkone112/my-first-blog.git --nuke --python=3.5
		#выполняет классические шаги деплоя
			#скачивает код с github
			#создает virtenv на PythonAnywhere
			#обновляет файл настроек с настройками деплоя
			#создает бд на pythonanywhere используя manage.py migrate
			#разбирается со static файлами
			#настраивает pythonanywhere так чтобы приложение было доступно в интернете
py manage.py migrate
#передает аргумент (migrate) в django который затем решает как с ним поступать
пользователи хранятся в бд => при пересоздании бд требуется снова создавать superuser
py -3.6 manage.py createsuperuser
/попытка_использовать_pa_autoconfigure_django==============================================

youtube#################################################################################
cd ~
pwd
git clone <path_to_root_project_from_github>
mkvirtualenv --python=/usr/bin/python3.5 venv
cd my-first-blog
pip install -r requirements.txt
pip install django
cd ..
dashboard->web->add new web app
	manual
		python 3.5
			конфигурация -> virtual env: venv(путь_до_приложения добавится автоматом)(blog/.virtualenvs/venv)
            Code:
                /var/www/mkone112_pythonanywhere_com_wsgi.py
                    import os
                    import sys
                    #
                    ## assuming your django settings file is at '/home/mkone112/mysite/mysite/settings.py'
                    ## and your manage.py is is at '/home/mkone112/mysite/manage.py'
                    path = '/home/mkone112/my-first-blog'
                    if path not in sys.path:
                        sys.path.append(path)
                    #
                    os.environ['DJANGO_SETTINGS_MODULE'] = 'djangogirls.settings'
                    #
                    ## then:
                    from django.core.wsgi import get_wsgi_application
                    application = get_wsgi_application()
dashboard-> web->reload
/home/mkone112/my-first-blog/djangogirls/settings.py
    ALLOWED_HOSTS = ['mkone112.pythonanywhere.com' ]
    STATIC_ROOT = '/home/mkone112/my-first-blog/static'
~/my-first-blog/$ python manage.py collectstatic
#команда копирует /static/ из приложений в installed_apps
	'''херня
	dashboard->static files-> /media/ : /home/mkone112/my-first-blog/media
							  /static/admin /home/mkone112/.virtualenvs/<env>/lib/python3.5/site-packages/django/contrib/admin/static/admin
	'''херня
dashboard:mkone112.pythonanywhere.com-> static files -> add ->/static/ /home/mkone112/my-first-blog/static

создаем бд
	python manage.py migrate blog
python manage.py migrate
создаем пользователя
	py manage.py createsuperuser
	admin
	mkone112@gmail.com
	pass:a	
СОВЕТЫ ПО БЕЗОПАСНОСТИ:https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
WEB, ERROR LOG -> ошибки	
ОБЩИЕ СОВЕТЫ ПО ОТЛАДКЕ НА PYTHONANYWHERE:http://help.pythonanywhere.com/pages/DebuggingImportError

URL-АДРЕСА DJ
#создаем домашнюю страницу блога
dj использует URLconf
URLconf
#набор шаблонов которые dj сравнивает с полученным url для вызова соотв view(метод для отображения)
djangogirls/djangogirls/urls.py
	...
		#любому адресу начинающимуся с admin ставится в соответствие view -> охватывается большое кол-во различных адресов => растет читаемость
		path('admin/', admin.site.urls) 
	...
docstring в начале
	модуля
	класса
	fx
ПЕРВЫЙ URL DJ
#список записей в home
		djangogirls/djangogirls/urls.py
			from django.contrib import admin
			from django.urls import path, include
			url patterns= [ 
				path('admin/', admin.site.urls),
				path('', include('blog.urls')),
			]
		blog/urls.py
			from django.urls import path
			from . import views
			urlpatterns = [
				path('', views.post_list, name='post_list')
			]
			#'' т.к. для URLconf http://127.0.0.1:8000/|http://localhost:8000 - не часть URL 
			#name - имя url используемое для его идентификации- м.б. таким же как представление|или совершенно иным
			МЫ БУДЕМ ИСПОЛЬЗОВАТЬ ИМЕНОВАННЫЕ URL'S ПОЗЖЕ
ПОПЫТКА ЗАПУСТИТЬ 
	#в django 1.6.4 вывод в браузере
	#в моей версии(~2.2) - выводит в консоль и не отвечает на GET
	module obj has no attr 'post_list'
		request method: GET
		request URL: http://127.0.0.1:8000/
		Django Version: <dj_ver>
		Exception Type: AttributeError
		Exception Value: 'module' object has no...
		Exception Location: <path_to_file>, <line_num>
	#нет соотв view
VIEWS
#логика приложения
#подробнее о представлениях:https://docs.djangoproject.com/en/2.0/topics/http/urls/
blog/views.py
		from django.shortcuts import render
		#запрашивает информацию из модели(ранее созданной) -> передаст в шаблон
		def post_list(request):
			return render(request, 'blog/post_list.html', {})
попытка запуска: templateDoesNotExit
render()
#собирает шаблон			
ВВЕДЕНИЕ В HTML
шаблоны в dj пишутся на HTML(HyperText Markup L...)
гипертекст - тип текста поддерживающий гипер ссылки между страницами
шаблоны хранятся в <app>/templates/<app>
#удобное соглашение об именовании
	blog/templates/blog/post_list.html
теперь корень сайта возвращает пустую страницу
if TemplateDoesNotExists => перезапути сервер
ТЕГИ HTML
	<p>
	#параграф
	вложенность тегов - нельзя закрыть тег пока внутри остаются открытые теги
	<h1>
	#заголовок
	<h2>
	#подзаголовок
	<h3>
	#заголовок 3го уровня
	...
	<h6>
	<em>
	#подчеркнутый текст
	<strong>
	#жирный текст
	<br />
	#переход на следующую строку
	<a href="https://djangogirls.org">link</a>
	<div>
	#раздел страницы
при переходе на localhost|127.0.0.1 ссылки меняются соответственно
DEPLOY
	COMMIT & PUSH В РЕПОЗИТОРИЙ GITHUB
		проверим какие файлы были изменены с последного развертывания
			git status
			git add --all . # '.' текущая директория
git add -all
#выбор всех файлов(включая удаленные(по умолчанию отслеживает только новые/измененные файлы))
git status
#зеленым отмечены файлы готовые к отправке на сервер
git commit -m "Changed the HTML for the site"
git push			

файловый менеджер github автоматом переходит /dirB/ в путях вида /dirA/dirB if dirA пуста
PYTHONANYWHERE->
	cd ~/my-first-blog #в dir где на github лежит .git
	git pull
перезапуск
DJANGO ORM И QuerySet
QuerySet
#список obj заданной модели
#позволяет читать/фильтровать данные из бд и изменять их порядок
#подробнее:https://docs.djangoproject.com/en/1.11/ref/models/querysets/
ИНТЕРАКТИВНАЯ КОНСОЛЬ DJANGO
(myenv) ~/djangogirls$ py manage.py shell
	#импортируем модель
	from blog.models import Post
	#получаем все записи блога
	Post.objects.all()	>> <QuerySet [<Post: my post title>, <Post: another post title>]>
	СОЗДАНИЕ OBJ
	#экземпляры моделей
		from django.contrib.auth.models import User
		#пользователи в бд
		#ранее созданный superuser
		User.objects.all()		>> <QuerySet [<User: ola>]>
		me = User.objects.get(username='ola')
		Post.objects.create(author=me, title='Sample title', text='Test') >> <Post: Sample title>
		Post.objects.all()	>> <QuerySet [<Post: my post title>, <Post: another post title>, <Post: Sample title>]>
	  ПУБЛИКАЦИЯ ПОСТА
		post = Post.objects.get(title="Sample title")
		post.publish()
	Фильтрация obj
	#django ORM использует double underscore для разделения имен полей и операций/фильтров
		Post.objects.filter(author=me)	>> <QuerySet ...>
		Post.objects.filter(title__contains='title') >> <QuerySet ...>
		Post.objects.filter(title_contains='title') >> FieldErr: Cannot resolve keyword title_contains
	  ПОЛУЧИТЬ СПИСОК ВСЕХ ОПУБЛИКОВАННЫХ ЗАПИСЕЙ
		from django.utils import timezone
		#как то странно это работает, я думал что это сравнение с текущей датой - а он выводит все записи у которых есть графа published_date
		Post.objects.filter(published_date__lte=timezone.now())	#по идее LessThanE
	СОРТИРОВКА OBJ
		Post.objects.order_by('created_date')
		#обратный порядок
		Post.objects.order_by('-created_date')
	СОЕДИНЕНИЕ
		Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
ДИНАМИЧЕСКИ ИЗМЕНЯЮЩИЕСЯ ДАННЫЕ В ШАБЛОНАХ		
views соединяют модели и шаблон
	post_list
	#возьмет модели и передаст шаблону
	blog/views.py
		...
		from .models import Post		#. - текущие dir & app
		from django.utils import timezone
		
		...
		#request - все что приходит от пользователя в запросе
		def post_list(request):
			posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
			return render(request, 'blog/post_list', {'posts': posts})	#по сути отвечаем на request
ШАБЛОНЫ DJ
	ТЕГИ ШАБЛОНОВ
	#отображаем шаблон списка записейcd
		ДОБАВЛЯЕМ ТЕГ В ШАБЛОН
			blog/templates/blog/post_list.html
				...
				{{ posts }}
				...
				#django поймет var как список obj
			ЦИКЛ FOR МОЖНО ИСПОЛЬЗОВАТЬ В ШАБЛОНЕ
				{% for post in posts %}
					{{ post }}
				{% endfor %}
				ПЕРЕМЕШАЕМ!
	{{<var> | linebreaksbr}}
	#прогоняет текст через фильтр для преобразования переносов строк в параграфы
					<div>
						<h1><a href="/">Django Girls Blog</a></h1>
					</div>
					
					{% for post in posts %}
						<div>
							<p>published: {{ post.published_date }}</p>
							<h1><a href="">{{ post.title }}</a></h1>
							<p>{{ post.text|linebreaksbr}}
						</div>
					{% endfor %}
МОДЕЛИ СОДЕРЖАТ МН-ВО ИНТЕРЕСНЫХ МЕТОДОВ
	.last
	.intersection
	...
git status
git add --all
git status
git commit -m "Modified templates to display posts from database."
git push
PythonAnywhere ->
	#cd $USER.pythonanywhere.com мне кажется что это не та dir
	git pull
reload
ВСЕ СЛОМАЛОСЬ
	/ возвращает только заголовок => смотрю логи => ничего
		>> бд разные - возвращаемый QuerySet - пуст => цикл не выполняется ни разу
Добавить записи -> проверить изменения
Т.к. я изменял репозиторий на PA - нужно отменить изменения
ПРИНУДИТЕЛЬНАЯ ПЕРЕЗАПИСЬ ЛОКАЛЬНЫХ ФАЙЛОВ
	#неотслеживаемые локальные файлы не будут затронуты
	git fetch
	#загружает последнюю версию из remote не пытаясь что-либо объединить(merge)|синхронизировать(rebase)
	git fetch --all
	git reset
	#назначает главной веткой только что обновленную
		--hard <branch>
		#изменяет ∀ файлы в рабочей ветви в соответствие с указанной
	git reset --hard origin/<branch>	#origin/master
CSS
#эл-ты идентифицируются именами тегов|attr class|attr id
#классы определяют группы элтов, id - конкретные элты
#class можно использовать с id
	<a href="" class="external_link" id="link_to_wiki_page">link</a>
#подробнее о css селекторах:http://www.w3schools.com/cssref/css_selectors.asp	
Boostrap
#один из наиболее популярных HTML&CSS фреймворков
#getbootstrap.com
#написан разработчиками из Twitter
#вроде как просто стягивает стили из инета
#код из файлов читается в порядке их следования -> порядок импортов - имеет val
	blog/templates/blog/post_list.html
		{% load static %}
		<html>
		<head>
			...
			<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
			<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
			<link href="https://fonts.googleapis.com/css?family=Lobster&subset=latin,cyrillic" rel="stylesheet" type="text/css">
			<link rel='stylesheet' href="{% static 'css/blog.css' %}"
		</head>
		<body>
			<div class="page-header">
				<h1><a href="/">Django Girls Blog</a></h1>
			</div>
			<div class="content container">
				<div class="row">
					<div class="col-md-8">
						{% for post in posts %}
							<div class="post">
								<div class="date">
									<p>Опубликовано: {{ post.published_date }}</p>
								</div>
								<h1><a href="">{{ post.title }}</a></h1>
								<p>{{ post.text|linebreaksbr }}</p>
							</div>
						{% endfor %}
					</div>
				</div>
			</div>
		...
СТАТИЧЕСКИЕ ФАЙЛЫ В DJ
#∀ файлы не изменяемые(создаваемые) динамически(html, css, ...)
#содержимое не зависит от контекста запроса и одинаково для ∀ пользователей
#dj ищет папки static внутри ∀(?) dirs приложений
РАСПОЛОЖЕНИЕ
	djangogirls
		blog
			static
			  css
				blog.css
					h1 a { #селектор:∀ <a> ⊂ <h1>
						color: #FCA205;
						font-family: 'Lobster';
					}
					
					body {
						/*padding-left:15px;*/
					}
					#добавим определения блоков для различных селекторов
					#селекторы с . - относятся к классам
					.page-header {
						background-color: #ff9400;
						margin-top: 0;
						padding: 20px 20px 20px 40px;
					}
					
					.page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
						color: #ffffff;
						font-size: 36pt;
						text-decoreation: none;
					}
					
					.content {
						margin-left: 40px;
					}
					
					h1, h2, h3, h4 {
						font-family: 'Lobster', cursive;
					}
					
					.date {
						color: #828282;
					}
					
					.save {
						float: right;
					}
					
					.post-form textarea, .post-form input {
						widht: 100%;
					}
					
					.top-menu, .top-menu:hover, .top-menu:visited {
						color: #ffffff;
						float: right;
						font-size: 26pt;
						margin-right: 20px;
					}
					
					.post {
						margin-bottom: 70px;
					}
					
					.post h1 a, .post h1 a:visited {
						color: #000000;
					} 
РАСШИРЕНИЕ ШАБЛОНА
#можно использовать одни блоки HTML для разных частей приложения
СОЗДАЕМ БАЗОВЫЙ ШАБЛОН
#max общая типовая форма страницы расширяемая для отдельных случаев
blog
	templates
		blog
			base.html
				{% load static %}
				<html>
				<head>
					<title>Django Girls blog</title>
					<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
					<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
					<link href="https://fonts.googleapis.com/css?family=Lobster&subset=latin,cyrillic" rel="stylesheet" type="text/css">
					<link rel="stylesheet" href="{% static 'css/blog.css' %}">
				</head>
				<body>
					<div class="page-header">
						<h1><a href="/">Django Girls Blog</a></h1>
					</div>
					<div class="content container">
						<div class="row">
							<div class="col-md-8">
								<!--создаем block - тег шаблона позволяющий вставить HTML этого блока в другие шаблоны расширяющие base.html
								{% block content %}
								{% endblock %}
							</div>
						</div>
					</div>

				</body>
				</html>
			post_list.html
				{% extends 'blog/base.html' %} #связываем шаблоны друг с другом 
				
				{% block content %}
					{% for post in posts %}
						<div class="post">
							<div class="date">
								{{ post.published_date }}
							</div>
							<h1><a href="">{{ post.title }}</a></h1>
							<p>{{ post.text|linebreaksbr }}</p>
						</div>
					{% endfor %}
				{% endblock %}
РАСШИРЯЕМ ПРИЛОЖЕНИЕ
СОЗДАЕМ СТРАНИЦУ ДЛЯ ОТОБРАЖЕНИЯ КОНКРЕТНОЙ ЗАПИСИ
#используем модель Post
СОЗДАНИЕ ССЫЛКИ НА СТРАНИЦУ ПОСТА В ШАБЛОНЕ
		blog
			templates
				blog
					post_list.html
						...
						<div class="date">
							{{ post.published_date }}
						</div>
						#{% ... %} использование тегов шаблонов dj
						#{% url ... %} создает url(по всей видимости на адрес имеющийся в urls) => потребуется отдельная view
						#'post_detail' - dj ищет url с именем post_detail в blog.urls.py
						#pk -primary(первичный) key
							#dj автоматом создал post.pk для модели Post (каждый пост ⊂ его, по умолчанию val post.pk - int ∃
							#post.pk идентифицирует отдельные записи в блоге ~ получению других полей obj Post(title, author, ...)
							
						<h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
						...
теперь dj возвращает ошибку NoReverseMatch т.к. нет прописанного URL и View для post_detail						
СОЗДАДИМ URL ДЛЯ СТРАНИЦЫ ПОСТА
#чтобы первый пост отображался по localhost/post/1 etc
blog/urls.py
	...
	urlpatterns = [
		path('', views.post_list, name='post_list'),
		#<int: проверка на int
		#'post/<int:pk>/' выражение для сравнения, int преобразуется в var pk
		#pk передается в views.post_detail
		#/ в конце обязателен?
		path('post/<int:pk>/', views.post_detail, name='post_detail'),
	]
		
попробуем получить конкретную запись блога
blog/views.py
	Post.objects.get(pk=pk)
#получаем ошибку для !∃ post
	#localhost/post/10	>> DoesNotExist
используем get_object_or_404
#if !∃ экземпляра Post => возвращаем 404
#можно создать свою страницу 404
blog/views.py
	...
	#мне кажется довольно логичным что get_object_or_404 хранится в .shortcuts
	from django.shortcuts import render, get_object_or_404
	#аргумент вроде должен иметь тоже имя(вообще логично - код читать легче)
	def post_detail(request, pk):
		post = get_object_or_404(Post, pk=pk)
		return render(request, 'blog/post_detail.html', {'post': post})
обновляем => ошибка исчезла
пробуем перейти по ссылке из заголовка записи (localhost/post/30) => TemplateDoesNotExist
#неудивительно => шаблона то нет
blog/templates/blog/post_detail.html
		{% extends 'blog/base.html' %}
		
		{% block content %}
			<div class="post">
				{% if post.published_date %} #срабатывает только if ∃
					<div class="date">
						{{ post.published_date }}
					</div>
				{% endif %}
				<h1>{{ post.title }}</h1>
				<p>{{ post.text|linebreaksbr }}</p>
			</div>
		{% endblock %}
перезапуск => все ок(требуется т.к. при предыдущем были ошибки)
git status => git add --all => git status => git commit -m "Added view and template for detailed blog post as well as CSS for the site." => git push
PA
	cd ~/mkone112.pythonanywhere.com
	git pull
	перезагрузить webapp
ОБНОВИМ STATIC НА PA
#обычно static обрабатывается отлично от исполняемых для оптимизации
#нужно чтобы сервер обновил их
PA
	#активируем virtualenv
	#~ $ source myenv/bin/activate на локальной машине(а в PA сработает?)
	#у меня нихера не работает => ~ $ source .virtualenvs/venv/bin/activate
	workon mkone112.pythonanywhere.com
	#немного похожа на migrate(вносим изменения => применяем их
	cd my-first-blog
	python manage.py collectstatic
	
	
ФОРМЫ В DJ
#удобный способ добавления/редактирования записей
#дают полный контроль над интерфейсом
дизайн админки dj сложно менять
можно создать новую форму | воспользоваться ModelForm для сохранения содержимого формы в модель
СОЗДАДИМ ФОРМУ ДЛЯ МОДЕЛИ Post
blog
	forms.py
		#импортируем формы dj
		from django import forms
		
		from .models import Post
		
		class PostForm(forms.ModelForm):
		
			class Meta:
				#модель используемая для создания формы
				model = Post
				#поле author будет автоматом выбрано в зависимости от авторизованного пользователя
				#created_date должна будет автоматом проставляться
				fields = ('title', 'text',)
СОЗДАЕМ ССЫЛКИ НА СТРАНИЦУ, URL, VIEW И ШАБЛОН
ССЫЛКА НА СТРАНИЦУ С ФОРМОЙ
	blog/templates/blog/base.html
	...
	<div class="page-header">
		#называем новое представление post_new
		#glyphicon gliphicon-plus определен в теме bootstrap - значек плюса
		<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
		...
<span>
#определение строчных эл-тов
#в отличие от блочных эл-тов(<table>,<p>,<div>) можно выделить часть информации внутри другого тега и установить для нее свой стиль	
update -> NoReverseMatch
URL
blog/urls.py
...
	path('post/new/', views.post_new, name='post_new'),
	...
update-> AttributeError
#view post_new еще не реализовано
blog/views.py
	...
	from .forms import PostForm
	...
	def post_new(request):
		#для создания формы отдаем PostForm() в шаблон
		form = PostForm()
		return render(request, 'blog/post_edit.html', {'form': form})
СОЗДАЕМ ШАБЛОН ПОД ФОРМУ
#требуется
	#отобразить форму
		#например
			{{ form.as_p }}
	#строка выше должна быть обернута в <form method="POST"></form>	
		#альтернатива - GET
	#кнопка save
		<button type="submit">Save</button>
	#сразу после открытия <form...> нужно добавить
		{% csrf_token %}
		#делает форму защищенной
		#без этого dj матерится -> Forbidden 403 CSRF vefification failed
blog/templates/blog/post_edit.html
	{% extends 'blog/base.html' %}
	
	{% block content %}
		<h1>New post</h1>
		<form method="POST" class="post-form">{% csrf_token %}
			{{ form.as_p }}
			<button type="submit" class="save btn btn-default">Save</button>
		</form>
	{% endblock %}
update -> форма пашет
СОХРАНЯЕМ ДАННЫЕ ИЗ ФОРМЫ
#на данный момент после отправки формы мы возвращаемся к тому же представлению, но с новыми данными(∀ поля формы) в request(точнее в request.POST)
#метод POST в отличие от GET используется для "публикации" данных
blog/views.py
#требуется обработать два случая
	когда только зашли на страницу -> пустая форма
	возвращаемся к view со ∀ информацией введенной в форму
	
	from django.shortcuts import redirect
	
	
	def post_new(request):
		if request.method == "POST":
		#строим форму с данными из PostForm
			form = PostForm(request.POST)
			#проверяем заполнены ли ∀ необходимые поля и нет ли не валидных val
			if form.is_valid():
				#сохраняем форму
				#commit=False - не сохраняем модель Post(т.к. сначала нужно добавить автора)
				post = form.save(commit=False)
				#добавляем автора
				post.author = request.user
				post.published_date = timezone.now()
				#сохранение(создание) записи
				post.save()
				return redirect('post_detail', pk=post.pk)
		else:
			form = PostForm()
		#переход на страницу записи сразу после создания
		#post_detail - имя view(которое требует pk) post - новая запись
		return render(request, 'blog/post_edit.html', {'form': form})
update-> localhost/post/new -> ∀ пашет(требуется быть залогиненым в админке)
ВАЛИДАЦИЯ ФОРМЫ
#в модели Post не указано что поля title и text необязательны(в отличие от published_date) -> при попытке отправить незаполненную форму рядом с полями будет выведено "This field is required"
ФОРМА РЕДАКТИРОВАНИЯ
blog/templates/blog/post_detail.html
	...
	{% endif %}
	<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}">
	<span class="glyphicon glyphicon-pencil"></span>
	</a>
	<h1>{{ post. title }}</h1>
	...
blog/urls.py
	...
	#передаем pk из url
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	...
blog/views.py
	...
	def post_edit(request, pk):
		#получаем модель для редактирования
		post = get_object_or_404(Post, pk=pk)
		if request.method == "POST":
			#передаем экземпляр post в качестве instance
			form = PostForm(request.POST, instance=post)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.published_date = timezone.now()
				post.save()
				return redirect('post_detail', pk=post.pk)
		else:
			#открываем форму для редактирования
			form = PostForm(instance=post)
		return render(request, 'blog/post_edit.html', {'form': form})
зайти на post_detail и попробовать изменить запись
БЕЗОПАСНОСТЬ
#на данный момент ∀ может редактировать запись
blog/templates/blog/base.html
	...
	{% if user.is_authenticated %}
	<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
	{% endif %}
blog/templates/blog/post_detail.html
	...
	{% if user.is_authenticated %}
		<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
	{% endif %}
