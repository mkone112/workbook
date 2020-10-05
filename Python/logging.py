логи могут дать больше данных чем трассировка стека сообщив состояние программы на момент сбоя
logging
#исп большинством third-party libs -> их msg можно интегрировать с собственными для создания единого лога
    .logger
    #?сущ
    #имя by def - root
    
    .config
    #модуль, разумеется требует отдельного импорта
        import logging
        ...
        logging.config >> AttrErr
        ...
        import logging.config
        ...
        logging.config >> ok

    #вроде СОДЕРЖ ВСЕ относящееся к конфигурированию
        .fileConfig(fname:str=<path>, disable_existing_loggers:bool)
        #производит конфигурирование используя файл конфигурации
        #es:
            import logging
            import logging.config
            ...
            logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
            # Get the logger specified in the file
            logger = logging.getLogger(__name__)
            logger.debug('This is a debug msg')
        #params:
            disable_existing_loggers:bool=True
            #исп для отключения/сохранения loggers СУЩ на момент вызова
            
#СУЩ 5 стандартных уровней severity(важности) события, КАЖД ВКЛЮЧ соотв метод для логгирования на соотв уровне
#by def severity debug и info не отображаются 
    .debug()
    # DEBUG
    # неявно вызывает .basicConfig без args -> после вызова - корневой logger не может быть настроен
    # by def не отображается
    #>> SEVERITY:logger_name:msg
        logging.debug('msg') >> DEBUG:root:msg

    .info()
    # INFO
    # неявно вызывает .basicConfig без args -> после вызова - корневой logger не может быть настроен
    # by def не отображается
    #>> SEVERITY:logger_name:msg
        logging.info('msg') >> INFO:root:msg

    .warning()
    # WARNING
    # неявно вызывает .basicConfig без args -> после вызова - корневой logger не может быть настроен
    #>> SEVERITY:logger_name:msg
        logging.warning('msg') >> WARNING:root:msg

    .error()
    # ERROR
    # неявно вызывает .basicConfig без args -> после вызова - корневой logger не может быть настроен
    #>> SEVERITY:logger_name:msg
        logging.error('msg') >> ERROR:root:msg


    .critical()
    # CRITICAL
    # неявно вызывает .basicConfig без args -> после вызова - корневой logger не может быть настроен
    #>> SEVERITY:logger_name:msg
        logging.critical('msg') >> CRITICAL:root:msg
    
    
    .exception()
    #ПОХОЖ на .error(exc_info=True)
    #всегда выводит данные об except -> использовать только в except:
    #регистрирует msg с уровнем ERROR и добавляет в msg информацию об except
        try:
            1/0
        except ZeroDivisionError as e:
            logging.exception("Exception occured")
        >>
            ERROR:root:Exception occured
            Traceback (most recent call last):
                File "<filename>", line <num>, in <module>
                    1/0
            ZeroDivisionError: division by zero
    #if требуется Severity != ERROR -> используется другие методы с переданным exc_info=True
#допускает создание пользовательских severity
    #не рекомендуется тк может привести к путаннице с журналами сторонних libs
    .basicConfig(**kwargs)
    #настройка корневого logger(работает oi он еще не был настроен - вызов работает один раз) 
    #params:
        level
        #корневой логгер с установленным указанным severity(предопределенные константы(по сути int числа)
            #регистрирования ВСЕХ событий уровня DEBUG и выше
            logging.basicConfig(level=logging.DEBUG)
            logging.debug('This will get logged')
        filename
        #путь к файлу лога
        #by def вывод в консоль
        filemode=a
        #
            w
            #при КАЖД запуске app(-> basicConfig()) файл перезаписывается
        format
        #формат вывода
            #вероятно
            '%(<val>)<спецификатор>'
        #examples
            logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')
            logging.warging('This will get logged to a file')
            >>
                root - ERROR - This will get logged to a file
        #можно передавать ЛЮБУЮ str в журналы, но СУЩ базовые элты ПРИНАДЛЕЖ LogRecord - могут быть легко добавлены в формат
            name
            levelname
            message
            process
            #process id
                logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
                logging.warning('This is a Warning')
                >>
                    18472-WARNING-This is a Warning
            asctime
            #YEAR-(XX_month)-(XX_date) HH:MM:SS,ms
                logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info('Admin logged in')
                >>
                    2018-07-11 20:12:06,288 - Admin logged in
                    
            ...
        #спецификаторы(сущ?)
            s
            #string
        
        datefmt
        #формат даты(исп time.strftime() ПРИНАДЛЕЖ datetime)
            logging.basicConfig(format='%(asctime)', datefmt='%d-%b-%y %H:%M:%S')
            logging.warning('Admin logged out')
            >>
                12-Jul-18 20:53:19 - Admin logged out
    #examles
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s')
#адаптирован пакета Log4j ПРИНАДЛЕЖ Java -> нарушает pep8(CamelCase vars) legacy для сохранения обратной совместимости

ЛОГИРОВАНИЕ ПЕРЕМЕННЫХ
#es
  logging.error('% raised an error', name)  
  logging.error(f'{name} raised an error')
    >> ERROR:root:John raised an error

ВЫВОД СТЕКА
#logging позволяет захват стека выполнения
    exc_info
    #
        exc_info=True
        #захватить стек приложения
    #es
        try:
            1/0
        except ZeroDivisionError as e:
            logging.error("Exception occured")
        >> 
            ERROR:root:Exception occured
        
        try:
            1/0
        except ZeroDivisionError as e:
            logging.error("Exception occured", exc_info=True)
        >>
            ERROR:root:Exception occured
            Traceback (most recent call last):
                File "<file_name>", line <line_number>, in <module>
                    1/0
            ZeroDivisionError: division by zero
            
ОПРЕДЕЛЕНИЕ СОБСТВЕННОГО ЛОГГЕРА ОТЛИЧНОГО ОТ root
#рекомендуется(особенно if app ВКЛЮЧ n модулей)
#user-defined logger
    # не может быть настроен basicConfig() -> требуется использовать Handler's & Formatter's
    #может ИМЕТЬ неск Handler's(напр для отправки в файл и по HTTP)
    ОСНОВНЫЕ КЛАССЫ
    
        Logger
        #класс чьи obj используются для вызова методов
        #получается .getLogger()
        
        LogRecord
        #obj автоматом создающийся Logger
        #СОДЕРЖ ВСЯ информация регистрируемого события
            имя логгера
            имя fx
            номер строки
            msg
            ...
        
        Handler
        #base class обработчик
        #используются для настройки user-defined loggers
        #подобно logger поддерживает установку severity(для создания неск обработчиков с РАЗН уровнями severity)
            #напр: WARNING и выше выводятся в консоль, но ERROR+ дополнительно пишутся в файл(см примеры)
        #methods:
            .setLevel(<logging_level>)
            #severity обработчика
            #es:
                stream_handler = logging.StreamHandler()
                stream_handler.setLevel(logging.WARNING)
            
            .setFormatter(<formatter>)
            #устанавливает Formatter возвращаемый logging.Formatter()
            #см примеры
        #производные отправляют LogRecord в требуемое место назначения вывода(консоль(sys.stdout)/файл/...)
        
            StreamHandler
            #производный Handler
            #отправляет журнал в ?консоль
            
            FileHandler
            #производный Handler
            #по идее отправляет журнал в файл
            
            SMTPHandler
            #производный Handler
            #по идее отправляет журнал по SMTP(почта)
            
            HTTPHandler
            #производный Handler
            #по идее отправляет журнал по HTTP
        
        
        Formatter
        #получает str формат вывода синтаксически ЭКВИВАЛЕНТНЫЙ basicConfig(format...)
        
        
    МЕТОДЫ
        .getLogger(name:str) -> Logger
        #метод
        #многократные вызовы с одним именем >> ссылку на один экземпляр Logger
            #избавляет от необходимости передачи obj logger везде где он требуется
        #es:
            import logging
            ...
            logger = logging.getLogger('example_logger')        
            logger.warning('This is a warning')
            >>
                This is a warning
            #в ОТЛИЧИЕ от root logger имя логгера не ВХОДИТ в выходной формат by def -> должен быть добавлен в конфиг
                #конфигурирование в формат ЭКВИВАЛЕНТНЫЙ root выдаст ЭКВИВАЛЕНТНУЮ ЗАПИСЬ
                    WARNING:example_logger:This is a warning
#es:
    #вывод WARNING+ в консоли, ERROR+ дополнительно пишутся в файл
    import logging
    
    # Create a custom logger
    # __name__ == '__main__' if модуль не импортирован else имя_модуля
    logger = logging.getLogger(__name__)
    
    # Create a handlers
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('file.log')
    stream_handler.setLevel(logging.WARNING)
    file_handler.setLevel(logging.ERROR)
    
    # Create formatters and add it to handlers
    stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_format)
    file_handler.setFormatter(file_format)
    
    # Add handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    
    # создаем LogRecord СОДЕРЖ ВСЕ данные о событии & передает ее ВСЕМ СУЩ обработчикам(stream_handler, file_handler)
    #file_hadler проигнориует этот LogRecord тк он ERROR+
    logger.warning('This is a warning')
    logger.error('This is an error')
    >>
        __main__ - WARNING - This is a warning
        __main__ - ERROR - This is an error
    
    ДРУГИЕ МЕТОДЫ НАСТРОЙКИ
    #полезно при частых ИЗМ конфигурации при работе app
    
        ФАЙЛ КОНФИГУРАЦИИ
        #es:
            ## file.conf
                #два логгера
                [loggers]
                keys=root,sampleLogger
                
                #один обработчик
                [handlers]
                keys=consoleHandler
                
                #один formatter
                [formatters]
                keys=sampleFormatter
                
                #после определения их имен - они настраиваются добавлением префиксов logger_|handler_|formatter_
                [logger_root]
                level=DEBUG
                handlers=consoleHandler
                
                [logger_sampleLogger]
                level=DEBUG
                handlers=consoleHandler
                qualname=sampleLogger
                propagate=0
                
                [handler_consoleHandler]
                class=StreamHandler
                level=DEBUG
                formatter=sampleFormatter
                args=(sys.stdout,)
                
                [formatter_sampleFormatter]
                format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
            
            ## example.py
                import logging
                import logging.config
                
                #load config
                logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
                
                # Get the logger specified in the file
                logger = logging.getLogger(__name__)
                
                logger.debug('This is a debug msg')
        DICT
            config.yaml
            # YAML конфиг
                version: 1
                formatters:
                    simple:
                        format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    handlers:
                        console:
                        class: logging.StreamHandler
                        level: DEBUG
                        formatter: simple
                        stream: ext://sys.stdout
                    loggers:
                        sampleLogger:
                            level: DEBUG
                            formatter: simple
                            stream: ext://sys.stdout
                        loggers:
                            sampleLogger:
                                level: DEBUG
                                handlers: [console]
                                propagate: no
                        root:
                            level: DEBUG
                            handlers: [console]
            test.py
                import logging
                import logging.config
                import yaml
                
                with open('config.yaml', 'r') as f:
                    config = yaml.safe_load(f.read())
                    logging.config.dictConfig(config)
                
                logger = logging.getLogger(__name__)
                logger.debug('This is a debug msg')
                >>
                    2018-07-13 14:05:03,766 - __main__ - DEBUG - msg