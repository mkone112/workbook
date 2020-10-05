magic method = метод перегрузки операции

dunder init == __init__

__new__ -> instance
#конструктор класса(экземпляров класса)
#может >> instance другого класса -> интерпритатор не вызывает __init__
#метод класса обрабатываемый особым образом(@classmethod не нужен)
#вызывается перед __init__, создает и >> obj, __init__ инициализирует(вроде присваивание var) obj переданный в качестве аргумента
#передает экземпляр в __init__(self)
#видимо принимает args ЭКВ __init__
#используется для настройки создания экземпляра
#es:
    #2.X
    class UpperAttrMetaclass(type):
        def __new__(upperattr_metaclass, future_class_name,
                    future_class_parents):
            
            attrs = (())
#pseudo constuct object
    def make_obj(class, args):
        new_obj = class.__new__(args)
        if isinstance(new_obj, class):
            class.__init__(new_obj, args)


__init__ -> None
#не конструктор
#инициализатор т.е. добавляет экземпляру всякой херни - не обязателен
#обязан >> None
    class Test:
        def __init__(self):
            return 0
    ...
    Test()  >> TypeError: __init__() should return None, not 'int'
#авто вызывается при создании obj
#ОТСУТСТВИЕ __init__ дает возможность создания obj без полей
    class Person:
        def set_name(self, name, surname):
            self.name = name
            self.surname = surname
    ...
    a = Person()
    a.set_name('first', 'second')

можно указать несколько __init__ но работать конечно будет лишь последний


__del__
#деструктор
#перегружает del