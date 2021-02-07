A Foolish Consistency is the Hobgoblin of Little Minds
# Код пишется реже чем читается
PEP8
# Создан для реализации согласованности кода между большим числом проектов
# Описывает согласованность & единство
# Важность согласованности
    # Согласованность с pep8 < согласованность в одном проекте < согласованность в модуле|fx самое важное
# Иногда руководство неприменимо
    0.pep уменьшает читабельность(даже if кто-то к этому больше привык)
    1.единообразие с уже написанным кодом не следуюшим pep
    # При сомнениях - выбирать более читабельный вариант

4 пробела
8 пробелов для старого кода
пробелы приоритетны
max длинна строки 
    79(?)|принятая в проекте
    72 для длинных блоков текста
        комменты
        docstrings
# Позволяет легко исп несколько окон
не мешать табы & пробелы в однои кодовой базе
аргументы интерпритатора
    -t
    # >> Warnings при исп смешанных отступов
    -tt
    # >> Errs при исп смешанных отступов

# Перенос длинных строк кода
    предпочтительно ()|[]
    | '\' if он выглядит лучше (google против)
    в случае необходимости можно добавить дополнительную пару скобок вокруг exp
    отступы для перенесенных кусков дб соблюдены
    переносы после операторов ⊃ ','
    # Examles
        # ЭТОТ ПРИМЕР СПОРЕН
        class Rectangle(Blob):
            def __init__(self, width, height,
                         color='black', emphasis=None, highlight=0):
                if (width == 0 and height == 0 and
                   color == 'red' and emphasis == 'strong' or
                   highlight > 100):
                    raise ValueError("sorry, you lose")
                if width == 0 and height == 0 and (color == 'red' or
                                                   emphasis is None):
                    raise ValueError("I don't think so -- valus are %s, %s" %
                                     (width, height))
                Blob.__init__(self, width, height,
                              color, emphasis, highlight)
    # es2:
        # опционально возможен отступ
        a = base / app_dir
            / other_dir
# Blank strs
    отделяются 2 строками
        fx вершнего уровня(не внутренние) & классы
    отделяются 1 строкой
        определения методов в классе
        группы импортов
        
    0|1 строка
        между неск expr записанными в одну строку
        # Например  
            заглушки fx
        логические части в fx

# Символ Ctrl+L(разрыв страницы) py обрабатывает как whitespace
    его можно исп для разделения кода на страницы

КОДИРОВКИ
# См PEP263

ИМЕНА
# ∀ идентификаторы должны означать англ слова(PEP3131), кроме сокращении и неанглийских технических терминов
# Единообразие с ∃ кодом важнее PEP(хотя это ПО ВОЗМОЖНОСТИ ЛУЧШЕ ПЕРЕПИСАТЬ)
    ПЕРЕЧИСЛЕНИЕ СТИЛЕИ ИМЕН
        
        b
        # Одиночная lowercase
        
        B
        # Одиночная UPPERCASE
        
        width
        # Слово lowercase
        
        WIDTH
        # Слово UPPERCASE
        
        width_with_underscores
        # lowercase words with underscores
        
        UPPERCASE_WITH_UNDERSCORES
        #
        
        CapitalizedWords
        # ~ CapWords ~ CamelCase ~ StudlyCaps
        
        mixedCase
        #в Δ от CamelCase - первое слово со строчной
        
        Capitalized_Words_With_Underscores
        #BAD PRACTICE
        
        <logic_group_prefix>_name
        # редко исп в Python, тк
            ?перед полями & именами obj стоит имя obj
            ?перед именами fx стоит имя модуля 
        # examples
            os.stat() >> (st_mode, st_size, st_mtime, ...)
            # Для подчеркивания соотв этих полеи структуре системных вызовов POSIX
        
        _single_leading_underscore
        #слабыи индикатор деталей реализации
        
        single_trailing_underscore_
        #для избежания конфликтов с зарезервированными словами
        #examples
            tkinter.Toplevel(master, class_='ClassName')
            from pprint import pprint as print_
        #исключения аргументы означаюшие класс & первый аргумент метода класса должен называться cls
        __double_leading_underscore
        # Δ имя attr класса
        # examples
            class FooBar:
                __boo = 1
            FooBar._FooBar__boo
                >> 1
            FooBar.__boo 
                >> AttrErr   
        
        __double_leading_and_trailing_underscore__
        #magic methods
        #исп только для деталей реализации Python
        # Реализует name mangling
        
              
#аббревеатуры в CamelCase пишутся CAPS
    HTTPServerError
    

name mangling
# Механизм Δ имен() добавляет имя класса к __attr__ для избежания конфликта с деталями реализации базового класса
# Разумееется не работает If имя подкласса = имени базового & имена их attrs тоже (что по идее весьма странно(может дело происходит в Δ модулях?))
# Может затруднить отладку при работе с __getattr__()(затрудняет доступ к attrs)
      # , но хорошо документирован и легко реализуется вручную
    # -> стараися достичь баланса (избежание конфликтов <> возможность доступа к этим attrs) 



dunder
# Исп для избежания конфликтов с attr классов спроектированных для наследования подклассами

ЗАПРЕЩЕНО
    I O l
    # Для однобуквенных имен
    
    ИМЕНА КОНСТАНТ
    # UPPERCASE_WITH_UNDERSCORES | UPPERCASE
    
    ИМЕНА МОДУЛЕЙ
    # Короткие, lowercase, могут ⊃ '_' if (улучшает читабельность)        
    # If модуль расширения C/C++ ⊃ сопутствуюшии модуль python ⊃ интерфеис высокого уровня -> расширение в _single_leading_underscore
    # Examples
        _socket.h
    
    ИМЕНА ПАКЕТОВ
    #короткие, lowercase, ⊅ '_'        
    #

    ИМЕНА КЛАССОВ
    #почти ∀ в CamelCase
    #классы для внутреннего исп могут начинаться с '_'
    
    ИМЕНА ИСКЛЮЧЕНИЙ
    # Тк - класс -> исп стиль классов
    # Может заканчиваться на Error (If exept действительно err)
    
    ИМЕНА GLOBAL V
    #~ именам fx
    
    
    ПРЕДОТВРАЩЕНИЯ ИМПОРТА GLOBAL V ИСП ONLY В МОДУЛЕ
        # Исп механизм __all__
        # | исп старое соглашение добавления к глобальным именам префикса '_'
        
    ИМЕНА FX
    # lowercase_with_underscores
    # | mixedCase в местах его преобладания для сохранения обратнои совместимости(напр threading.py)
    
    ИМЕНА FX ARGS
    # Первый arg class method - всегда cls


КОНФЛИКТЫ С ЗАРЕЗЕРВИРОВАННЫМИ СЛОВАМИ
    single_trailing_underscore_
    #
    исп синоним
    #   
    
    КОНФЛИКТЫ С ИМЕНАМИ ПОДКЛАССОВ
    double_trailing_underscore__
    # Для задействования механизма Δ имен 

СТРОКИ & КОММЕНТАРИИ
# ∀ strs должны ⊃ лишь ascii chars
    ИСКЛЮЧЕНИЯ:
        test case тестируюшие не-ASCII возможности программы
        имена авторов
        # Но имена желательно транслитерировать в латиницу
    
    КОММЕНТАРИИ
    # Менее предпочтительны чем понятные имена v 
    # Противоречие коду недопустимо
    # Законченные предложения
        # Titled, кроме случаев начала предложения с имени v
        # '.' в конце можно опустить If (предложение одно и короткое)
        # Два пробела после '.' в конце предложений
    
    КОММЕНТАРИИ В СТРОКЕ КОДА
    # Исп как можно реже
    # Отделяются двумя пробелами
    
    БЛОК КОММЕНТАРИЕВ
    # Обычно объясняет ∀ код(|его часть) после блока
    # Должен ⊃ отступ кода
    
    СТРОКИ ДОКУМЕНТАЦИИ
    # см PEP257
    # Требуются для ∀ public модулей, fx, классов, методов
    # Рекомендуются для ∀ private, кроме очевидных случаев
        """
        Docstring
        
        """

Strunk & White: "Elements of style"
#  эталонное руководство по написанию английских текстов
         
ПРОБЕЛЫ
    ЗАПРЕЩЕНЫ
        перед & после скобок
            #  ok
            spam(ham[1], {eggs: 7})
        перед ',', ';', ':'
            # Ok
            if x == 3: print(x, y); x,y = y, x
        в вызовах
            # Ok
            print('arst')
        при доступе по индексу
            # Ok
            d['key'] = lst[index]
        вокруг '=' для выравнивания
            # Ok
            x = 1
            lst = [x]
            long_v_name = [lst]
        вокруг '=' при его исп для обозначения kwarg|default val for params
            # Ok
            print(lst, sep='')
            def complex(real, imag=0.0):...
    НЕОБХОДИМЫ
        вокруг операторов exp(но не в параметрах вызова)
        # =, +=, -=, ..., ==, <, >, <>, !=, <=, >=, in, not, not in, is, is not, and, or, not
        # Арифметических операторов
            i = i + 1
            sum += 1
            sum = 1 * 2 + 3
            c = (a + b) * (a - b)
НИКОГДА НЕ ИСПОЛЬЗУЙ СОСТАВНЫЕ ИНСТРУКЦИИ(;)

ПЕРЕНОСЫ
    допустимо писать короткое, односторочное тело на строке заголовка
        if foo == 'blah': do_blah_thing()    
        for x in lst: total += x
        while t < 10: t = delay()
    недопустимо не ставить их при исп (?блочных) операторов(try...finally, if...else)


MULTILINE COMPREHENSIONS
#examples
	memberdef_list = [elem for elem in from_cache(classname, 'memberdefs')
        	          if elem.argsstring != '[]' and 
                	     'std::string' in null2string(elem.vartype)]
    
IMPORT
# Импорт Δ модулей на разных строках
    import os
    import sys
# Допустим импорт нескольких obj из модуля в одной str
    from subprocess import Popen, PIPE
# После комментариев модуля & docstring, но до объявления global v & const
# ?спецификации __all__ указываются после импортов
# Относительные импорты КРАИНЕ НЕ РЕКОМЕНДУЮТСЯ(см PEP328)
    абсолютные импорты переносимее & читабельнее
    # При исп класса ⊂ модулю допустимо писать так:
        from myclass import MyClass form foo.bar.yourclass import YourClass
        # If такое написание вызывает конфликт ->
            import myclass
            import foo.bar.yourclass
    ГРУППИРОВКА ИМПОРТОВ
        импорты standart lib
        
        импорты thirdparty
        
        импорты модулеи текушего проекта

CLASS ATTRS        
# Простые public простыми & понятными именами
ПРОЕКТИРОВАНИЕ НАСЛЕДОВАНИЯ
# При сомнениях лучше сделать attr класса "private", тк затем будет проше сделать его public, чем наоборот
# Открытые attrs используются пользователями классов -> нужно быть уверенным в обратной совместимости
# Для "private" не требуется гарантии их !Δ
# "protected" - attr класса ⊂ API подклассов
    # Некоторые классы проектируются для наследования классами расширяюшими | Δ поведения базового
        # При проектировании таких классов нужно явно указать:
            pubic attrs
            attrs ⊂ API подклассов(subclass API)
            attrs исп only базовым классом
    # Открытые attrs ⊅ prefix '_'
# Не исп сложные методы доступа/Δ(accessor/mutator, get/set)
    # Их легко добавить позже -> исп св-ва(properties) для скрытия fx реализации за синтаксисом доступа к attrs

properties работают only in new-style classes
нужно стараться избавляться от побочных эффектов fx-поведения
# Вещи вроде кеширования допустимы
избегай исп долгих операции тк из-за записи с помощью attrs складывается впечатление относительно быстрого доступа
if класс базовый, но не нужно чтобы подклассы наследовали   