потоки
#независимо планируются
#могут exe асинхронно
#СУЩ в одном процессе ядра -> имеют одну выделенную mem(heap)


context switch
#переключение между exe конкурентных задач = переключение между контекстами


асинхронность
#альтернатива multithreading
#асинхронные события происходят независимо в одном потоке
#в отличие от многопоточности можно контролировать когда и как происходит произвольное вытеснение
    #облегчает изоляцию
    #избегает состояния гонки
#запуск и остановка корутин происходит в соотв с критериями а не на время
#асинхронная задача может вообще не вызываться
