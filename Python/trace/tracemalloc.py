спец инструментарий для обнаружения утечек используется if анализ кода не результативен
    DataDog
    #мониторинг производительности микросервисов

tracemalloc
#создание ram snapshots
    .start()
    #инициализация tracemalloc
        tracemalloc.start()
    
    .take_snapshot()
    #>> снимок памяти
        snapshot = tracemalloc.take_snapshot()
    
    .statistics()
    #отображение на снапшоте упорядоченного lst ВСЕХ основных выделений ресурсов
        #отмечает 5 основных источников выделений mem группируемые по имени файла истоника
        import tracemalloc
        import logging
        ...
        logging.basicConfig(level=logging.INFO)
        tracemalloc.start()
        snapshot = tracemalloc.take_snapshot()
        for i, stat in enumerate(snapshot.statistics('filename')[:5], 1):
            # logging.info('top_current', i=i, stat=str(stat))
            logging.info(f'{i} {stat}')
        >>
            INFO:root:1 C:/Users/mk/PycharmProjects/tracemalloc_test/1.py:0: size=432 B, count=1, average=432 B
    
        .get_traced_memory()
        #es:
            