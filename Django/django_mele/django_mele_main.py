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