re - regular expression
    ^       начало текста или начало любой строки в мультистроковом режиме
    $       конец текста или конец любой строки в мультистроковом режиме
установка Django
    может требовать дополнительные lib'ы
    с django поставляется простой веб-сервер(включен для мнгновенной разработки без дополнительной настройки боевого сервера(напр Apache)) которые можно заменить на сторонний
    django м.б. запущен на мн-ве платформ поддерживающих WSGI(PEP 3333), Альтернативы:docs-> Развёртывание Django
    для работы с бд потребуется соотв движок:PostgreSQL(рекомендуется), MySQL, SQLite 3, Oracle
    Совместимые версии Python
        1.6         3
        1.8         2.7; 3.2-3.5
        1.9..1.10   2.7; 3.4-3.5
        для каждой версии python официально поддерживается только последний микро-релиз(X.Y.Z)
        обычно поддерживается Ptython срок поддержки которого заканчивается до срока поддержки Django LTS:напр. поддержка python 3.3 завершилась 09.2017 а Django 1.8 LTS 04.2018 -> django 1.8 последняя версия поддерживающая python 3.3
    в начале нового проекта и зависимые lib поддерживают python 3 -> стоит использовать его else: использовать python 2.x | портировать(помочь портировать) эти lib'ы на 3.x
    сторонние приложения django могут иметь свою политику поддержки версий Python
    стабильные версии django содержат api обратно совместимое с пред версиями
    для установки на Jython требуются дополнительные шаги
        ...
    HOW TO INSTALL DJANGO ON WINDOWS
        3.5, also provide instruction for installing virtualenv and virtualenvwrapper
        для пользователей django, а не его разработчиков
        python --version    >> 3.5.3
        virtualenv and virtualenvwrapper provide a dedicated environment for each Django project
        #необязательны, но best practice
        pip install virtualenvwrapper-win
        set http(s)_proxy=http(s)://username:password@proxyserver:proxyport
        #if connected to the internet behind a proxy
        mkvirtualenv myproject  >> "(myproject)"
        #create virtual env for project, virtualenv активируется автоматически
        workon myproject
        #возобновление работы при перезапуске консоли
        pip install django
        # download and install latest django release
        django-admin --version
        #verify correct install, and view version
        #if only displays the hep => problem with file association in Win => check PATH(if several python version installed)
при проблемах с кодировкой: pc-name должно быть на латинице без спец символов
СОЗДАНИЕ ПЕРВОГО ПРИЛОЖЕНИЯ
создадим проект состоящий из простого приложения для голосования из двух частей
    Публичный сайт: отображает пользователям голосования и позволяет голосовать
    Интерфейс админа: добавление, изменение и удаление голосований
    проверка что django запущен
    #вроде нельзф выполнить до запуска virtualenv
        python -c "import django; print(django.get_version())"
    при использовании django в первый раз ->
        первоначальные настройки
            генерация основы проекта django
                настройки
                    проекта
                    бд
                    приложений
                    ...
        перейти в каталог где будет храниться код и выполнить
            django-admin startproject mysite
            создает каталог
                mysite/             #контейнер проекта, название никакак не используется django -> можно переименовать
                    manage.py   #скрипт для взаимодействия в проектом Django
                    db.sqlite3  #файл бд
                    mysite/     #Python пакет проекта, имя используется для импорта чего-либо из проекта, напр mysite.urls
                        __init__.py #пустой файл указывающий python что текущий каталог - проект
                        settings.py #настройки/конфигурация проекта django
                        urls.py     #конфигурация url'ов проекта, "содержание" всех django сайтов
                        wsgi.py     #точка входа проекта для wsgi-совместимых веб-серверов
        название проекта не должно конфликтовать с именами модулей python(включая django)
        не стоит размещать файлы проекта в корневом каталоге как например в PHP напр /var/www т.к. есть риск что он будет доступен для просмотра => не безопасно
        должно быть размещено в каталоге вне корневой директории сайта, например /home/mycode
        python manage.py runserver
        #запускает простой web-сервер для разработки написанный на python,
            >> Performing system check...
               System check identified no issues (0 silenced).
               You have unapplied migrations: your app may not work properly until they are applied.
               Run 'python manage.py migrate' to apply them.
               <data>
               Django version <version>, using settings 'mysite.settings'
               Starting development server at http://127.0.0.1:8000/
        #порт по умолчанию 8000, адрес 127.0.0.1
        #скрипт явно перед аргументы из sys.args
            python manage.py runserver <port>   #установка порта
            python manage.py runserver <address>:<port>
                127.0.0.1:8080
        С предупреждением о невыполненных миграция - разберемся позже
        НИКОГДА не используй встроенный веб-сервер django на живом сайте - создан исключительно для разработки, разработчики django умеют писать web-framework'и , но не web-сервера
        dev-сервер автоматом перезагружается при изменении python файлов, однако не перезагружается при добавлении файлов
        при добавлении файлов -> требуется перезагрузить сервер(видимо остановить и запустить)
СОЗДАНИЕ ПРИЛОЖЕНИЯ POLLS
т.к. окружение создано -> приступаем к работе
каждое приложение django состоит из пакета Python следующего соглашениям, django создает структуру приложения сам
приложение = web-приложение предоставляющее определенный функционал напр. блог
проект = совокупность приложений и конфигурации сайта
проект может СОДЕРЖ несколько приложений
приложение может использоваться несколькими проектами
приложение может находиться где-угодно в путях Python
в учебники мы будем создавать приложение рядом с manage.py, и оно будет импортировано как независимый модуль, а не подмодуль mysite(будет находится вне пакета)
    python manage.py startapp polls         #polls название приложения
    #создает дерево каталогов - части приложения
        polls/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            views.py
polls - опрос, голосование
СОЗДАЕМ ПЕРВОЕ ПРЕДСТАВЛЕНИЕ
    polls/views.py
        from django.http import HttpResponse

        def index(request):
            return HttpResponce('Hello, world')
    чтобы вызвать представление нужно назначить его на url -> добавим функцию view index в настройки url'ов
    создадим urls.py в каталоге приложения
    polls/urls.py
        from django.conf.urls import url
        from . import views         #явно текущая директория, подозреваю что сработало бы и import views

        urlpatterns = [
            #views.index - расположение fx, name - видимо url
            url(r'^$', views.index, name='index')    #^$ какой-то якорь для форматирования или вроде того
            #возможно нужно использовать path('', views.index, name='index')
            #вроде ^$ это корень(index.html), а ^polls это /polls нихера это re!
            #вроде возвращает None
        ]
    добавим ссылку на polls.urls в главной конфигурации URL'ов
        mysite/urls.py
            from django.conf.urls import include, url
            from django.contrib import admin

            urlpatterns = [
                url(r'^polls/', include('polls.urls')),
                url(r'^admin/', admin.site.urls)            #if получилось include(admin.site.urls)(автор несет херню) вместо admin.site.urls -> возможно версия django не соответствует учебнику, например версия устаревшая
                # странно, я думал что этот файл нужно редактировать вручную(да так и есть), возможно он генерится сам(нихера)
                # ^ поиск в начале
            ]
django
#пакет фреймворка
    .conf
        .urls
            .url(regex, view, kwargs=None, name=None)
            #django 1.x only, ~ django.urls.path 2.x # пиздежь
            #regex - regular expression - шаблон для распознавания строк (в данном случае url'ов), django начинает с первой регулярки и идет по списку сравнивая запрошенный url c каждой регуляркой до совпадения, регулярки не проверяют GET|POST аргументы или доменное имя например:
                # при запросе https://www.example.com/myapp/ проверяется тольк myapp/
                # при запросе https://www.example.com/myapp/?page=3 так же проверяется только myapp/
                для регулярок можно использовать модуль re
            #эти регулярные выражения компилируются при первом импорте модуля с конфигурацей url'ов => работают очень быстро(пока достаточно просты)
            #view
                #когда django находит подходящее re -> вызывает указанную fx представления передавая первым аргументом obj HttpRequest, и все распознанные регулярным выражением значения как остальные аргументы, if re использует простое распознование val - они передаются как позиционные args, if используется именованное распознавание - val передаются как именованные args
            #kwargs
                #в представление можно передать переопределенные именованные args
                #возможность не используется в djbook
            #name
                #добавив имя url-у - можно обращаться к нему из любой точки проекта(особенно шаблонов) - такой подход позволяет делать глобальные изменения в настройках url'ов меняя минимум файлов
    .urls
        .path()
        #~django.conf.urls.url из django 1.x
РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
# сложные регулярные выражения могут замедлять производительность -> не стоит полагаться на их широкие возможности
    https://en.wikipedia.org/wiki/Regular_expression
    O'Reilly "Mastering Regular Expression" Jeffrey Friedl

НАСТРОЙКА БД
