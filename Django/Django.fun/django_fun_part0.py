dj - django
джанго был разработан в среде новостного агенства с четким разделением между издателем контента и публичным сайтом, менеджеры сайтов используют сис-му для добавления контента => django решает проблему создания единого интерфейса для админа
позволяет писать веб-приложения быстро
ПРОЕКТИРОВАНИЕ МОДЕЛИ
    dj СОДЕРЖ orm для описания формата бд в виде python-кода
    синтаксис моделей данных СОДЕРЖ мн-во способов представления данных
      mysite/news/models.py
        #походу достаем данные из бд с помощью точечной нотации
        from django.db import models

        class Reporter(models.Model):
            full_name = models.CharField(max_length=70)

            def __str__(self):
                return self.full_name

        class Article(models.Model):
            pub_date = models.DataField()
            headline = models.TextField()
            reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
            def __str__(self):
                return self.headline

комманда migrate ищет все имеющиеся модели и создает на их основе недостающие таблицы в бд
.__str__ 3.x = .__unicode__ 2.X
НАСТРОЙКА БД
автоматическое создание бд
    migrate
    #ищет все имеющиеся модели и создает  на их основе недостающие таблицы в бд
    #при необходимости предоставляет продвинутый контроль над изменениями в структуре данных
    python manage.py migrate
доступен создающийся на лету без предварительной кодогенерации Python API для доступа к данным
    #Import the models we created from our "news" app
    from news.models import Reporter, Article
    #No reporters are in the system yet
    Reporter.objects.all()              >> []
    #Create a new Reporter
    r = Reporter(full_name='John Smith')
    #сохр obj в бд
    r.save()
    #теперь он имеет id
    r.id                                >> 1
    #Просмотреть все экземпляры Reporter
    Reporter.objects.all()              >> [<Reporter: John Smith>]


explicitly  - прямо,непосредственно,точно
НЕ ЗАКОНЧИЛ//

ПРЕДСТАВЛЕНИЕ
#КАЖД представление выполняет одно из двух дейтсвий
    возвращение HttpResponse obj содержащее ответ для запрашиваемой страницы
    #подробнее:HttpResponse:https://django.fun/docs/django/ru/2.2/ref/request-response/#django.http.HttpResponse
    создание исключения вроде Http404
    #подробнее:Http404:https://django.fun/docs/django/ru/2.2/topics/http/views/#django.http.Http404
    все что требует django - HttpResponse|Exeption
    остальное зависить от меня - любые действия с использованием любыйх lib python
        представление может читать записи из бд
        использовать сис-му шаблонов вроде dj или сторонней
        может генерировать pdf
        выводить xml
        создавать zip на лету
#view/вьюха
#контейнер для веб-страниц и другого содержимого
#простая fx(или метод для представлений на основе классов)
#тип веб-страницы в приложении dj обычно
    выполняющая определенную fx
    имеет определенный шаблон
    #ПРИМЕР
        #приложение блога может иметь представления
            домашняя страница           - последние записи
            детализация                 - отдельная страница одной записи
            страница архива по годам    - отображает все месяцы с записями в одном году
            страница архива по месяца   - отображает записи за месяц
            действия с комментариями    - обрабатывает размещение комментариев к записи
django выбирает представление на основе анализа части url после имени домена
в инете можно встретить запросы вида
    «ME2/Sites/dirmod.asp?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B»
django позволяет создавать гораздо более элегантные шаблоны URL
ШАБЛОН URL
#общая форма URL, напр
    /newsarchive/<year>/<month>/
ПАРАМЕТР TEMPLATE
#подробнее:https://django.fun/docs/django/ru/2.2/ref/settings/#std:setting-TEMPLATES
#описывает как django будет загружать и отображать шаблоны
    по умолчанию файл настроек настраивает бэкэнд DjangoTemplates чья опция APP_DIRS=True
    #подробнее:APP_DIRS:https://django.fun/docs/django/ru/2.2/ref/settings/#std:setting-TEMPLATES-APP_DIRS
    по соглашению DjangoTemplates ищет /templates в каждом INSTALLED_APPS