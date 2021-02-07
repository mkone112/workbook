подсисма уведомлений django.contrib.messages позволяет отображать одноразовые msgs
промежуточный слой
    django.contrib.messages.middleware.MessageMiddleware
#предоставляет простой механизм отправления уведомлений пользователям
    # by def - хранятся в cookies и отображаются при последующем запросе пользователя
#es:
    from django.contrib import messages
    ...
    # приклепляем('отправляем') уведомление
    messages.error(request, 'Something went wrong')
#типы msgs:
    success()
    #успешное завершение действия
    
    info()
    #
    
    warning()
    #не критичная err
    
    error()
    #действие не завершилось|произошла err
    
    debug()
    #видимо работает только с settings.DEBUG = True
#настраивается для всего project -> можно легко использовать в любом app


система сообщений автоматически подключает `django.contrib.messages.context_processor.messages` добавляющий переменную `messages` в контекст шаблона
    активированные контекстные процессоры задаются в settings.TEMPLATES[<n>]['OPTIONS']['context_processors']

v `messages` мб использована для отображения ВСЕХ СУЩ уведомлений для конкретного user
# подробнее о django messages `https://docs.djangoproject.com/en/2.0/ref/contrib/messages`

dj позволяет аутентифицировать users использую разл ресурсы
    django.contib.auth.backends.ModelBackend
    #аутентифицирует users исп модель из django.conrib.auth
        #подходит для большинства projects
можно создать свой бекенд аутентификации для добавления новых способов аутентификации
#https://docs.djangoproject.com/en/2.0.topics/auth/customizing/#other-authentication-sources
    напр
        через LDAP
#достаточно создать класс имеющий
    authenticate(request|None, <user_data>) -> User|None
    get_user(ID) -> User
при использовании authenticate() dj пробует применить бекэнды последовательно


стоит добавлять индексы(db_index=True) для полуй часто использующих filter(), exclude(), order_by()...
    для полей с unique=True и ForeignKey - индексы создаются автоматом

ОПРЕДЕЛЕНИЕ СОСТАВНОГО ИНДЕКСА
    Meta.index_together


при определение ManyToMany dj создает промежуточную таблицу с pk objs связанных моделей, поле ManyToMany может быть определено в ЛЮБОЙ из них
    related_name как обычно создает медеджер отношений


Form.clean_<field> вызываются при .is_valid()



Букмарклет - сохраненные в браузере закладки изображений, реализован на js ,  расширяет функциональность браузера
# при нажатии на закладку -> exe js что позволяет работать с содержимым любого сайта - полезная возможность для создания инструментвов взаимодействующих с другими сайтами, напр Pinterest реализует букмарклет для шаринга контента на другие платформы.
    Алгоритм:
        User сохраняет uri моего сайта в закладках, uri содержит js-код в attr href
        User переходит на ДРУГОЙ сайт и кликает на закладку -> сохраненный js начинает exe
    т.к. js в закладке - его не изменить после сохранения -> можно обойти добавив fx обновления exe кода букмарклета, пользователи будут сохранять именно его и можно модифицировать код букмарлета в любое время. При exe кода из закладки будет скачиваться актуальная версия букмарклета.

Букмарклет мб загружен на ЛЮБОЙ сайт ВКЛЮЧАЯ использующие HTTPS, из соображений безопасности браузер предотвращает загрузку букмарклета по протоколу http на сайте использующем https.

сервер разработки dj предназначен только для разработки и не поддерживает https

sorl-thumbnail
    {% thubmbnail %}
    # генерация превью в шаблонах

require_POST, required_GET, require_http_methods(...)


Для AJAX-запросов обычно не используется добавление CSRF-токена в данные КАЖД запроса, вместо этого dj позволяет указать кастомный HTTP-header `X-CSRFToken: <token>` что позволяет работать с async запросами от ЛЮБЫХ js-libs
# ДОБАВЛЕНИЕ ТОКЕНОВ В ASYNC ЗАПРОСЫ
    получить CSRF-token из csrftoken задающийся if в настройках активирована защита от csrf(по идее by def)
    добавить его к заголовкам
    #details: docs.djangoproject.com/en/2.2/ref/csrf/#ajax
    
Когда пользователь нажимает ссылку like/unlike на стороне браузера нужно
    отправить AJAX-запрос с id(image-id) и action
    if получен успешный ответ(видимо {"status": "ok"})    


ОГРАНИЧЕНИЕ НА ПРИНЯТИЕ ТОЛЬКО AJAX-ЗАПРОСОВ AJAX-VIEWS
    
    request.is_ajax()
    #проверяет сделан ли запрос с помощью XMLHttpRequest

XMLHttpRequest
# exe async requests

ПОСТРАНИЧНЫЙ ВЫВОД С AJAX
#при прокрутке до конца -> подгружаем след страницу
    создадим view для постраничного вывода
    #должен обрабатывать и sync и async запросы -> мб получать изображения без js
        при первом запросе get -> первые 8 imgs


ОТСЛЕЖИВАНИЕ ДЕЙСТВИЙ ПОЛЬЗОВАТЕЛЕЙ
    реализуем
        сисму подписок
            пользователи смогут подписываться друг на друга и просматривать активность друзей
        ленту новостей
        используем signals
        подключим redis
        оптимизация запросов для связанных objs        

ПРИЧИНЫ ИСПОЛЬЗОВАНИЯ ПРОМЕЖУТОЧНОЙ МОДЕЛИ
    сложность модификации одной из моделей(например встроейнной User)
    нужна доп информация об отношении
    

ОГРАНИЧЕНИЯ ПРОМЕЖУТОЧНОЙ МОДЕЛИ
    неработает часть методов менеджеров
        add()
        create()
        remvoe()
        ...
        # -> требуется явно удалять obj промежуточной модели

ЗАДАНИЕ КАНОНИЧЕСКИХ URLS МОДЕЛЕЙ
    либо get_user_model
    
    # by def={}
    ABSOLUTE_URL_OVERRIDES = {
        'app_label.model_name': lambda o: f'/blog/{o.slug}/'
    }
    #dj динамически добавляет .get_absolute_url для каждой модели перечисленной в dict(по умолчанию модель его не имеет) -> и им после этого мб пользоваться

user.get_full_name() -> f'{self.first_name} {self.last_name}'


{% include ... with v=val %}

создадим модель для сохранения действий пользователя
    для этого добавим поле target, по foreignKey может ссылаться только на одну модель
        используем ПОДСИСТЕМУ ТИПОВ СОДЕРЖИМОГО


django.contrib.contenttypes
# предоставляет обобщенный интерфейс ко всем моделям проекта
# используется другими apps ПРИНАДЛЕЖ django.contrib
    подсис-мой аутентификации
    админкой
    
    .models
    
        .ContentType
        # модель чьи объекты содержат сведения о моделях проекта
        # автоматом создает новые экземпляры при создании моделей
            app_label
            # имя модели, берется из Meta модели
            model
            # название класса модели
            name
            # человекочитаемое имя модели
            # берется из Meta.verbose_name
            
            .model_class()
            #получить класс модели
            
            .save
            
            .name
            
            natural_key
            
            objects
            #orm
                .get_for_model(model)
                # получить тип для модели
            id
            
            logentry_set
            
            model
            
            save_base
            
            serializable_value
            
            unique_error_message
            
            validate_unique
            
            refresh_from_db
            
            id
            
            get_deffered_fields
            
            get_object_for_this_type
            
            check
            
            clean
            
            clean_fields
            
            date_error_message
            
            delete
            
            get_all_objects_for_this_type

ДОБАВЛЕНИЕ ОБОБЩЕННЫХ ОТНОШЕНИЙ
# в обобщенных связях ContentType - посредник между моделями
    добавляем поля в модель
        ForeignKey на ContentType
        #указывает на модель связанной с текущей
        поле с id связанного obj
        #обычно PositiveIntegerField для id автоматом созданных dj
        поле для определения свзяи и управления ей
        #обращается к ForeignKey на ContentType и полем с id связанного obj
        # обычно GenericForeignKey