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
	manage.py migrate

