__mro__
#позволяет проверить порядок разрешения attr
    class A:
        a = 'A'
    
    class B:
        a = 'B'
    
    class C(B, A):
        ...
    
    C.__mro__
    >>     
        (__main__.C, __main__.B, __main__.A, object)

__class__
#СОДЕЖ link на класс экземпляра
    class C:...
    
    C().__class__   >> __main__.C