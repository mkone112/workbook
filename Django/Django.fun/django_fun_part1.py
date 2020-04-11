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
    проверка что django Установлен
        python -m django --version
    проверка что django запущен
    #вроде нельзф выполнить до запуска virtualenv
        python -c "import django; print(django.get_version())"
    при использовании django в первый раз ->
        первоначальные настройки
            генерация основы проекта django
            #набор настроек для экземпляра django
                настройки
                    проекта
                    бд
                    приложений
                    ...
        перейти в каталог где будет храниться код и выполнить
            django-admin startproject mysite
            создает каталог
                mysite/             #контейнер проекта, название никакак не используется django -> можно переименовать #python модуль
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
        можно использовать все доступные публичные IP адреса(?)
        #полезно при работе с Vagrant или для проверки работы на других машинах в сети
            #0 - сокращение от 0.0.0.0
            python manage.py runserver 0:8000
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
        from django.conf.urls import url    #можно использовать from django.urls import path
        from . import views         #явно текущая директория, подозреваю что сработало бы и import views

        urlpatterns = [
            #views.index - расположение fx, name - видимо url
            url(r'^$', views.index, name='index')    #^$ какой-то якорь для форматирования или вроде того
            #можно использовать path('', views.index, name='index')
            #вроде ^$ это корень(index.html), а ^polls это /polls нихера это re!
            #вроде возвращает None
        ]

    добавим ссылку на polls.urls в главной конфигурации URL'ов
django.conf.urls.include()
#позволяет ссылаться на другие URLconfs
#когда django встречает include() - отсекает любую часть URL-адреса, совпадающую с этой точной и отправляет оставшуюся строку во включенный URLconf для дальнейшей обработки
#для упрощения добавления и воспроизведения адресов - т.к. опросы находятся в их собственном URLconf(polls/urls.py) - их можно поместить в /polls/, /content/polls/ или по любому корневому пути, и приложение все-равно будет работать
    #указание корневого URLconf на модуль polls.urls
    #подключение представления index к URLconf
        mysite/urls.py
            from django.conf.urls import include, url
            from django.contrib import admin

            urlpatterns = [
                #нужно всегда использовать include, кроме admin.site.urls
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
        .path(route, view, kwargs=None, name=None)
        #~django.conf.urls.url из django 1.x

РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
# сложные регулярные выражения могут замедлять производительность -> не стоит полагаться на их широкие возможности
    https://en.wikipedia.org/wiki/Regular_expression
    O'Reilly "Mastering Regular Expression" Jeffrey Friedl

НАСТРОЙКА БД
settings.py
#модуль python с набором переменных хранящих настройки django
    бд по умолчанию sqlite
    для использования другой бд
#содержит комментарии
    чем сгенерирован напр django-admin startproject using Django 2.2.5
    DEBUG = True
    INSTALLED_APPS
    #список всех приложений django активированных в проекте
    #по умолчанию содержит приложения для покрытия основных задач
    #некоторые из них используют min одну таблицу бд => необходимо создать таблицу бд
        django.contrib.admin    #интерфейс админа
        django.contrib.auth     #система авторизации
        django.contrib.contenttypes #фреймвок типод данных
        django.contrib.sessions     #фреймворк сессии
        django.contrib.messages     #фреймворк сообщений
        django.contrib.staticfiles  #фреймворк для работы со статическими файлами
    DATABASES['default']
        ENGINE
        #модуль python для работы с бд(бэкенды) напр:
            django.db.backends.sqlite3
            django.db.backends.postgresql
            django.db.backends.mysql
            django.db.backends.oracle
            ...
        NAME
        #полный абсолютный путь к файлу бд/или имя if бд представлена не файлом(интерфейсом?)

            os.path.join(BASE_DIR, 'db.sqlite3') #создает файл в каталоге проекта
        USER
        #для бд отличных от SQLite
        PASSWORD
        #для бд отличных от SQLite
        HOST
        #для бд отличных от SQLite
    TIME_ZONE\
    #часовой пояс
        пример
            Europe/Moscow
для смены бд по умолчанию
    установить соотв библиотеки
при использовании PostgreSQL|MySQL требуется создать бд
    консоль бд-> 'CREATE DATABASE database_name;'
также необходимо удостовериться что пользователь бд указанный mysite/settings.py имеет права на создание бд
#не нашел пользователя в mysite/settings.py
#это позволяет создать test database которая нужна в 3ей части урока
при использовании SQLite - ничего не нужно создавать заранее -> файл бд создается автоматом при необходимости(запросе?)
Приложения django могут использоваться на разных проектах => можно создать пакет
некоторые приложения используют минимум одну таблицу в бд => их необходимо создать перед использованием
    python manage.py migrate
    #проверяет настройку INSTALLED_APPS и создает все необходимые таблицы в бд указанной в settings.py применяя миграции которые находятся в приложении
    #выводит сообщения для каждой примененной миграции
    можно посмотреть таблицы созданные Django в консоли бд
        PostgreSQL  \dt
        MySQL       SHOW TABLES;
        SQLite      .schema
        Oracle      SELECT TABLE_NAME FROM USER_TABLES
    воизбежания лишних миграция можно закомментировать строки в INSTALLED_APPS перед миграцией

СОЗДАНИЕ МОДЕЛЕЙ
модели - по сути структура бд с дополнительными метаданными
#основной источних данных
#содержит набор полей и поведение хранящихся данных
Django следует принципу DRY - определение моделей в одном месте и автоматическое извлечение данных из них
миграции - часть работы с данными, в отличие от напр Ruby On Rails миграции вынесены из файла моделей и являются просто историей которую django может использовать для изменения бд в соответствии с текущей структурой моделей
#миграции происходят из файлов моделей и представляют собой историю которую django может просмотреть для обновления схемы бд чтобы она соответствовала моделям
для приложения голосования создадим модели
    Question
        #содержит вопрос и дату публикации
    Choice
        #содержит текст ответа и колво голосов
        #каждый obj Choice связан с obj Question
    модели отображаются простыми классами
    #подклассами django.db.models.Model
    polls/models.py
    from django.db import models
    class Question(models.Model):
        #атрибуты отображают поле в таблице бд
        #каждое поле представлено экземпляром класса Field что указывает django тип хранящихся данных
        #CharField - текстовое поле
        #pub_date - название экземпляра Field, поля в машинном формате - используются в коде, а бд использует их как названия колонок
        #первый необязательный arg конструктора класса Field можно использовать для задания отображаемого, удобного для восприятия названия поля - оно используется в некоторых компонентах django и полезно для документирования(используется в паре интроспективных частей Django и дублируется как документация), if название не указано -> django использует машинное название
        #max_length обязательеный arg
        question_text = models.CharField(max_length=200)
        #обязательные arg - используется в схеме бд и при проверке
        pub_date = models.DateTimeField('date published')   #поле даты и времени
    class Choice(models.Model):
        #связь между моделями определяется ForeignKey
        #каждый Choice связан с одним obj Question
        #django поддерживает все основыне типы связей
            #многие-к-одному
            #многие-ко-многим
            #один-к-одному
        question = models.ForeignKey(Question, on_delete = models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
обязательные arg в классах унаследованных от field использутся не только в схеме бд, но и при валидации
АКТИВАЦИЯ МОДЕЛЕЙ
эта небольшая часть кода моделей(см выше) предоставляет django большое кол-во информацции позволяющей django
    создать структуру бд(CREATE TABLE) для приложения
    создать Python API для доступа к данным obj Question и Choice
  но первым делом нужно сообщить что приложение polls установлено
приложения django - "подключаемые" - можно использовать приложение в нескольки project и распространять приложение т.к. они не связаны с конкретным проектом django
    #включаем приложение в проект
    #добавляем ссылку на его класс конфигурации
    mysite/settings.py
    INSTALLED_APPS = [
        #находится в polls/apps.py
        'polls.apps.PollsConfig'
        ...

    ]
теперь django знает что нужно использовать приложение polls
    python manage.py makemigrations polls
    #сообщает django что были внесены изменения в модели и что нужно сохранить их в миграции
        >>
            Migrations for 'polls':
                0001_initial.py
                    - Create model Choice
                    - Create model Question
                    - Add field question to choice
    миграции используются django для сохранения изменений моделей и структуры бд - это просто файлы на диске
    #миграции - то как django хранит изменения в моделях => в схеме бд
    можно изучить миграцию для создания моделей
        polls/migrations/0001_initial.py
        #их не нужно каждый раз проверять, но их формат удобен для чтения если нужно внести в них изменения
migrate
#команда django
#выполняет миграции и автоматом обновляет бд
посмотрим какой sql выполнит эта миграция
    sqlmigrate
    #команда sqlmigrate получает название миграции и возвращает их sql
    #не запускает мигарацию в сис-ма, а просто выводит на экран, чтобы увидеть какой SQL django считает необходимым -> полезно чтобы узнать что собирается делать django| если требуется сценарий sql для дальнейшего изменения
        python manage.py sqlmigrate polls 0001
            #пример для postgresql
            >>
                BEGIN
                --
                --  Create model Choice
                --
                CREATE TABLE "polls_choice" (
                    "id" serial NOT NULL PRIMARY KEY,
                    "choice_text" varchar(200) NOT NULL,
                    "votes" integer NOT NULL
                );
                --
                -- Create model Question
                --
                CREATE TABLE "polls_question" (
                    "id" serial NOT NULL PRIMARY KEY,
                    "question_text" varchar(200) NOT NULL,
                    "pub_date" timestamp with time zone NOT NULL
                );
                --
                -- Add field question to choice
                --
                ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
                ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
                CREATE INDEX "polls_choice_7aa0fa6ee" ON "polls_choice" ("question_id");
                ALTER TABLE "polls_choice"
                    ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
                        FOREIGN KEY ("question_id")
                        REFERENCES  "polls_question" ("id")
                        DEFERRABLE INITIALLY DEFERRED;

                COMMIT;
        полученные запросы зависят от используемой бд
        названия таблиц создаются автоматом из названия приложения и названия модели в нижнем регистре(это можно переопределить) polls_choice
        первичные ключи(ID) добавлены автоматом(можно переопределить)(?246c99a640fbbd72)
        Django добавляет _id к названию внешнего ключа(можно переопределить)
        связь явно определена через FOREIGN KEY constraint, не волнуйтесь о DEFERRABLE - это указание для PostgreSQL не применять ограничения FOREIGN KEY до окончания транзакции
        вывод адаптирован к используемой бд => обрабатываются специфичные для бд типы полей автоматом
            auto_increment                      MySQL
            serial                              PostgreSQL
            integer primary key autoincrement   SQLite
        тоже самое с экранирование полей - "|'
python manage.py check
#проверяет любые проблемы в проекте не далая миграций и не трогая бд
теперь запустим
    python manage.py migrate
    #берет все не примененные миграции и запускает из в бд синхронизируя изменения внесенные в модели с помощью схемы в бд
    для создания таблицы моделей в бд
    >>
        Operations to perform:
            Apply all migrations: admin, auth, contenttypes, polls, sessions
        Running migrations:
            Rendering model states... DONE
            Applying polls.0001_initial... OK
django отслеживает примененные миграции используя таблицу django_migrations в бд
миграции мощны и позволяют со временем менять свои модели по мере разработки проекта без необходимости пересоздания бд - миграции специализируются на обновлении бд realtime без потери данных
вспомним трехэтапное руководство по внесению изменений в модель
    изменение модели(models.py)
    миграция изменений python manage.py makemigrations
    применение изменений в бд python manage.py migrate
причина того что сущ отдельные команды для создания и применения миграций заключаются в том что миграции фиксируются в svn(напр git) и отправляются вместе с приложением => облегчают разработку и могут использоваться другими разработчиками
==========================================выполнил_до_сюда=====
ЗНАКОМСТВО С API
#поиграемся с api django
    python manage.py shell
    #вызов интерактивного интерпритатора python
    #используется вместо ввода python т.к. manage.py устанавливает переменную окружения DJANGO_SETTINGS_MODULE которая дает django путь импорта Python до mysite/settings.py
    попав в оболочку изучите API бд :https://django.fun/docs/django/ru/2.2/topics/db/queries/
        #импорт классов моделей
        from polls.models import Choice, Question
        #в сис-ме пока нет Question's
        Question.objects.all()  >> <QuerySet []>
        #создаем новый Question
        #поддержка тайм зон включена по умолчанию в settings.py
        #Django Ожидает datetime с tzinfo для pub_date >> используй timezone.now() вместо datetime.datetime.now()
        from django.utils import timezone
        q = Question(question_text="What's new?", pub_date=timezone.now())
        #сохраним obj в дб
        q.save()
        #теперь он имеет id
        q.id    >> 1
        #доступ к val полей через атрибуты
        q.question_text >> "What's new?"
        q.pub_date      >> datetime.datetime(...)
        #change values by charging the attributes
        q.question_text "What's up?"
        q.save()
        #objects.all() отображает все объекты в дб
        Question.objects.all() >> <QuerySet [<Question: Question object (1)>]>
    это не полезное представление объекта => исправим
        polls/models.py
            ...
            class Question(models.Model):
                ...
                def __str__(self):
                    return self.question_text

            class Choice(models.Model):
                ...
                def __str__(self):
                    return self.choice_text
представления obj(__str__(?__repr__)) используются во всех автоматически сгенерированных страницах админки Django
Добавим пользовательский метод к модели
        polls/models.py
        import datetime
        from django.utils import timezone   #утитлита django для часовых поясов

        class Question(models.Model):
            ...
            def was_published_recently(self):
                ruturn self.pub_date >= timezone.now() - datetime.timedelta(days=1)
поддержка часовых поясов: https://django.fun/docs/django/ru/2.2/topics/i18n/timezones/

СНОВА ЗАПУСТИМ интерпритатор
    python manage.py shell

        from polls.models import Choice, Question
        #проверяем что __str__ пашет
        Question.objects.all()  >> <QuerySet [<Question: What's up?>]>
        #django предоставляет богатый api для поиска в бд полностью управляемый ключевыми словами
        Question.objects.filter(id=1)   >> <QuerySet [<Question: What's up?>]>
        Question.objects.filter(question_text__startswith='What')   >> <QuerySet [<Question: What's up?>]>
        #получить question за послединй год
        from django.utils import timezone
        current_year = timezone.now().year
        Question.objects.get(pub_date__year=current_year)   >> <Question: What's up?>

        #Запрос НЕСУЩ id
        Question.objects.get(id=2)  >> Err: DoesNotExits: Question matching query does not exits
        #поиск по primary key наиболее частая ситуация, django предоставляет ярлык для извлечения primary-key
        Question.objects.get(pk=1)  >> <Question:What's up?>
        #~
        Quesition.objects.get(id=1) >> <Question:What's up?>
        #проверяем кастомный метод
        q = Question.objects.get(pk=1)
        q.was_published_recently()  >> True
        #передадим Question несколько Choice
        #.create() создает новые Choice
        #Choice obj выполняет INSERT, добавляет choice в набор доступных выборов и возвращает новый Choice obj
        #видимо конструктор класса создающий новые экземппляры
        #django создает набор для хранения "другой стороны" отношения ForeignKey(напр. выбор вопроса) к которой можно получить доступ через API
        q = Question.objects.get(pk=1)
        #Отобразить все choice из набора связанных obj
        q.choice_set.all()
        <QuerySet []>   #пока пусто
        #создадим выборы
        q.choice_set.create(choice_text='Not much', votes = 0)  #мне кажется что votes не обязательны(мы же вроде указали их по default)
        q.choice_set.create(choice_text='Not much', votes = 0)
        c = q.choice_set.create(choice_text='Just hacking again', votes=0)
        #Choice obj имеет api для доступа к связанным Question obj
        c.question  >> <Question: What's up?>
        #И наоборот
        q.choice_set.all()  >> <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
        q.choice_set.count()    >> 3

        #API автоматом отслеживает нужные отношения
        #используй двойные подчеркивания для разделения отношений
        #это работает на любой глубине
        #Найдем все Choice для всех Question чей pub_date в текущем году
        Choice.objects.filter(question__pub_date__year=current_year)    >> <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
        #удалим один из Choice
        c. = q.choice_set.filter(choice_text__startswith='Just hacking')
        c.delete()
дополнительная информация о связях в моделях:Доступ к связанным obj:https://django.fun/docs/django/ru/2.2/ref/models/relations/

как использовать __ для поиска полей через API:Поиск по полям:https://django.fun/docs/django/ru/2.2/topics/db/queries/#field-lookups-intro

полная информация об api бд:справочник по api бд:https://django.fun/docs/django/ru/2.2/topics/db/queries/
Административная часть Django
#создание админки для сотрудников/клиентов для добавления/изменения/удаления контента - утомительно
#django полностью автоматизирует создание интерфейса админа для моделей
СОЗДАНИЕ ПОЛЬЗОВАТЕЛЯ С ПРАВАМИ АДМИНА
    python manage.py createsuperuser
        username: admin
        Email adress: admin@example.com
        pass:...
ЗАПУСК СЕРВЕРА РАЗРАБОТКИ
#сайт админа активирован по умолчанию
    python manage.py runserver
http://127.0.0.1:8000/admin/
#админка
#в зависимости от настроек браузера(не django?) и наличия у django данного языка админка локализована
ПОПРОБУЕМ ВОЙТИ В АДМИНКУ
#отображается несколько типов редактируемого контента
    группы
    пользователи
    #предоставляются django.contrib.auth
django.contgib.auth
#инфраструктура аутентификации
#предоставляет группы и пользователей
ДОБАВЛЕНИЕ СВОЕГО ПРИЛОЖЕНИЯ В АДМИНКУ
#наше приложение голосования еще не отображется в админке
#сообщим админке что у obj Quesition есть интерфейс админа
    polls/admin.py
    from django.contrib import admin
    from .models import Question
    admin.site.register(Question)
#теперь django знает что Question должен отображаться в админке
нажать Question->
    список изменений для вопросов
    #на этой странице отображаются все вопросы в бд, и можно выбрать один из них для изменения
    editing form for question obj
        форма автоматически генерируется из модели Question
        различные типы полей модели










































