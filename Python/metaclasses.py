# ВСЕ obj - экземпляр класса|метакласса 
    # КРОМЕ type
        # type - СОБСТВЕННЫЙ МЕТАКЛАСС
            # это НЕЛЬЗЯ воспроизвести на python - реализовано читерством на уровне реализации
# классы - экземпляры метаклассов
# причина сложности метапрограммирования не в метаклассах, а в том что они используются для сложных вещей основанных на
    интроспекции
    манипуляции наследованием
    __dict__
    ...
# принцип
    перехтат создания класса
    #при exe "class" создается ns будущего класса, затем дергается type()
    изменение класса
    возвращение модифицированного
# преимущества метаклассов перед fx
    явно
    # class UpperAttrMetaclass(type) сразу указывает на метакласс
    ООП
    #метаклассы могут наследоваться от других метаклассов, с перегрузкой их методов(напр. __new__, __init__, __call__
    группировка методов
    метаКЛАССЫ
# крайне сложны -> выше верояность ошибок
НАЗНАЧЕНИЕ
    # как виртуальный конструктор
    
    # создание API
        django orm
            #model.Model определяет __metaclass__
            #который превращает класс - в сложную привязку к бд и выставляет наружу простой API
НЕ ИСПОЛЬЗУЮТСЯ
    для простого ИЗМ класса
        #АЛЬТЕРНАТИВЫ
            РУКАМИ
            ДЕКОРАТОРЫ КЛАССОВ
