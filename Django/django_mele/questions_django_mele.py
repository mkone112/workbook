как создать собственную модель пользователя?
# https://docs.djangoproject/en/2.0/topics/auth/customizing/#substituting-a-custom-user-model
# позволяет сделать код гибче
# может усложнить интеграцию со сторонними apps взаимодействующими с моделью пользователя
    кроме использования ссылки onetoone, можно полностью заменить модель пользователя
        наследованием от `AbstractUser` реализующего базовые методы пользователя
        