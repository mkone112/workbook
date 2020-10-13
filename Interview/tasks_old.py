__new__

дескрипторы

метаклассы 3.X
    typ или mcls
    #стандартное имя для первого arg в __new__ метакласса

super

__class__

mro
#порядок разрешения методов? не attr?

__dict__

имя текущей fx
    import inspect
    def foo():
        print( inspect.stack()[0][3] )
    foo()

bound method


__slots__