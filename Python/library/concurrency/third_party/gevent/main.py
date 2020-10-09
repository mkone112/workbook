gevent
#похож на asyncio
    #особо эффективен при работоте с io bound тк процесс их exe может эффективно координироваться пранировщиком
#гарантирует что сетевые libs будут переключать свой gevent-контекст в любой подходящий для этого момент
#lib организации одновременных вычислений на основе libev
#предоставляет удобный API для задач, связанных с одновременной обработкой данных(CPU bound) & и работой с сетью(IO bound)
#переключение контекста реализовано через yield
    
    .select
    #модуль
        .select(rlist, wlist, xlist, timeout=None)
        #реализация select.select блокирующая только текущий greenlet
    
    
    .spawn(function, *args, **kwargs) -> Greenlet_instanse
    #метод
    #реализован метаклассом
    #мб исп как gevent.spawn|Greenlet.spawn
        gevent.spawn(print)
        >>
            <Greenlet at <adress>: <built-in function print>>
        gevent.spawn(print).spawn
        >>
            <bound method Greenlet.spawn of <class 'gevent._gevent_cgreenlet.Greenlet'>>
    #создает экз Greenlet(микро/зеленый поток) и помещает туда fx для исполнения(инициализирует greenlet)
    
    .joinall(greenlets_seq)
    #блокирует исполнение программы для exe переданных гринлетов & возвращает управление при завершении ВСЕХ
    #>> [<Greenlet at 0x1f2a0373948: _run>, ...]
        #которые СОДЕРЖ мн-во интересных возможностей
        gevent_run = gevent.joinall([gevent.spawn(print)])[0]
        gevent_run.successful() >> True
greenlet
#~микропоток
#паттерн
#запускаются в основном процессе и координируются в нем подобно os threads, но не используют ресурсы ос и контролируются не ей
    #-> в ЛЮБОЙ момент работает только один greenlet
#изначально не имеет своего планировщика исполнения
#реализован в виде C расширения




libev
#модуль C?