cd <project_dir> && python3.8-venv -mvenv <venv_dirname> && source <venv_dirname>/bin/activate
#ubuntu может требовать
	virtualenv --python=python3.6 <venv_dirname>
#win
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned >> A
	venv\Scripts\activate
pip install --upgrage pip 
pip install ipython jupyter django-extensions
pip install <packets>~=<ver> | <project>/requirements.txt -> Django~=2.2.4 -> pip install -r requirements.txt
#исправление установки pip в venv	
	python -m pip install -U --force-reinstall pip
django-admin <projectName> <dir> #. для текущего каталога
py manage.py startapp <app>
settings.py
	TIME_ZONE = 'Moscow/'
	LANGUAGE_CODE = '<яз>-<страна>'
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	INSTALLED_APPS += ['<app>', 'django_extensions']
<app>/models.py
	from django.conf import settings
	from django.db import models
	from django.utils import timezone
	
	class Post(models.Model):
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
<app>/admin.py
	from django.contrib import admin
	from .models import Post
	
	admin.site.register(Post)
py manage.py makemigrations && py manage.py migrate
#UnicodeDecodeError -> py manage.py runserver 0:8000
py manage.py createsuperuser
<пакет_конфигурации>/urls.py
	from django.urls import include
	urlpatterns = [
		...
		path('', include('<app>.urls')),
	]
<app>/urls.py
	from django.urls import path
	from . import views
	urlpatterns = [
		path('', views.<view>, name=<view_name>), #name = view_name для удобства
		#<int: - валидатор
		path('post/<int:pk>/', views.post_detail, name='post_detail'),
		path('post/new/', views.post_new, name='post_new'),
		path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	]
<app>/views.py
	from django.shortcuts import render, get_object_or_404, redirect
	from django.utils import timezone
	from .models import Post
	from .forms import PostForm
	def post_list(request):
		posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('published_date')
		return render(request, 'blog/post_list.html', {'posts': posts})	#сборка шаблона
	def post_detail(request, pk):
		post = get_object_or_404(Post, pk=pk)
		return render(request, 'blog/post_detail.html', {'post': post})
	def post_new(request):
		if request.method == "POST":
			#строим форму с данными из PostForm
			form = PostForm(request.POST)
			#проверим заполнены/валидны ли ∀ необходимые поля
			if form.is_valid():
				post = form.save(commit=False)
				#добавляем автора
				post.author = request.user
				post.pulished_date = timezone.now()
				post.save()
				return redirect('post_detail', pk=post.pk)
		return render(request, 'blog/post_edit.html', {'form': PostForm()})
	def post_edit(request, pk):
		post = get_object_or_404(Post, pk=pk)
		if request.method == "POST":
			#передаем экземпляр post как instance
			form = PostForm(request.POST, instance=post)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.published_date = timezone.now()
				post.save()
				return redirect('post_detail', pk=post.pk)
			return render(request, 'blog/post_edit.html', {'form', PostForm(instance=post)})
		
		
		
<app>/templates/<app>/post_list.html
	{% extends '<app>/base.html' %}
	{% block content %}
		{% for post in posts %}
			<div class="post">
				<p>{{ post.published_date }}</p>
				#{% url ... %} тег шаблонизатора создает url (.../post_detail)
				#pk передается в маршрутизатору
				<a href="{% url 'post_detail' pk=post.pk %">{{ post.title }}</a></h1>
				<p>{{ post.text|linebreaksbr }}</p>
			</div>
		{% endfor %}
	{% endblock %}
	
	
	
<app>/templates/<app>/post_detail.html
	{% extends 'blog/base.html' %}
	
	{% block content %}
		<div class="post">
			{% if post.published_date %}
				<div class="date">
					{{ post.published_date }}
				</div>
			{% endif %}
			{% if user.is_authenticated %}
			<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}">post_edit</a>
			{% endif %}
			<h1>{{ post.title }}</h1>
			<p>{{ post.text|linebreaksbr }}</p>
		</div>
	{% endblock %}
	
	
<app>/static/css/blog.css
	...
<app>/templates/<app>/base.html
	{% load static %}
	<html>
	<head>
		<title...
		<bootstap_links...
		<googlefonts_link...
		<link rel="stylesheet" href="{% static '<dir_from_static>' %}>
	<body>
		<div class="page-header">
			{% if user.is_authenticated %}
			<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
			{% endif %}
		<div class="content container"...
			{% block content %}
			{% endblock %}
	...
<app>/forms.py
	from django import forms
	from .models import Post
	class PostForm(forms.ModelForm):
		class Meta:
			#модель исп для создания формы
			model = Post
			#поле author будет автоматом выбрано для авторизованного пользователя
			fields = ('title', 'text',)
<app>/templates/<app>/post_edit.html
	{% extends 'blog/base.html' %}
	{% block content %}
		<h1>New post</h1>
		<form method="POST">{% csrf_token %}
			#отображение формы?
			{{ form.as_p}}
			<button type="submit">Save</button>
		</form>
	{% endblock %}