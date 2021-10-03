explain
#причины длительного exe Запроса
#Understanding EXPLAIN:http://www.dalibo.org/_media/understanding_explain.pdf
#для оптимизации запросов требуется понимать логику работы ядра pl
#выводит информацию неоходимую для понимания что делает ядра при запросе
analyze
    считывает случайное(?) число строк
        число строк зависит от параметра default_statistics_target
    собирает статистику val по кажд колонке