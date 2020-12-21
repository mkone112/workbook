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