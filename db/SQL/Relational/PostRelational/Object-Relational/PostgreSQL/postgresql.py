связующая таблица?
#та что реализует связи между записями в Δ таблицах?
?как создать поле ⊃ число записеи в другои/этои-же таблице 


РЕЛЯЦИОННЫЕ СУБД?
#в реляционных субд данные представлены таблицами
#заголовок таблицы определяет столбцы
    #для КАЖД стоблца устанавливается тип данных - val соответствующих полей строк должны удовлетворять этим типам
    ТИПЫ ДАННЫХ СТОЛБЦОВ
    #site: postgrespro.ru/doc/datatype.html
    #можно создавать свои типы
        ОСНОВНЫЕ ТИПЫ
            integer
            text
            boolean
                true
                false
            NULL
            #не задано/не известно
#данные распологаются в строках
#данные не упорядочены(напр. не хранятся в порядке добавления)

PostgreSQL
#реляционная субд
#написан переносимо на C -> можно легко собрать на неподдерживаемых платформах
#постгрес/постгрес-q-l, но не постгре
#к версии 6.0 управление взяла на себя небольшая группа энтузиастов получившая название Глобальной группы разработки PostgreSQL(PostgreSQL Global Development Group), выполняет поддержку основных версий сис-мы в течение 5 лет с момента выпуска, осуществляется через списки рассылки(как и координация разработки)
#все основные решения о планах развития и выпусках новых версияй принимаются Управляющим комитетом(Core team) состоящим из 5 человек, кроме обычных разработчиков вносящих посильный вклад в развитие сис-мы, выделяется группа основных разработчиков(major contributors) сделавших наиболее существенных вклад в развитие PostgreSQL, а также разработчики с правом записи в репозиторий(committers), актуальный список разработчиков: postgresql.org
#один из крупнейших глобальных opensource проектов с широким русским представительством
#Вадим Михеев из Красноярска входивший в Core Team сыграл большую роль в становлении PostgreSQL(сейчас уже не занимается проектом), создал важнейшие части сис-мы
    многоверсионное управление одновременным доступом(MVCC)?
    #позволяет обходиться без блокировок строк во всех случаях кроме одновременного изменения строки в нескольких процессах
        #читающие транзакции никогда не блокируют пишущие и наоборот
        #работает и для уровня изоляции serializable

    сис-ма очистки(vacuum)?
    журнал транзакций(WAL)?
    вложенные запросы?
    триггеры?
#наиболее полно-fx free open-source субд уровня предприятия, применяется для создания критичных high-load бизнес-систем, альтернатива коммерческим бд(скорее сожрала их нахрен)
#основана на postgres
#цикл разработки очередной версии pl обычно занимает ~год, за это время принимаются на рассмотрения патчи от сообщества, для обсуждения которых традиционно используется список рассылки pgsql-hackers, патч включается в релиз if сообщество
    признает идею полезной
    реализацию правильной
    код проходит проверку другими разработчиками
    #за полгода до релиза(обычно весной) - этап стабилизации кода - новый fx откладывается до следующего релиза, продолжают приниматься только исправления уже включенных в релиз патчей
    #в течение релизного цикла несколько раз выпускаются беты, в конце выходит релиз-кандидат=> major
#раньше номер версии состоял из двух чисел, но начиная с 2017, было оставлено одно, за 9.6 последовала 10(по сути второе число осталось, но теперь обозначает minor, а не major релиз)
#наиболее критичные ошибки бекпортируются для предыдущих версий в виде minor патчей включающих накопительные исправления
#корректно оформленное сообщение об ошибке имеет шансы на скорейшее решение(напр в течение суток)
#помимо поддержки сообществом ряд компаний осуществляют коммерческую поддерку, в РФ - postgres professional: postgrespro.ru
serializable
#самый строгий уровень изоляции
#использует сис-му Serializable Snapshot Isolation обеспечивающую полное отсутствие аномалий сериализации и гарантирует что при одновременном выполнении транзакций результат будет тем-же что и при ПОСЛЕД exe


PostgreSQL 12
#релиз в октябре 2019
#release notes: postgrespro.ru/docs/postgresql/12/release-12
    секционирование
    #ранее аналог секционирования м.б. сделать лишь вручную на основе
        механизма наследования
        ограничений исключения
        триггеров
    возможность ссылаться на секционированную таблицу из внешних ключей
    увеличена скорость выполнения операций(в том числе при большом числе секций)
    уменьшения уровня блокировок для служебных команд
    упрощения администрирования
    НЕ РЕАЛИЗОВАНО
        глобальные индексы на секционированных таблицах
        #ведутся активные дискуссии
    индексы
        индексы на основе b-tree уменьшаются в размерах
        #касается
            многоколоночных индексов
            индексов с повторяющимися данными
        увеличилась скорость вставки в индексы
        при создании GiST, SP-GiST, GIN генерируется меньше журнальных записей
        индекс GiST может включать дополнительные столбцы с помощью конструкции INCLUDE, чтобы стать покрывающими
        #в пред версии это было доступно только для b-tree
        индекс SP-GiST обзавелся поиском ближайших соседей(k-NN), наравне с GiST
        #b-tree на подходе
        добавлена команда REINDEX CONCURRENTLY
        #пересоздает индексы без помех для операций изменения данных
        #ранее этого м.б. достичь коммандами CREATE и DROP INDEX CONCURRENTLY, но заменить индекс поддерживающий ограничение целостности без кратковременной монопольной блокировки было нельзя
    оптимизация и выполнение запросов
    запросы могут распараллеливаться на уровне изоляции serializable
    #т.к. в пред версиях была добавлена поддержка предикатных блокировок для индексов GiST, GIN и Hash -> уровень serializable становится еще привлекательнее(правда на репликах он пока не работает)
    другие изменения улучшающие качество планирования запросов
    команда EXPLAIN умеет сообщать нестандартные параметры оптимизатора => полезно для диагностики
    производительность сервера
        поддержка JIT-компиляции активирована по умолчанию
        из TOAST может извлекаться минимально необходимая начальная часть val
        #вместо того чтобы полностью распаковывать сжатое val и выбрасывать лишнее, как было раньше
    мониторинг
    #вывод запросов в журнал может генерировать огромный V информации
        возможность регистрации лишь определенного % транзакций
        #особенно полезно для OLTP-систем
        добавлены представления показывающие ход выполнения команд
        #по аналогии с имеющимся pg_stat_progress_vacuum
            CREATE INDEX
            REINDEX
            VACUUM FULL
        добавлено событие ожидания
            синхронизация с диском при записи в журнальных файлов
            #позволит получать лучшую детализацию perf io
        многие системные представления показывают более полную информацию
        добавлены fx просмотра архивного и временного каталога непосредственно из SQL
    очистка(vacuum)
    #default val обеспечивают более производительную работу автоочистки, что не отменяет необходимости ее настроки
        возможностей настройки автоочистки стало больше
        команды VACUUM и ANALYZE научились пропускать таблицы которые не удалось заблокировать
            #заодно они не пытаются больше запрашивать блокировку для таблиц к которым user не имеет доступа
        появилась возможность не удалять пустые страницы в конце табличного файла при очистке
        #обычно это полезно, но требует кратковременной блокировки таблицы
        команде VACUUM можно запретить очищать индексы
        #например для быстрейшей заморозки версии строк для предотвращения последствий переполнения счетчика транзакций
        можно указывать горизонт видимости в vacuumdb
        #позволяет направить очистку на те таблицы которые в ней больше всего нуждаются
        очистка удаляет пустые листовые страницы из GiST-индексов
    репликация и восстановление
        все параметры восстановления перенесены в postgresql.conf
        #Recovery.conf более НЕСУЩ
        переход в режим восстановления и режим резервного сервера инициируется двумя сигнальными файлами
        #это изменение унифицирует работу с конфигурационными параметрами и позволит в будущем менять некоторые настройки без перезагрузки сервера
        можно делать копии репликационных слотов(физических и логических)
        #полезно например при развертывании нескольких реплик из одного бекапа
        новая SQL-fx повышает резервный сервер до основного
        #ранее это м.б. сделать only сигналом от ос
        необходимые для работы потоковой репликации процессы wal_sender не учитываются при ограничении max числа соединений => мн-во коннектов клиентов больше не могут мешать репликации
    команды SQL
        GENERATED ALWAYS AS
        #создание в табл генерируемых столбцов
        #текущая реализация допускает only хранимые столбцы
            генерируемые столбцы зачастую удобнее столбцов, заполненных триггерами и быстрее
        COPY FROM
        #добавлена возможность фильтрация строк при чтении записей из файла в табл
        COMMIT
        #можно добавить AND CHAIN для завершения одной транзакции и начала след(предусмотрено стандартом SQL)
        ROLLBACK
        #можно добавить AND CHAIN для завершения одной транзакции и начала след(предусмотрено стандартом SQL)
        CREATE ACCESS METHOD
        #создание табличные методы доступа, и указание метода доступа при создании табл
        #единственный доступный - heap => пока для user'ов ничего не изменилось, но фактически это первый шаг к подключаемым хранилищам данных потребовавший серьезных изменений в ядре
        #разработка новых экспериментальных методов уже начата
    утилиты
        psql
        #консольный клиент
        #многими недооценен
        #стал удобнее
             поддерживается вывод таблиц в CSV
             подсказка по командам SQL выдает ссылку на документацию
             улучшено автодополнение по табуляции для многих команд
             добавлена команда
                 \dP
                 #показывает секционированные таблицы
        pg_upgade
        #добавлены
             возможность клонировать файлы(if фс это позволяет(а в чем проблема?))
             #эффект ~ использованию hardlinks, но след изменения не затрагивают  старый кластер и к нему можно вернуться при возникновении проблем
        pg_verify_checksums
        #переименована в pg_checksums
        #добавлена возможность включать/выключать checksums кластера без его пересоздания, сервер однако должен быть отсановлен
    поддержка SQL/JSON
        добавлена основная часть SQL:2016
            язык путей SQL/JSON
            #играет роль ~ XPath при работе с XML
    разное
        в таблицах системного каталога столбей oid больше не скрытый
        #теперь его видно в запросах с *
        документация обзавелась иллюстрациями
            66.4 "Реализация индексов GIN"
            68.6 "Компоновка страницы бд"
oid
#тип/столбец
#не следует использовать тип oid в собственный таблица(почему?)
стандары SQL
    SQL:2016
        определил способы работы с JSON, положив конец несовметимым реализациям
табличные методы доступа?
vacuumdb
#утилита
PostgreSQL 13+
#планируется
    мониторинг
        возможность регистарции только части "коротких" операций
    команды SQL
        GENERATED ALWAYS AS
        #дополнение: возможность виртуальных стоблцов(вычисление на лету)
        CREATE ACCESS METHOD
        #новые экспериментальные методы
            Zheap
            #избавляет от разрастания таблиц и необходимости очистки используя журнал отката
            #должен хорошо подойти для работы с часто изменяющимися данными
            #site:github.com/EnterpriseDB/zheap
            Zedstore
            #реализует колоночное хранилище данных со встроенным сжатием. Подходит для аналитических запросов обрабатывающих мн-во строк, но лишь чатсь столбцов
            #site:github.com/greenplum-db/postgres/tree/zedstore
    утилиты
        ps_checksums
            возможность включать/выключать checksums кластера на лету(без остановки сервера)
    поддержка SQL/JSON
        поддержка типов даты/времени
        часть стандарта описывающая необоходимые fx
            представление JSON в виде реляционной табл
            ...
pg_verify_checksums
#утилита >= 11 ~ pg_checksums 12
pg_checksums
#утилита 12+ ~ pg_verify_checksum 11-
pg_upgrade
#утилита обновления сервера
OLTP
#система
#exe множество однотипных транзакций

PostgreSQL 10
#последняя версия имеющая поддержку 32bit
#нововведения:
    декларативное секционирование
    #возможность объявить таблицу секционной при создании
    расширенная статистика по нескольким столбцам
    #позволяет учесть fx-зависимости и кол-во различных val для улучшения оценок планировщика
    #теперь расширенная статистика поддерживает списки частых val, на оценки для fx теперь можно влиять, указывая планировщику ожидаемую селективность, кардинальность и стоимость в зависимости от val параметров fx
    снято ограничение на материализацию общих табличных exp
    #позволяет планировщику оптимизировать их вместе с основным запросом
    #это изменение нарушает поведение по умолчанию, которое можно вернуть, явно указав MATERIALIZED
    управление выбором общего|частного плана для подготовленных операторов с помощью параметра сервера
    #ранее не было способа запрета планировщику переключаться на общий план, что могло приводить к неоптимальному выполнению запросов

кардинальность?
селективность?
PostgreSQL 11
#первая версия лишившаяся поддержки 32bit OS
#нововведения:
    возможность объявлять ограничения уникальности на секционированной таблице
    поддержка JIT-компиляции
    #не активирована по умолчанию
особенности pl
    надежность, устойчивость
        горячее резервирование
        восстановление
        различные виды репликации?
            синхронная
            асинхронная
            каскадная
    безопасность
    #позволяет подключаться по защищенному SSL-соединению
    #предоставляет аутентификацию по паролю(включая SCRAM)
    #возможность использования клиентских сертификатов
    #аутентификация с помощью внешних сервисов
        LDAP
        RADIUS
        PAM
        Kerberos
    #управление пользователями и доступом к obj БД
        создание и управление пользователями/групповыми ролями
        разграничение доступа к obj БД на уровне пользователей/групп
        детальное управление доступом(на уровне строк, столбцов)
        поддержка SELinux через встроенную fx-нальность SE-PostgreSQL(мандатное управление доступом)
    соответствие стандартам
        по мере развития стандарта ANSI SQL его поддержка обновляется в PostgreSQL, начиная от SQL-92 до SQL:2016
        поддерживает 160/179 обязательных возможнотей ANSI SQL, и большое кол-во не обязательных
    поддержка транзакционности
        обеспечивает полную поддержку свойств ACID
        обеспечивает эффективную изоляцию транзакций(благодаря MVCC)
    инструментарий для разработчиков приложений
    #позволяет реализовать приложение ЛЮБОГО типа
        языки серверного программирования
            встроенный PL/psSQL
            #удобен тесной интеграцией с SQL
            C
            Perl
            Python
            Tcl
            JS
            Java
            ...
        api для обращения к субд из приложений на ЛЮБОМ яп(включая стандартные интерфейсы ODBC, JDBC)
    набор obj бд, позволяющий эффективно реализовать логику ЛЮБОЙ сложности на строне сервера
        таблицы
        индексы?
        ПОСЛЕД
        ограничения целостности?
        представления?
        материализованные представления?
        секционирование?
        подзапросы?
        with-запросы(в том числе рекурсивные)?
        агрегатные/оконные fx?
        хранимые fx?
        триггеры?
    гибкая сис-ма полнотекстового поиска(многоязычная) с эффективным индексным доступом
    слабоструктурированные данные в духе NoSQL
        хранилище key:val hstore
        xml
        json/jsonb
    подключение источников данных, включая все основные субд в кач-ве внешних таблиц по стандартку SQL/MED с возможностью полноценного использования для записи и распределенного выполнения запросов(Foreign Data Wrappers)
    масштабируемость/производительность
    #pl эффективно использует multi-core cpu - производительность растет почти линейно с увеличением числа ядер
    #начиная с 9.6 pl может работать с данными в параллельном режиме
    #pl 10 позволяет параллельно читать данные(включая индексное сканирование), выполнять соединения и агрегации
    #pl 11 имеет
        полноценный режим хеш-соединения при котором несколько процессов совместно строят и используют общую хеш таблицу,
        возможность сканировать секционные таблицы и создавать индексы параллельно
    #pl 12 позволяет
        распараллеливать запросы на уровне изоляции serializable
        выполняет JIT-компиляцию запросов(повышая возможности использования аппаратных средств)?
        ...
    планировщик запросов
    #основан на стоимости
    #использует собираемую статистику, и учитывает в своих мат. моделях io/cpu
    #позволяет оптимизировать самые сложные запросы
    #обладает всеми методами доступа к данным,способам выполнения соединений характерных для передовых коммерческих субд
    #позволяет выполнять сканирование по битовой карте, что позволяет объединять несколько индексов для ускорения доступа
    возможности индексирования
        индекс
        #походу что-то вроде карты - указания что-где лежит
    #методы доступа
    #многие типы индексов могут создаваться не только по одному, но и по нескольким столбцам табл, независимо от типа можно строить индексы как по столбцам, так и по произвольным выражениям(?), а также создавать частичные индексы только для определенных строк
    #покрывающие индексы(?) позволяют ускорить запросы за счет того что все необходимые данные извлекаются из самого индекса без обращения к таблице(?)
        b-tree
        #традиционный способ
        hash
        #индекс на основе хеширования
        #в отличие от b-tree - работают только при проверке на равенство, но порой могут оказаться лаконичнее/эффективнее
        GiST
        #обобщенное сбалансированное дерево поиска
        #применяется для данных не допускающих упорядочивания(?почему бы и нет)
            R-tree
            #применяются для индексирования точек на плоскости с возможностью быстрого поиска ближайших соседей(k-NN search)
            индексирование операции пересечения интервалов
        SP-GiST
        #обобщенное несбалансированное дерево, основанное на разбиении области значений на непересекающиеся вложенные области, напр
            дерево квадрантов для пространственных данных
            префиксное дерево для текстовых строк
        GIN
        #обобщенный инвертированный индекс
        #используется для сложных val(состоящих из эл-тов)
        #применение
            полнотекстовый поиск где требуется находить документы содержащие слова из запроса
            поиск val в массиве
        RUM
        #развитие GIN для полнотекстового поиска
        #индекс доступный в виде расширения
        #ускорение фразового поиска и выдача результаов упорядоченных по релеватности
        BRIN
        #компактная структура, позволяет найти компромисс между размером индекса и скоростью поиска
        #эффективен на больших кластерных таблицах
        Bloom
        #индекс основанный на фильтре Блума, имеет компакное представление и позволяет быстро отсечь заведомо не нужные строки, но требует перепроверки оставшихся
    кроссплатформенность
        unix(Linux, FreeBSD, Solaris, macOS)
        windows
    расширяемость
    #одно из фундаментальных преимуществ PostgreSQL лежащее в основе его архитектуры - полноценная поддержка расширений
    #пользователи могут без изменений базового кода добавить
        типы данных
        fx и операторы для работы с новыми типами
        индексные и табличные методы доступа
        серверные яп
        подключения к внешним источникам данных(Foreign Data Wrappers)
        загружаемые расширения
      РАСШИРЕНИЯ
      #в стандартную поставку PostgreSQL входит ~50 расширений
        CitusDB
        #распределение данных по разным экземплярам PostgreSQL(шардинг(шаринг?))
        #массивно-параллельное выполнение запросов
        PostGIS
        #одна из наиболее известных и мощных сис-м обработки геоинформационных данных
    доступность
    #лицензия крайне либеральна, схожа с BSD и MIT, допускает
        неограниченное использование pl
        модификацию кода
        включение в состав других проектов(в том числе коммерческих)
    независимость
    #не принадлежит ни одной компании, развивается международным сообществом => независимость от вендора сохраняет инвестиции в ЛЮБОЙ ситуации

Solaris != Linux
k-NN search
#быстрый поиск ближайших соседей(алг. n-ближайших соседей?)

ODBC?
#интерфейс
JDBC?
#интерфейс
ACID
#св-ва
SQL:2016
#стандарт ANSI SQL, стандартизировал поддержку работы с JSON
ПОДКЛЮЧЕНИЕ К СЕРВЕРУ?
ТРАНЗАКЦИИ?
ИСПОЛЬЗОВАНИЕ PostgreSQL КАК БД ПРИЛОЖЕНИЯ?
МИНИМАЛЬНЫЕ НАСТРОЙКИ СЕРВЕРА?
pgAdmin?
#gui для управления pl
#аналоги
    wiki.postgresql.org/wiki/Community_Guide_to_PostgreSQL_GUI_Tools
#не умеет работь с дампами psql
ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ?
    ПОЛНОТЕКСТОВЫЙ ПОИСК?
    ФОРМАТ JSON?
    ДОСТУП К ВНЕШНИМ ДАННЫМ?
СЕРТИФИКАЦИЯ СПЕЦИАЛИСТОВ
#Олег Бартунов - астроном, научный сотрудник ГАИШ МГУ, занимается PostgreSQL более 25 лет, вместе с Федором Сигаевым и Александром Коротковым(committers)(авторы большого кол-ва популярных расширений) основал Postgres Professional в 2015, направления:
    коммерческая поддержка pl 24/7
    локализация PostgreSQL - поддерка национальных кодировок и unicode
    система полнотекстового поиска
    работа с массивами?
    работа с слабо-структурированными данными?
        hstore
        json
        jsonb
    новые методы индексации?
        GiST?
        SP-GiST?
        GIN?
        RUM?
        Bloom?
    создание спецверсии PostgreSQL сертифицированной ФСТЭК для использования в сис-мах обработки персональных данных
        Postgres Pro Standart?
        #полностью совместим с ванильной версией
        #бесплатен для ознакомления и образовательных целей
json - слабо-структурированные данные?
#текстовый формат
hstore
#формат слабо-структурированных данных?
jsonb
#формат слабо-структурированных данных?
#двоичная версия json
УСТАНОВКА И НАЧАЛО РАБОТЫ
#используется ванильный дистр pl 12
    установка службы pl
    управление службой pl
    инструкции по установке: postgresql.org/download
        параметры сервера
            порт 5432?
            разрешать подключения с любых адресов?
            локаль? для хранения данных на русском обязательна русская?
            пароль пользователя
            настроить PATH - для подключения к pl под текущим user'ом
            параметры оптимизации
                параметры по умолчанию - занимает меньше ram
        stack builder
        #установка и загрузка модулей
УПРАВЛЕНИЕ СЛУЖБОЙ И ОСНОВНЫЕ ФАЙЛЫ
    при установке регистрируется служба postgresql-12
    #запускается автоматом под учеткой Network Service
    содержит bat для запуска и остановки службы
    журнал сообщений сервера(походу рядом с data)
        с:\program files\PostgreSQL\12\data\log
        #запись периодически переключается в новый файл(имя содержит дату и время переключения(создания))
    конфиги распологаются в каталоги бд
    #документированы
    #настроек по умолчанию достаточно для ознакомления
        postgresql.conf
        #конфиг с основными настройками сервера
        pg_hba.conf
        #настройки доступа
        #по умолчанию только с локального пк и по паролю
pl написана на C, качество кода невероятно высоко
УСТАНОВКА НА LINUX
    ARCH
        sudo pacman -Syu
        #Обновление баз данных пакетов и полное обновление системы
        sudo pacman -Sc
        #очистить кеш
        sudo pacman -Sy postgresql
        sudo su - postgres -c "initdb --locale ru_RU.UTF-8 -E UTF8 -D '/var/lib/postgres/data'"
        #инициируем кластер с нужной локалью(она должна быть доступна в сис-ме
        при ошибке 'Невозможно создать директорию недостаточно прав' - изменяем владельца PGROOT директории и пробуем снова
        sudo chown -R postgres:postgres /var/lib/postgres/

        systemctl start postgresql
        systemctl status postgresql
        systemctl enable postgresql
        при ошибках
            /var/log/postgresql/postgresql-12-main.log
        sudo su - postgres
        #становимся пользовалетелем postgres
        createuser -DRSP <username>
        #D user не может создавать бд
        #R user не может создавать аккаунты
        #S user не суперпользователь
        #P запрашивать пароль при создании
        также можно использовать createuser без параметров, он задаст соотверствующие вопросы
        if имя пользователя совпадает с именем пользователя $USER - я получу доступ к бд оболочки pl без указания имени пользователя
        создаем бд(от пользователя с правами rw) if кодировка не указана - используемая по умолчанию
            createdb -0 username dbname [-E db_encoding]
        управление бд
            psql db_name -U username
            #if username=текущему пользователю($USER)
                psql
    Debian based
        #подключение пакетного репозитория PGDG(PostgreSQL Global Development Group)
            sudo apt-get install lsb-release
            sudo sh -c 'echo "deb \
                 http://apt.postgresql.org/pub/repos/apt/ \
                 $(lsb_release -cs)-pgdb main" \
                 > /etc/apt/sources.list.d/pgdg.list'
            wget --quet -0 - \
            https://www.postgresql.org/media/keys/ACCC4CF8.asc \
            | sudo apt-key add -
        #обновление списка пакетов
            sudo apt-get update
        #проверка настроек локализации
        #для хранения данных на русском val var
            LC_CTYPE
            LC_COLLATE
            #должны быть = ru_RU.UTF8
            #val en_US.UTF8 тоже подходит, но менее предпочтительно
            при необходимости нужно установить эти var
                export LC_CTYPE=ru_RU.UTF8
                export LC_COLLATE=ru_RU.UTF8
        #также необходимо убедиться что в сис-ме установлена соотв локаль
            locale -a | grep ru_RU  >> ru_RU.utf8
            #if это нет так => генерация локали
            sudo locale-gen ru_RU.utf8
        #установка
            sudo apt-get install portgresql-12
        #проверка состояния
            sudo -u postgres psql -c 'select now()'     >> <current time>
    wsl
        #проще простого
django лучше интегрирована с postgresql чем с mongo
flask лучше интегрирована с mongo чем с postgresql
управление службой в linux
    при установке автоматом создается пользователь postgres
        от имени которого работают процессы
        обслуживается сервер
        которому принадлежать все файлы субд
        актульные версии
            Debian 8 Jessie
            Debian 9 Stretch
            Debian 10 Buster
            Ubuntu 16.04 Xenial
            Ubuntu 18.04 Bionic
        данные бд
            /var/lib/postgresql/<version>/main
        основной конфиг
            /etc/postgresql/<version>/main/postgresql.conf
        конфиг настроек доступа
        #по умолчанию доступ only с локальной машины из под пользователя бд чье имя = имя пользователя ос
notepad++ имеет плагин для postgres
ОТНОШЕНИЕ МНОГИЕ КО МНОГИМ
    x отображается на любое y
    y отображается на любое x
        => не fx!
pl - объектно-реляционная бд

РЕЛЯЦИОННАЯ БД
    бд основанная на реляционной модели данных
    relation(отношения, зависимость, связь)
    НОРМАЛИЗАЦИЯ
    #нормальная форма
    #цель нормализации - устранение недостатков структуры бд, приводящих к избыточности
    избыточность приводит к
        аномалиям
        нарушениям целостности данных
        #реляционная модель описывает типичные примеры избыточности и способы их устранения
РЕЛЯЦИОННАЯ МОДЕЛЬ ДАННЫХ(РМД)
#логическая модель данных
#прикладная теория построения бд - приложение к задачам обработки данных теории мн-в, и логики первого порядка
#включает в себя
    структурный аспект(составляющая)
    #данные в бд - набор отношений
    аспект(состовляющая) целостности
    #отношения отвечают определенным условиям целостности
        рмд поддерживает декларативное ограничение целостности
            уровня домена(типа данных)
            уровня отношения
            уровня бд
    аспект обработки(манипулирования)
    #рмд поддерживает операторы манипулирования отношениями
        реляционная алгебра
        реляционное исчисление
    теория нормализации
реляционный -отношение
    неформальный синоним -таблица(нестрогое и неформальное) обозначает "отношение" не как абстрактное понятие, а визуальное представление отношение => нередко приводит к представлению что РМД имеет дело с плоскими таблицами, хотя отношения не могут быть плоскими или нет
    ОСОБЕННОСТИ РМД
        модель - логическая
        #отношения - логические(абстрактные), а не физические(хранимые) структуры
        для рбд веред информационный принцип
        #все информационное наполнение бд представлено одним способом - явное задание attr в кортежах отношений ,т.е. нет никаких указателей(адресов) связывающих одно val с другим
        наличие реляционной алгебры позволяет реализовать
            декларативное программирование
            декларативное ограничение целостности
            #в дополнение к навигационному(процедурному) программированию и процедурной проверке условий
АЛЬТЕРНАТИВЫ РЕЛЯЦИОННОЙ МОДЕЛИ
    иерархическая модель
    #устаревшая архитектура
    сетевая модель
    #устаревшая архитектура
    объектно-ориентированные субд(pl?)





материализованному представлению требуется обновление при изменении параметров например в *.lang
поле=ячейка=var

перечислять все поля в таблицах с их зависимостями по идее удобно для понимания структуры даже большой бд
    можно помечать для полей родителя и наследника
САМЫЙ ЛУЧШИЙ СПОСОБ АНАЛИЗА БД => ПРОСМОТРЕТЬ ЛИБО ЕЕ ЛИБО ЕЕ ДАМП






