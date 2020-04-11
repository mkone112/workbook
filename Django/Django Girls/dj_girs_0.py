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
dashboard:mkone112.pythonanywhere.com-> static files -> add -> /home/mkone112/my-first-blog/static