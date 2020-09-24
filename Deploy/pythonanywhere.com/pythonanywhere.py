создать beginer акк
dashboard -> account -> создать api token
#пример исп
	username, token = ...
	requests.get(
		f'https://www.pythonanywhere.com/api/v0/user/{username}/cpu',
		headers={'Authorization': f'Token {token}'}
	)
settings.py
		ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.pythonanywhere.com']
.gitignore
	...
загрузка на github
dashboard -> bash ->
попытка_использовать_pa_autoconfigure_django
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
		py -3.6 manage.py createsuperuser
youtube
	cd ~ && pwd && git clone <path_to_root_project_from_github>
	mkvirtualenv --python=/usr/bin/python3.5 venv
	cd my-first-blog
	pip install -r requirements.txt
	#pip install django
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
	dashboard:mkone112.pythonanywhere.com-> static files -> add ->/static/ /home/mkone112/my-first-blog/static
cd ~/my-first-blog #в dir где на github лежит .git
git pull
перезапуск
ОБНОВЛЕНИЕ STATIC
	#активируем venv
	#~ $ source .virtualenvs/venv/bin/activate
	workon mkone112.pythonanywhere.com
	cd my-first-blog
	python manage.py collectstatic
	