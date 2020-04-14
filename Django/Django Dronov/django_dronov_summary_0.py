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









