#позволяет писать async код
    .ThreadPoolExecutor(<?num_of_thread>) -> Future
    #исполнитель
    #поддерживает пул потоков & процессов
    #задачи отправляются в пул
        #пул запускает задачи в доступном потоке/процессе

    .ProcessPoolExecutor


pip install futures