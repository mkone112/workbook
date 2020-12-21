ЗАЧЕМ
#процессы дороги
    #-> для io используем threads
        #] 3 потока exe io
            # интерпритатор должен переключаться между ними, выделяя им ресурсы
                проверяем t0 -> ждет
                проверяем t1 -> ждет
                проверяем t2 -> готов -> exe код
                #понесли потери на переключение на 2 не готовых потока

asyncio
#не умеет тупо прочитать файл с диска асинхронно
#синтаксический сахар над реализацией кооперативной многозадачности в одном потоке
#такой код легче писать и поддерживать
    разработчик сам определяет места переключения контекста
#предоставляет event loop отслеживающий события io & переключающий готовые и ждущие события io задачи
#исп для упрощения исп корутин и футур в асинхронном коде чтобы код выглядел синхронным без callback's
#сущ fx exe асинхронные задачи io
    #передаем fx циклу, чтобы он запустил их сам, он >> Future, мы проверяем его на готовность
#исп генераторы и корутины для остановки/возобновления задач
#оперирует
    event loop
    #системный механизм к которому asyncio предоставляет интерфейс
    #ожидает события и производит рассылку msg/events
    #управляет планированием и передачей awaitables(exe различных задач - регистрирует поступление и запускает в нужный момент)
    #можно исп несколько
        #в py 3.7(?-/?+) рекомендуется использовать один
        .time() -> float
        #текущее время измеренное внутренними часами цикла(!= time.time(), не время работы цикла)
    корутинами
    #спец fx похожая на генератор от которых ожидается(await) возврат управления обратно в event loop
    #ЛЮБАЯ fx с async
    #так-же obj первого класса
    #запускаются через event loop
    #содержат yield
        #переключает выполнение на другие корутины(возврат в main loop)
    #cooperative subroutine
    #подпрограмма для добровольной упреждающей многозадачности
        #активно уступает ресурсы другим подрограммам/процессам вместо принудительного вытеснения ядром
    #термин coroutine придуман в 1958 Мелвином Конвеем в Conway's Law для описания кода освобождающего ресурсы для других частей сис-мы
    #в asyncio так-же называется awaiting
        
    футурами
    #obj хранящие текущий результат exe какой-либо задачи(напр что задача еще не обработана, результат или exept)(по идее похоже на js promises), может обеспечивать пустую структуру для последующего заполнения данными и механизм callback срабатывающий при готовности данных
    #low level obj
    #заполнитель еще не полученных данных
    #в py 3.7(?-/?+) никогда не требуется создавать напрямую
    
#разбивает код на процедуры определяемые как корутины позволяя управлять их выполнением(включая параллельное)
#предоставляет фундаментальные инструменты реализации async io
#3.4+
    .gather(awaitables) -> future
    # асинхронный запуск и получение результата для нескольких задач
    # создает task
    # сбор awaitable в группу - удобный способ запланировать одновременное exe нескольких coroutines
    # связывает tasks несколькими полезными способами
        #когда ВСЕ tasks завершены -> их результаты >> в lst упорядоченом в соотв с порядком списка awaitable(те как и были переданы)
        #ЛЮБАЯ собранная задача мб отменена без отмены других собранных задач
    
    .create_task(coro(args...)) -> task_obj
    # создает и планирует task
    # "цикл - ищи и запусти эту сoroutine при первой возможности"
    
    .get_running_loop() -> <link_to_running_event_loop>
    
    .sleep(delay)
    #блокировка корутины на delay
    #иммитация блокировки io
        async def main():
            print('Sleep now.')
            await asyncio.sleep(1.5)
            print('Wake up!')
        ...
        asyncio.run(main())
    .run()
    #неявно создает & запускает eventloop
    #не может быть вызвана из СУЩ цикла обработки событий -> не может использоваться в Anaconda/IPython/Jupyter
    
    .stream
    #набор high-lvl сетевых примитивов для управления async событиями TCP
    
    .lock
    # async аналог примитива синхронизации ПРИНАДЛЕЖ threading
    
    .event
    # async аналог примитива синхронизации ПРИНАДЛЕЖ threading
    
    .condition
    # async аналог примитива синхронизации ПРИНАДЛЕЖ threading
    
    .subprocess
    # набор инструментов для запуска async подпроцессов(напр команд оболочки)
    
    .queue
    # async аналог queue
    
    .exception
    # обработка except в async коде
#компоненты
    HIGH-LEVEL API
    #для написания apps
    LOW-LEVEL API
    #для создания libs & сред на основе asyncio

ИНИЦИАЛИЗАЦИЯ MAIN EVENT LOOP
#каноническая точка входа в asyncio app:
    asyncio.run(main()) #main - coroutine верхнего уровня
    #неявно создает и запускает event loop


блокирующий io
#
    with open('myfile.txt', 'r') as file:
        data = file.read()
        # Until the data is read into mem, the program waits here
    ...
разбиение задач на конкурентные подзадачи возможено only при таком параллелизме когда он же и управляет этими подзадачами

СТРАТЕГИИ МИНИМИЗАЦИИ ЗАДЕРЖЕК БЛОКИРОВАНИЯ IO
    multiprocessing
    threading
    asyncio




корутины

футуры

awaitable
#(ожидаемый) ЛЮБОЙ obj от которого можно ждать прерывания выполнения
    courutine
    task
    #obj оборачивающий корутины
    #предоставляет методы для контроля выполнения и запроса статуса
    #позволяют запустить корутины в eventloop(что-то вроде proxy-интерфейса)
    future

ASYNC/AWAIT
#fx объявленные как coroutine(async) можно ожидать(вызывать) с помощью await
    async
    #keyword 3.5+
    
    
    await
    #keyword 3.5+
    #приостанавливает exe текущей корутины и вызывает ожидание awaitable (при await task - exe текущей coroutine блокируется до завершения task)
        async def other_coroutine(n):
            print(f"The answer is {n}.")
        ...
        async def main():
            # Планирование задачи - запуск по усмотрению event loop
            task = asyncio.create_task(other_coroutine(42))
            
            # Ожидаем завершения задачи
            # ВОЗВРАЩАЕМ УПРАВЛЕНИЕ EVENT LOOP
            await task
        ...
        asyncio.run(main())
        #после завершения, возможность запуска появится у других корутин
    #при вызове await, asyncio понимает что fx потребуется время
        #приостанавливает ее exe и мониторит ЛЮБЫЕ связанные события io, позволяя в это время запустить другую задачу
        #при io event(поступлении данных) он возобновляет fx




Task
#awaitable оборачивающийся вокруг coroutine
    .cancel()
    #планирование отмены на следующем проходе eventloop
    #отмена не гарантирована - task мб exe до прохода