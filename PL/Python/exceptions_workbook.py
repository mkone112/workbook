py 2.6- позволял исп str в качестве exept
∀ указываи перехватываемые исключения
    # Кроме ImportError перехватит SystemExit, KeyboardInterrupt
        # Породит проблемы, напр сложности с завершением по ^C 
    try:
        import platform_specific_module
    except:
        platform_specific_module = None
    # Для перехвата ∀ исключений исп Exception
        try:
            ...
        except Exception:
            ...
    # Исключения:
        Вывод ∀ ошибок(напр traceback)
        Для exe кода после перехвата exept, и его повторного >> для перехвата в другом месте
        # Обычно лучше исп try...finally

MIN КОДА В БЛОКЕ try...except...finally
    try:
        value = collection[key]
    except KeyError:
        return key_not_found(key)
    else:
        return handle_value(value)
    


BASE EXCEPTIONS

    ImportError
    #
    
    SystemExit
    #
    
    KeyboardInterrupt
    #