классы python основаны на идеях Smalltalk

базовый класс = супер класс

классы братья
# не обязательно наследующиеся друг от друга классы, являющиеся базовыми для одного класса
    class Brother0:
        ...
    
    class Brother1:
        ...
        
    class C(Brother0, Brother1):
        ...