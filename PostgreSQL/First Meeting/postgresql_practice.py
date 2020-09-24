CRUD
    CREATE?
    READ?
    UPDATE?
    DELETE?
для подключения к субд нужен клиенты
    psql
    #терминальный клиент
    #входит в любую сборку pl
    #удобен для решения повседневных задач администрирования бд
        написание небольших запросов
        автоматизация процессов
            периодическая установка изменений кода на сервер субд
    #имеет собственные команды для ориентации в obj хранящихся в бд и представления данных из таблиц
запуск psql
    sudo -u postgres psql
    .../Program Files/PostgeSQL/12/scripts/runpsql.bat
ввод
#в [] указываются val по умолчанию
    сервера
    бд
    порта
    имя пользователя
    пароля пользователя postgres указанный при установке pl
при проблемах с отображение кириллицы -> убедиться что установлен TrueType-шрифт(напр Lucida Console|Consolas)
при проблемах с кодировкой сразу матерится
    в ответ -> приглашение к вводу
        postgres=#
один сервер pl может обслуживать несколько бд, но одновременно пользователь работает только с одной
символ ; используется для завершения строк, пока он не встретится команда считается незавершенной => команды можно разбивать на несколько строк

СОЗДАДИМ БД
    CREATE DATABASE test;   >> CREATE DATABASE
    #кажется она удаляется при переподключении=> видимо требуется зафиксировать изменения или что-то вроде
ПЕРЕКЛЮЧИМСЯ НА СОЗДАННУЮ БАЗУ
    \с test             >> You are now connected to db "test" as user "postgres"
    #приглашение к вводу сменится на имя бд
команды с \ не SQL - специальные команды psql(разные клиенты могут иметь разный синтаксис)
    полный спискок команд psql
        \?
        #т.к. довольно объемна => показана с помощью настроенной в ос команды-пейджера(обычно more|less)
сменить кодировку
    панель управления -> региональные стандарты -> дополнительно -> изменить язык сис-мы -> использовать UTF-8
    or
    REG ADD HKCU\Console\%SystemRoot^%_system32_cmd.exe /v CodePage /t REG_DWORD /d 1251
    or
    тупо добавить в батник psql
        chcp 1251
СОЗДАДИМ ТАБЛИЦУ
#дисциплин читаемых в вузе
    CREATE TABLE cources(
        c_no text PRIMARY KEY,  #столбец course_number
        title text,
        hours integer
        #float тоже пашет
        );
    #подсказка меняется с <db_name>=# на <db_name>(#
    #кроме имен и типов столбцов можно определить автоматически проверяемые ограничения целостности => СУБД не допустит появления в бд некорректных данных
    PRIMARY KEY
    #ограничение целостности сообщающее что val должны быть уникальны и не NULL
    #используется для идентификации строк
constraints(англ) - ограничение целостности?
ПОЛНЫЙ СПИСОК ОГРАНИЧЕНИЙ ЦЕЛОСТНОСТИ
#site:postgrespro.ru/doc/ddl-constraints.html
#справка по команде
\help CREATE TABLE
#~ \h кажется
ДОБАВИМ НЕСКОЛЬКО СТРОК(данных) В ТАБЛИЦУ
    INSERT INTO courses(c_no, title, hours)
    VALUES('CS301', 'Базы данных', 30),
        ('CS305', 'Сети ЭВМ', 60);          >> INSERT 0 2   #что за цифры?
#при отсутствии таблицы -> err: отношения НЕСУЩ
при массовой загрузке INSERT - не подходит
COPY
#site: postgrespro.ru/doc/sql-copy.html
#~
СОЗДАДИМ ЕЩЕ ПАРУ ТАБЛИЦ
CREATE TABLE students(
    s_id integer PRIMARY KEY,
    name text,
    start_year integer
);
#видимо указание что чему соответсвует, конечно можно поменять местами поля в values и students
INSERT INTO students(s_id, name, start_year)
VALUES (1451, 'Анна', 2014),
     (1432, 'Виктор', 2014),
     (1556, 'Нина', 2015);
     #так тоже работает
     INSET INTO students(name, s_id, start_year)
     VALUES ('Анна', 1451, 2014),
     ...
экзамен содержит оценку студента по дисциплине => студенты и дисциплины связаны отношением "многие ко многим"
запись в таблице экзаменов идентифицируется совокупностью номера студента и курса
    такое ограничение целостности относящееся сразу нескольким столбцам определяется фразой CONSTRAINT
    #при этом в итоговой таблице этого столбца не будет(ограничение целостности будет работать скрытно)
команды SQL вроде CREATE - фразы
CREATE TABLE exams(
    s_id integer REFERENCES students(s_id),
    c_no text REFERENCES cources(c_no),
    score integer,
    CONSTRAINT pk PRIMARY KEY(s_id, c_no) #т.к ограничение целостности с именем pk по уникальному not NULL val (s_id, c_no)
    );
теперь при любых действия субд будет проверять что все идентификаторы s_id, указанные в таблице exams соответствуют реальным студням(записям в табл students), а номера c_no сущ курсам => будет нельзя оценить не сущ студента, или поставить оценку по не сущ дисциплине(независимо от ошибок в коде/действий user'а)
#ограничения целостности - ставять границы возможных val
REFERENCES
#фраза
#определяет ограничения ссылочной целостности - внешние ключи(FOREIGN KEYS?)
#ограничение показывающее что val из одной табл ссылаются на строки в другой
ПОСТАВИМ СТУДНЯМ ОЦЕНКИ
INTO exams(s_id, c_no, score)
VALUES (1451, 'CS301', 5),
     (1556, 'CS301', 5),
     (1451, 'CS305', 5),
     (1432, 'CS305', 4);    >> INSERT 0 4   #видимо число ошибок/ число добавленых записей
#при попытке записи в несущ студня ->
    ОШИБКА: INSERT|UPDATE в табл. 'exams' нарушает ограничение внешнего ключа 'exams_s_id_fkey'
    ПОДРОБНОСТИ: Ключ (s_id) = (<несущ ключ>) отсутствует в табл 'students'
#при попытке дублирования => err
#при попытке добавления ключа не сущ в таблице=> err
ВЫБОРКА ДАННЫХ
    ПРОСТЫЕ ЗАПРОСЫ
    SELECT
    #оператор sql
    #чтение данных
  выведем два столбца из таблицы courses
  SELECT title AS course_title, hours
  FROM courses;

    AS
    #конструкция
    #позволяет переименовывать столбец
    #напоминает with as/ from .. import as из python
        СИНТАКСИС
            SELECT столбец [AS <отображаемое_имя>], столбец [AS ...] ...
            FROM таблица
        ПРИМЕРЫ
        SELECT title AS Название_Курса
        FROM cources                >> ok

        SELECT title AS Название Курса  >> err
        ...

        SELECT title AS 'Название Курса' >> err
        ...

        SELECT title AS "Название Курса"
        FROM cources                >> ok

        SELECT title AS "Название курса", hours AS "Часы"
        FROM cources                >> ok
ВЫВОД ВСЕХ СТОЛБЦОВ
    SELECT * FROM table_name;
в результирующей выборке можно получить одинаковые строки(if выводить например без PRIMARY KEY)

DISTINCT
#site: postgrespro.ru/doc/sql-select.html#SQL-DISTINCT
ВЫБОР ВСЕХ РАЗЛИЧНЫХ ГОДОВ
#~python set
    SELECT DISTINCT start_year FROM students;
        start_year
        ----------
            2014
            2015
ПОСЛЕ SELECT можно указывать любые exp
select без from будет содержать одну строку
    SELECT 2+2 AS result;
    #SELECT 2+2 result; тоже пашет
        result
        ------
            4
без указания имени столбца
        ?column?    #видимо val по умолчанию или что-то в этом духе
WHERE
#ПОЛУЧЕНИЕ СТРОК УДОВЛЕТВОРЯЮЩИХ УСЛОВИЮ
#условие должно иметь логический тип(по идее bool)
        SELECT * FROM cources WHERE hours > 45;
#в результирующую таблицу попадают все значения возвращающие true
#false|NULL отбрасываются
    #true/false отображаются в табл как t|f
        res
        ---
        t
NULL
#~false в булевых выражениях
#сравнение NULL с чем-либо = NULL
#логические операции с NULL = NULL, кроме
    true OR NULL = true
    false AND NULL = false
    #для проверки определенности val => IS [NOT]/IS [NOT] DISTINCT FROM/coalesce
        #подробнее: postgrespro.ru/doc/functions-comparison.html
        IS
        #~is python
            SELECT 1 IS NULL res
            SELECT 1 IS NOT NULL res;

        IS [NOT] DISTINCT FROM
        coalesce
        #fx для проверки определенности val
#кажется NULL val по умолчанию для новых столбцов - ячейка отображается пустой => UPDATE ... SET ... NULL ~ очистке поля
pl регистронезависим
ОПЕРАТОРЫ СРАВНЕНИЯ
    =
    <> !=
    >
    >=
    <
    <=
булевы выражения могут быть сложны и совмещаться с
    AND
    OR
    NOT
    и круглыми скобками
    #как в большинстве яп
СОЕДНИНЕНИЯ
#грамотно спроектированная рбд не содержит избыточных данных
#например таблица эзаменов жне содержит имя студента, т.к. его можно найти в другой таблице по номеру билета(что-то вроде цепи)
    => часто требуется соединять данные из нескольких таблиц перечисляя их с FROM
    SELECT * FROM courses, exams;
    #прямое|декларативное представление таблиц - к каждой строке одной табл добавляется каждая строка другой
        test=# SELECT * FROM cources;
             c_no  |    title    | hours
            -------+-------------+-------
             CS301 | Базы данных |    30
             CS305 | Сети ЭВМ    |    60
            (2 строки)
        test=# SELECT * FROM cources, exams;
             c_no  |    title    | hours | s_id | c_no  | score
            -------+-------------+-------+------+-------+-------
             CS301 | Базы данных |    30 | 1451 | CS301 |     5
             CS305 | Сети ЭВМ    |    60 | 1451 | CS301 |     5
             CS301 | Базы данных |    30 | 1556 | CS301 |     5
             CS305 | Сети ЭВМ    |    60 | 1556 | CS301 |     5
             CS301 | Базы данных |    30 | 1432 | CS305 |     4
             CS305 | Сети ЭВМ    |    60 | 1432 | CS305 |     4
            (6 строк)
        test=# SELECT * FROM exams;
             s_id | c_no  | score
            ------+-------+-------
             1451 | CS301 |     5
             1556 | CS301 |     5
             1432 | CS305 |     4
            (3 строки)
        test=# SELECT * FROM exams, cources;
             s_id | c_no  | score | c_no  |    title    | hours
            ------+-------+-------+-------+-------------+-------
             1451 | CS301 |     5 | CS301 | Базы данных  |    30
             1451 | CS301 |     5 | CS305 | Сети ЭВМ    |    60
             1556 | CS301 |     5 | CS301 | Базы данных  |    30
             1556 | CS301 |     5 | CS305 | Сети ЭВМ    |    60
             1432 | CS305 |     4 | CS301 | Базы данных  |    30
             1432 | CS305 |     4 | CS305 | Сети ЭВМ    |    60
     как правило более содержательныей результат можно получить указав WHERE условие соединения
     ПОЛУЧИМ ОЦЕНКИ ПО ВСЕМ ДИСЦИПЛИНАМ
     #сопоставляя курсы с экзаменами по курсу
     #в результат не включаются строки таблицы для которых не нашлось пары
        SELECT courses.title, exams.s_id, exams.score
        FROM courses, exams
        WHERE courses.c_no = exams.c_no;
                title    | s_id | score
            -------------+------+-------
             Базы данных | 1451 |     5
             Базы данных | 1556 |     5
             Сети ЭВМ    | 1432 |     4
    #с именами
    SELECT cources.title AS "Название предмета", exams.s_id AS "Идентификатор студента", exams.score as "Оценка"
    FROM cources, exams
    WHERE cources.c_no = exams.c_no;
    #АЛЬТЕРНАТИВА(с точки зрения СУБД - обе формы эквивалентны)
    УКАЗЫВАНИЕ СОЕДНИНЕНИЯ С ПОМОЩЬЮ JOIN
    #выведем студентов и их оценки по курсу Сети ЭВМ
    SELECT students.name, exams.score
    FROM students
    JOIN exams
      ON students.s_id = exams.s_id
      AND exams.c_no = 'CS305';
    #при этом в выборку не попали студни не сдававшие эзамен по дисциплине
        ДОБАВИМ ВНЕШНЕЕ СОЕДИНЕНИЕ
        #чтобы в выборку попали все студенты
        #соединения - обычная, и естественная для реляционных субд операция
        #pl ВКЛЮЧ мн-во эффективных механизмов для выполнения соединения
        #подробнее о соединениях: postgrespro.ru/doc/sql-select.html#SQL-FROM
        LEFT JOIN
        #в результат добавляются строки из левой таблицы(поэтому операция называется LEFT JOIN) для которых не нашлось пары в правой, при этом для столбцов правой таблицы возвращаются неопределенные val
        SELECT students.name, exams.score
        FROM students
        LEFT JOIN exams
            ON students.s_id = exams.s_id
            AND exams.c_no = 'CS305';
            >>
                 name  | score
                --------+-------
                 Анна   |
                 Виктор |     4
                 Нина   |
                (3 строки)
    условие во фразе WHERE применяется к готовому результату соединения => if вынести ограничение на дисциплины из условия соединения, Нина не попадет в выборку т.к. для нее exams.c_no не равен 'CS305'
        SELECT students.name, exams.score
        FROM students
        LEFT JOIN exams ON students.s_id = exams.s_id
        WHERE exams.c_no = 'CS305';
    #
при наличии альтернативных запросов - нужно выбирать более наглядные варианты
не стоит соединять данные в приложении - лучше доверить это бд
ВООБЩЕ МНОГО ВЕЩЕЙ МОЖНО ДЕЛАТЬ В БД ВМЕСТО КОДА

ПОДЗАПРОСЫ
#оператор SELECT формирует табл которую можно вывести как результат, но может быть использована в другой SQL конструкции в любом месте где по смыслу может находиться таблица, такая вложенная команда SELECT заключенная в круглые скобки - подзапрос
#if подзапрос возвращает одну строку и один столбец -> его можно использовать как обычное скалярное выражение
    #при открытии скобки - приглашение меняется на '<db_name>(#'
    #?вот это я конечно с трудом понимаю - вроде это прямое произведение двух таблиц
    SELECT name,
    (SELECT score
    FROM exams
    WHERE exams.s_id = students.s_id
    AND exams.c_no = 'CS305')
    FROM students;
    >>
              name  | score
             --------+-------
              Анна   |
              Виктор |     4
              Нина   |
              (3 строки)
скалярное выражение
#видимо просто выражение(операнды и операторы)
    численные выражения
    выражения со значениями-строками символов
    выражения со значениями даты-времени
    выражения со значениями-временными интервалами
    булевские выражения

скалярные подзапросы можно использовать в условиях фильтрации
ПОЛУЧИМ ВСЕ ЭКЗАМЕНЫ КОТОРЫЕ СДАВАЛИ СТУДЕНТЫ ПОСТУПИВШИЕ ПОСЛЕ 2014
    #мой вариант
        SELECT cources.title
        FROM cources, students
        WHERE students.start_year > 2014;
        >>
            title
            ------
            Базы данных
            Сети ЭВМ
    #книга
        SELECT *
        FROM exams
        WHERE (SELECT start_year
             FROM students
             WHERE students.s_id = exams.s_id) > 2014;
             >>
             s_id | c_no  | score
            ------+-------+-------
             1556 | CS301 |     5
\dt ПОКАЗАТЬ ВСЕ ТАБЛИЦЫ
в SQL можно формулировать условия и на подзапросы возвращающие произвольное число строк
    #IN проверяет содержится ли val в таблице возвращаемой подзапросом
    #список студентов получивших оценки по указанному курсу
    SELECT name, start_year
    FROM students
    WHERE s_id IN (SELECT s_id
                FROM exams
                WHERE c_no = 'CS305');
получается что указывать полный путь к столбцу вида students.c_no нужно только при наличии нескольких таблиц указанных во FROM
    #список студней не получивших оценки меньше 5
    SELECT name, start_year
    FROM students
    WHERE s_id NOT IN
        (SELECT s_id FROM exams WHERE score < 5);
КАК ВЫВЕСТИ СОДЕРЖИМОЕ НЕСКОЛЬКИХ ТАБЛИЦ?
    #кроме LEFT JOIN ничего не могу придумать
        нет - нихера
            SELECT *
            FROM students
            LEFT JOIN exams
                ON true;
                >>
                    дает результат ~
                    SELECT * FROM students, exams;
    #объединение запросов
        SELECT * FROM students;SELECT * FROM exams;
        #по другому вроде не пашет
    UNION
        #несколько таблиц в одной(заголовок от первой указанной)
        #вроде совпадающие столбцы сливаются в один
        #число столбцов должно совпадать иначе-> err
КОММЕНТАРИИ
#в начале синтаксического анализа заменяются пробелом
    ОДНОСТРОЧНЫЕ КОММЕНТЫ
       --comment
    МНОГОСТРОЧНЫЕ КОММЕНТЫ
    #поддерживают вложенность
        /* Multiline comment
         * with nested /* comment block */
         */
       
ЧТО БУДЕТ if указать столбцы без пути к таблице при выборе из нескольких таблиц?
    а что будет if запрашиваемые столбцы будут в нескольких таблицах?
ПОЛУЧИМ СПИСОК ВСЕХ ОТЛИЧНИКОВ С ОЦЕНКАМИ ПО КОНКРЕТНЫМ ПРЕДМЕТАМ
    SELECT students.name AS "Имя", cources.title AS "Предмет", exams.score AS "Оценка"
    FROM students, exams, cources
    WHERE students, exams, cources
    AND exams.c_no = cources.c_no
    AND NOT exams.score < 5;

еще одна возможность использовать предикат EXISTS
EXISTS
#предикат
#проверяет что подзапрос возвратил min одну строку
    SELECT name, start_year
    FROM students
    WHERE NOT EXISTS (SELECT s_id
                  FROM exams
                  WHERE exams.s_id = students.s_id
                  AND score < 5)
подробнее о подзапросах:postgrespro.ru/doc/functions-subquery.html

иногда уточнения имен столбцов недостаточно для устранения неоднозначности
    например в запросе одна и та же табл может учавствовать дважды|вместо табл в предложении FROM может использоваться безымянный подзапрос
        в этих случаях после подзапроса можно указать alias
            псевдонимы можно использовать и для обычных таблиц
alias'ы выбираются короткими и понятными(читабельными)
ALIAS пишется через пробел
безымянный подзапрос?
ВЫВЕДЕМ ИМЕНА СТУДНЕЙ И ИХ ОЦЕНКИ ПО ПРЕДМЕТУ БД
    #s - alias таблицы; ce - alias подзапроса
    SELECT s.name, ce.score
    FROM students s
    JOIN (SELECT exams.*
        FROM cources, exams
        WHERE cources.c_no = exams.c_no
        AND cources.title = 'Базы данных') ce
      ON s.s_id = ce.s_id;
 АЛЬТЕРНАТИВА БЕЗ ПОДЗАПРОСА
    SELECT s.name, e.score
    FROM students s, cources c, exams e
    WHERE c.c_no = e.c_no
    AND c.title = 'Базы данных'
    AND s.s_id = e.s_id;
АЛЬТЕРНАТИВА БЕЗ ALIAS
    SELECT name, score
    FROM students, exams
    WHERE students.s_id = exams.s_id
    AND c_no = 'CS301';
СОРТИРОВКА
#данные в табл не упорядочены
ORDER BY <exp>[, <exp>]
#выполняет сортировку согласно списку exp(ключей сортировки)
#подробнее:postgrespro.ru/doc/sql-select.html#SQL-ORDERBY
#после КАЖД exp можно указать направление
    ASC     по возрастанию(default)
    DESC    по убыванию
    #упорядочивание по возрастанию оценки, по совпадающим оценкам - по возрастанию номера студенческого билета, при совпадении первых двух ключей - по убыванию номера курса
        SELECT *
        FROM exams
        ORDER BY score, s_id, c_no DESC;
сортировку стоит выполнять в конце всех запросов перед получением результата, в подзапросах - обычно бессмысленна
МОЖНО ЛИ ВЫВЕСТИ ТАБЛИЦУ КАК ЯЧЕЙКУ ДРУГОЙ ТАБЛИЦЫ?
ГРУППИРОВКА
#размещение в одной строке результата val вычисленное на основе данных из нескольких строк исходных таблиц
вместе с группировкой используют АГРЕГАТНЫЕ FX
ВЫВЕДЕМ ОБЩЕЕ КОЛ-ВО ПРОВЕДЕННЫХ ЭКЗАМЕНОВ, КОЛ-ВО СДАВШИХ ИХ СТУДНЕЙ И СРЕДНИЙ БАЛЛ
    #ps. DISTINCT - разные студенты - явно здесь не нужен
    #count(*) видимо подсчет строк в
    SELECT count(*), count(DISTINCT s_id), avg(score)
    FROM exams;
        >>
             count | count |        avg
             -------+-------+--------------------
               3 |     3 | 4.6666666666666667
count()
#по всей видимости fx (агрегатная) подсчета строк в столбце/таблице
#походу возвращает int
#возвращает столбец с именем count
avg()
#fx (?агрегатная)
#среднее по столбцу
#походу возвращает float
#возвращает столбец с именем avg
кажется длинна float по умолчанию 16знаков после запятой(по идее это half precition или что-то вроде)
не уверен что разобрался в синтаксических единицах?
    где может быть
        DISTINCT
        WHERE
        таблицы возвращаемые SELECT
полный список агрегатных fx:postgrespro.ru/doc/functions-aggregate.html
МОЖНО ПРОКРУЧИВАТЬ ВЫВОД psql ниже последней строки с помощью CTRL!
МОЖНО ПОЛУЧИТЬ АНАЛОГИЧНУЮ ИНФОРМАЦИЮ
#в разбивке по номерам курсов с помощью предложения GROUP BY с ключами группировки
        SELECT c_no, count(*), count(DISTINCT s_id), avg(score)
        FROM exams
        GROUP BY c_no;
        >>
            c_no  | count | count |        avg
            -------+-------+-------+--------------------
            CS301 |     2 |     2 | 5.0000000000000000
            CS305 |     1 |     1 | 4.0000000000000000
GPOUP BY <lock_key>[,<lock_key>]
#предложение с ключами блокировки(группировка строк в одну по одинаковым val из столбца)
#подробнее:postgrespro.ru/doc/sql-select.html#SQL-GROUPBY
пробельные символы не учитываются в запросах

HAVING
#предложение
#позволяет фильтровать строки по результатам агреггирования в запросах исп группировку(только? - > вроде да)
#в отличие от WHERE(применяющегося до группировки(в них можно использовать исходную таблицу) - условия HAVING применяются после группировки(и в них можно использовать таблицы - результаты)
ИМЕНА СТУДНЕЙ ПОЛУЧИВШИХ БОЛЕЕ ОДНОЙ 5
    SELECT students.name
    FROM students, exams
    WHERE students.s_id = exams.s_id AND exams.score = 5
    GROUP BY students.name
    HAVING count(*) > 1;
    >>   name
        ------
         Анна
    #кажется сравнивает таблицу до GROUP BY и после
        SELECT students.name
        FROM students, exams
        WHERE students.s_id = exams.s_id AND exams.score = 5;
        >>   name
            ------
             Анна
             Анна
             Нина
        SELECT students.name
        FROM students, exams
        WHERE students.s_id = exams.s_id AND exams.score = 5
        GROUP BY students.name;
        >>   name
            ------
             Анна
             Нина
    НАЗВАНИЯ ПРЕДМЕТОВ С БОЛЕЕ ЧЕМ 1 СТУДНЕМ С 5ой
    #заглянем в таблицу чтобы понять как с ней работать
        #походу требуется указать PRIMARY KEY и связывающие ключи в обеих таблиц
        SELECT *
        FROM cources, exams
        WHERE exams.score = 5
        GROUP BY cources.title, cources.c_no, exams.s_id, exams.c_no;
        >>
             c_no  |    title    | hours | s_id | c_no  | score
             -------+-------------+-------+------+-------+-------
             CS305 | Сети ЭВМ    |    60 | 1556 | CS301 |     5
             CS301 | Базы данных  |    30 | 1451 | CS301 |     5
             CS301 | Базы данных  |    30 | 1556 | CS301 |     5
             CS305 | Сети ЭВМ    |    60 | 1451 | CS301 |     5
         #ТЕРЕРЬ УДАЛИМ СТРОКИ С НЕСОВПАДАЮЩИМИ c_no
         #если добавить GROUP BY задача будет решена
            SELECT cources.title
            FROM cources, exams
            WHERE exams.score = 5 AND cources.c_no = exams.c_no
            GROUP BY cources.c_no;
SELECT title
FROM cources, exams, students;
#будет выбрана только одна строка - при отсутствии неоднозначности в этом нет проблем
#столбец будет содержать дубли
    каждое val будет продублировано 3 раза(по числу столбцов в матрице на кооторую умножают)
        затем эти повторы будут снова продублированы 3 раза
        ДЛЯ ИСКЛЮЧЕНИЯ ПОВТОРОВ
          #таблицы можно попробовать связать
            SELECT title
            FROM students, exams, cources
            WHERE cources.c_no = exams.c_no
            AND exams.s_id = students.s_id;
            #но здесь будет один лишний дубль т.к. есть два отличника в группе
            выхода я не вижу
          альтернатива
            SELECT DISTINCT title
            FROM students, cources, exams;
в psql при выборе элемента из истории, текущее положение в истории смещается на эту позицию => удобно исправить косяк в одной строке, и повторить весь остальной ввод

ОШИБКИ
    SELECT *
    FROM cources, exams
    WHERE exams.score = 5
    GROUP BY cources.title;
        >>  ОШИБКА:  столбец "cources.c_no" должен фигурировать в предложении GROUP BY или использоваться в агрегатной функции
        СТРОКА 1: SELECT *
ИЗМЕНЕНИЕ И УДАЛЕНИЕ ДАННЫХ
UPDATE
#оператор
#выполняет изменение полей для строк определяемых(выбираемых) WHERE(по аналогии с SELECT)
#подробнее:postgrespro.ru/doc/sql-update.html
    УВЕЛИЧИМ ЧИСЛО ЧАСОВ ДЛЯ КУРСА "Базы данных" в два раза
        UPDATE cources  #таблица
        SET hours = hours * 2   #столбец #а есть ли дополненное присваивание?-> походу нет, hours *= 2 >> Err
        WHERE c_no = 'CS301';
        >> UPDATE 1     # видимо число обновленных полей
поле = ячейка
DELETE
#оператор удаления строк(ячейку очевидно не удалить, разве что перезаписать)
#подробнее:postgrespro.ru/doc/sql-delete.html
    DELETE FROM exams WHERE score < 5;  >> DELETE 1
  УДАЛЕНИЕ ВСЕЙ СТРОК
    DELETE FROM exams;
как удалить столбец из таблицы?(кроме заполния NULL)
ТРАНЗАКЦИИ
#операции составляющие логически неделимую единицу работы
#подробнее о транзакция:postgrespro.ru/doc/tutorial-transactionshtl
#еще более подробно о транзакция:postgrespro.ru/doc/mvcc.html
    РАСШИРИМ СХЕМУ БД
    #распреледим студней по группам, в каждой из которых должен быть староста
        #староста обязан входить в students(но я что-то не вижу требования чтобы он был обязан быть в группе - как это сделать?)
        CREATE TABLE groups(
            g_no text PRIMARY KEY,
            #запрещаем неопределенные val
            monitor integer NOT NULL REFERENCES students(s_id)
        );
    ДОБАВИМ СТОЛБЕЦ
        ALTER TABLE students
        ADD g_no text REFERENCES group(g_no)
        >>  ALTER TABLE
    СОЗДАДИМ ГРУППУ
    #A-101 и поместим в нее всех студней, староста - Анна
    #затруднение
        мы не может создать группу без старосты, но как назначить старосту несущ группе? => потенциально может привести к несогласованности(логической некорректности) данных
        ДВЕ ОПЕРАЦИИ НУЖНО СОВЕРШИТЬ ОДНОВРЕМЕННО
        #одна не имеет смысла без другой
        #пример искуственный, для этого в groups g_no должна зависить от students
            BEGIN;  >> BEGIN
            INSERT INTO groups(g_no, monitor)
            SELECT 'A-101', s_id
            FROM students
            WHERE name = 'Анна';
            ЗАПУСТИМ ПАРАЛЛЕЛЬНЫЙ СЕАНС PSQL
            #и проверим изменения(их нет т.к. транзакция не завершена)
                SELECT * FROM groups;
            ПЕРЕВЕДЕМ СТУДНЕЙ В НОВУЮ ГРУППУ
                UPDATE students SET g_no = 'A-101';
            ЗАВЕРШИМ ТРАНЗАКЦИЮ
            #зафиксировав изменения
                COMMIT;
BEGIN;
COMMIT;
#начало, конец транзакции, не выполняется(или выполняется виртуально) пока не встрети COMMIT;
#возвращает ROLLBACK при попытке завершить кривую транзакцию
ROLLBACK
#команда прерывающая транзакцию
END;
#кажется вызывает COMMIT;
КАК УДАЛИТЬ ТАБЛИЦУ?
pl дает гарантии
    АТОМАРНОСТЬ
        ЛЮБАЯ транзакция выполняется только целиком
        #if в одной из команд - ошибка => изменения не фиксируются
    СОГЛАСОВАННОСТЬ
        при фиксации изменений - все ограничения целостности выполняются - иначе транзакция прерывается
        данные согласованы до и после транзакции
    ИЗОЛЯЦИЯ
        другие клиенты не имеют доступа к несогласованным данным во время транзакции
        #за счет этого pl может параллельно обслуживать мн-во сеансов сохраняя корректность данных
        #особенность pl - мн-во клиентов могут работать с данными не блокируя друг друга
            но блокировка возникает при одновременном изменении строки из разных процессов
    ДОЛГОВЕЧНОСТЬ(НАДЕЖНОСТЬ)
        #данные не пропадут(да-да) при сбое (при правильных настройках(каких?))
ALTER [TABLE](only?)
#добавление столбца в СУЩ табл
в окне то-ли cmd то-ли psql есть пункты
    отметить(хз зачем)
    найти(CTRL-F)

SELECT* FROM groups;    >> ok
SELECT *FROM groups;    >> ok
SELECT*FROM groups;     >> Err
команды не являющиеся корректными - просто игноририются
    test=# asfd >> #ничего
НЕ СМОГ ПРИДУМАТЬ КАК СДЕЛАТЬ СВЯЗЬ ТАБЛИЦ ВЗАИМНОЙ
    CREATE TABLE new_groups(
            g_no text PRIMARY KEY REFERENCES students(g_no),
            monitor integer NOT NULL REFERENCES students(s_id)
    ;
    >> ОШИБКА:  в целевой внешней таблице "students" нет ограничения уникальности, соответствующего данным ключам
КОМАНДЫ psql
#мне кажется что аргументы в скобках используют синтаксис re [abc] ~ a|b|c
\x
#[+] более подробный вывод
#переключить табличный(традиционный) вывод(столбцы и строки) на расширенный(КАЖД столбец на отдельной строке)
#удобно для просмотра широких строк
\q
#~quit~exit~\quit
\watch <sec>
#повторять последний SQL запрос в цикле через заданное число секунд
#прерывается по CTRL-C
\e <file> <string>
#править буфер запроса/файл во внешнем редакторе
#обычно это вроде послений sql запрос в notepad
#не очень понял как использовать свой редактор(указанный путь к notepad++ не сработал(возможно из-за "++" в конце)
    \e  >> перекидывает в notepad => \c test => сохранить и закрыть notepad => выполнит \c test
\ef [,fx[,string]]
#править определение fx во внешнем редакторе
\i  <file>
#выполнить команды из файла
\echo <string>
#записать строку в стандартный вывод
\r
#очистить буфер запроса
\if
\elif
\else
\endif
    #условия
    #не очень разобрался
\d[S+] name
#описание таблицы/представления/послед
    \d
    #~\dt кажется
    \dS
    #выводит кучу таблиц (видимо системных)
    \d+
    #~dt + размер и описание
    \d tablename
    #просмотреть свойства таблицы
        столбцы(колонки)
        типы
        правило сортировки
        допустимость NULL
        По умолчанию
        Modifiers(ограничения целостности)[не уверен]
        Индексы
        #пример
            "students_pkey" PRIMARY KEY, btree (s_id)
        ссылки извне
            #пример
            TABLE "exams" CONSTRAINT "exams_s_id_fkey" FOREIGN KEY (s_id)REFERENCES students(s_id)
\l[+]
#список бд
    \l
    #+ кодировка, LC_TYPE, LC_COLLATE
    \l+
    #+права доступа, размер, табл. пространство
\С [string]
#задать заголовок таблицы или убрать
\H
#переключить режим вывода в HTML
\conninfo
#информация о текущем соединении
    база
    user
    server
    adress
    port
\password [user_name]
#безопасно сменить пароль пользователя
\! [command]
#выполнить команду в командной оболочке или закустить ее
    \! cls #очистка вывода
\timing [on|off]
#показывать время выполнения операторов
\du
#список пользователей, со списком ролей, и членством в ролях(видимо группах)
    Суперпользователь
    Создает роли
    Создает БД
    Репликация
    Пропускать RLS
\di
#список индексов(отношений)(вроде PRIMARY KEY всех таблиц)
\dv
#список представлений(отношений)
\df
#список fx
#по умолчанию пуст
    схема
    имя
    тип результата
    тип args
    тип
\dn
#список схем
        Список схем
      Имя   | Владелец
    --------+----------
     public | postgres
\dx
#список установленных расширений
          Имя   | Версия |   Схема    |           Описание
        ---------+--------+------------+------------------------------
         plpgsql | 1.0    | pg_catalog | PL/pgSQL procedural language
\dp
#список привелегий
\dm
    список материализованных views
\dL
    список языков процедур


судя по выводу \l+ размеры таблиц нереально большие - 8mb на таблицу 3x3
УДАЛЕНИЕ ТАБЛИЦЫ
    DROP TABLE table;
    удаление obj с зависимостями
        DROP TABLE table CASCADE;
УДАЛЕНИЕ СТОЛБЦА
            ALTER TABLE tablename
            DROP COLUMN columnname;
            #if сущ, и имеет зависимости
                ALTER TABLE tablename
                DROP COLUMN IF EXISTS column_name CASCADE;
УДАЛЕНИЕ БД
#по идее распространенная операция - должно быть просто
схема?
оконные fx?
отличия реляционная/постреляционная бд?
attr по идее = столбцы
ДЕМОНСТРАЦИОННАЯ БД
    #8 таблиц с правдоподобными данными + 4 представления
    #авиакомпания
    #aviacompany.png на рабочем столе
    #временный срез ~ бекапу реальной сис-мы(if рейс departed=> на момент среза борт в воздухе)
    #текущая версия 15.08.2017
    СУЩНОСТИ
    #не связанные столбцы в разных таблицах|сущностях имеют разные названия(напр amount|total_amount) видимо для исключения неявных связей
    пассажир
    #не отдельная сущность
    #для простоты - все пассажиры уникальны
    карта городов - просто данные, не имеет смысла их разбирать
    очевидно что поля с использованием timezone - local
        СХЕМЫ
            bookings(не таблица)
            public
        материализованных представлений нет
        при подключении бд параметр search_path устанавливается автоматом
        представления показывает данные на языке установленном в конфигурационном параметре booking.lang(default - русский)
        ПРЕДСТАВЛЕНИЯ
            aircrafts
                     CREATE VIEW aircrafts AS
                     SELECT ml.aircraft_code,
                        (ml.model ->> lang()) AS model,
                        ml.range
                       FROM aircrafts_data ml;
            airports
                    CREATE VIEW airports AS
                     SELECT ml.airport_code,
                        (ml.airport_name ->> lang()) AS airport_name,
                        (ml.city ->> lang()) AS city,
                        ml.coordinates,
                        ml.timezone
                       FROM airports_data ml;
            flights_v
            --представление для рейсов
                CREATE VIEW flights_v AS
                 SELECT f.flight_id,
                    f.flight_no,
                    #МЕСТНОЕ ВРЕМЯ ВЫЛЕТА
                    f.scheduled_departure,
                    timezone(dep.timezone, f.scheduled_departure) AS scheduled_departure_local,
                    #МЕСТНОЕ ВРЕМЯ ПРИБЫТИЯ
                    f.scheduled_arrival,
                    #ПРОДОЛЖИТЕЛЬНОСТЬ ПОЛЕТА
                    timezone(arr.timezone, f.scheduled_arrival) AS scheduled_arrival_local,
                    (f.scheduled_arrival - f.scheduled_departure) AS scheduled_duration,
                    #РАСШИФРОВКА ДАННЫХ О АЭРОПОРТАХ
                    f.departure_airport,
                    dep.airport_name AS departure_airport_name,
                    dep.city AS departure_city,
                    f.arrival_airport,
                    arr.airport_name AS arrival_airport_name,
                    arr.city AS arrival_city,
                    f.status,
                    #3x-значный id самолета
                    f.aircraft_code,
                    f.actual_departure,
                    timezone(dep.timezone, f.actual_departure) AS actual_departure_local,
                    f.actual_arrival,
                    timezone(arr.timezone, f.actual_arrival) AS actual_arrival_local,
                    (f.actual_arrival - f.actual_departure) AS actual_duration
                   FROM flights f,
                    airports dep,
                    airports arr
                  WHERE ((f.departure_airport = dep.airport_code) AND (f.arrival_airport = arr.airport_code));
            routes
            --представление для маршрутов
                CREATE VIEW routes AS
                 WITH f3 AS (
                         SELECT f2.flight_no,
                            f2.departure_airport,
                            f2.arrival_airport,
                            f2.aircraft_code,
                            f2.duration,
                            array_agg(f2.days_of_week) AS days_of_week
                           FROM ( SELECT f1.flight_no,
                                    f1.departure_airport,
                                    f1.arrival_airport,
                                    f1.aircraft_code,
                                    f1.duration,
                                    #массив дней по которым совершаются полеты(один рейс может происходить не каждый день)
                                    f1.days_of_week
                                   FROM ( SELECT flights.flight_no,
                                            flights.departure_airport,
                                            flights.arrival_airport,
                                            flights.aircraft_code,
                                            (flights.scheduled_arrival - flights.scheduled_departure) AS duration,
                                            (to_char(flights.scheduled_departure, 'ID'::text))::integer AS days_of_week
                                           FROM flights) f1
                                  GROUP BY f1.flight_no, f1.departure_airport, f1.arrival_airport, f1.aircraft_code, f1.duration, f1.days_of_week
                                  ORDER BY f1.flight_no, f1.departure_airport, f1.arrival_airport, f1.aircraft_code, f1.duration, f1.days_of_week) f2
                          GROUP BY f2.flight_no, f2.departure_airport, f2.arrival_airport, f2.aircraft_code,
                          #плановая продолжительность рейса
                          f2.duration
                        )
                 SELECT f3.flight_no,
                    f3.departure_airport,
                    dep.airport_name AS departure_airport_name,
                    dep.city AS departure_city,
                    f3.arrival_airport,
                    arr.airport_name AS arrival_airport_name,
                    arr.city AS arrival_city,
                    f3.aircraft_code,
                    f3.duration,
                    f3.days_of_week
                   FROM f3,
                    airports dep,
                    airports arr
                  WHERE ((f3.departure_airport = dep.airport_code) AND (f3.arrival_airport = arr.airport_code));

        ТАБЛИЦЫ
        #(s) Указание что это экземпляр(строка?) сущности (не избыточен - позволяет исключить опечатки)
            aircrafts_data
            --самолет/борт
                #id
                aircraft_code character(3) NOT NULL
                #название модели
                model jsonb NOT NULL
                #дальность полета[км]
                range integer NOT NULL
                CONSTRAINT aircraft_range_check CHECK ((range > 0))
            airports_data
                CREATE TABLE airports_data (
                airport_code character(3) NOT NULL,
                airport_name jsonb NOT NULL,
                #можно исп для идентификации аэропортов в одном городе(напр для пересадок?)
                city jsonb NOT NULL,
                #долгота и широта
                coordinates point NOT NULL,
                timezone text NOT NULL
            );
            boarding_passes
            --посадочный талон
            --пассажир может зарегистрироваться только на рейс который есть в Ticket_filight(s)
            --выдача возможна за сутки до scheduled_departure(при регистрации)
            --комбинация ticket_no(seat_no)&flight_id д.б. уникальна(одно место - один пассажир)
            --pk = Ticket_flights pk
                CREATE TABLE boarding_passes (
                    ticket_no character(13) NOT NULL,
                    flight_id integer NOT NULL,
                    # присваивается в порядке регистрации пассажиров
                    # уникален в пределах рейса
                    boarding_no integer NOT NULL,
                    # место
                    # схема данных не контролирует что места в посадочных талонах соответствуют имеющимся в салоне
                    seat_no character varying(4) NOT NULL
                );
            bookings
            --бронирование/бронь(билетов)
            --основная сущность
            --одна Booking(s) может ВКЛЮЧ неск. пассажиров с отдельными Ticket(s)(билетами)
            --предпологается что ВСЕ Ticket(s)(билеты) в Booking(s)(брони) ВКЛЮЧ = набор Flight(s)(несмотря на отсутствие ограничений)
                CREATE TABLE bookings (
                    book_ref character(6) NOT NULL,                 #идентификатор
                    book_date timestamp with time zone NOT NULL,    #пассажир max за месяц делает бронь
                    total_amount numeric(10,2) NOT NULL             #общая стоимость Flight(s)(перелетов) ВСЕХ пассажиров в брони
                );

            flights
            --перелеты/рейсы
            --КАЖД Flight(s)(рейс) следует из departure_airport в arrival_airport
            --Flight(s)(рейс) с одинаковым flight_no(номером рейса) имеют одинаковые departure_airport и arrival_airport, но разные scheduled_departure
            --Flight(s)(рейсы) с пересадками отсутствуют - вместо этого при отсутствии прямого маршрута(route(s)?) в Ticket(s) включается несколько Flight(s)
            --избыточна - позволяет получить информацию о маршруте независимо от дат рейсов
                CREATE TABLE flights (
                    #первичный суррогатный ключ для обеспечения компактности внешних(Foreign) ключей
                    #ВКЛЮЧ два поля: flight_no & sheduled_departure(чтобы было проще ссылаться на строку из других таблиц)
                    flight_id integer NOT NULL,
                    flight_no character(6) NOT NULL,            #номер рейса
                    scheduled_departure timestamp with time zone NOT NULL, #плановая дата, время вылета, походу local
                    scheduled_arrival timestamp with time zone NOT NULL, #плановые дата, время прибытия, походу local
                    departure_airport character(3) NOT NULL,    #код аэропорта вылета
                    arrival_airport character(3) NOT NULL,      #код аэропорта прибытия
                    # статус Flight(s)(рейса), одно из val:
                    #     Scheduled
                    #         доступен для брони не более чем за месяц до scheduled_departure
                    #         НЕСУЩ в бд более чем за месяц до scheduled_departure
                    #     On Time
                    #         доступен для регистрации(за сутки до scheduled_departure)
                    #         не задержан
                    #     Delayed
                    #         доступен для регистрации(за сутки до scheduled_departure)
                    #         задержан
                    #     Departed
                    #         aircraft(борт) в воздухе
                    #     Arrived
                    #         aircraft(борт) прибыл в arrival_airport(пункт назначения)
                    #     Cancelled
                    #         Flight(s) отменен
                    status character varying(20) NOT NULL,
                    aircraft_code character(3) NOT NULL,
                    #может отличаться на неск часов от scheduled_departure
                    actual_departure timestamp with time zone,
                    #может отличаться на неск часов от scheduled_arrival
                    actual_arrival timestamp with time zone,
                    CONSTRAINT flights_check CHECK ((scheduled_arrival > scheduled_departure)),
                    CONSTRAINT flights_check1 CHECK (((actual_arrival IS NULL) OR ((actual_departure IS NOT NULL) AND (actual_arrival IS NOT NULL) AND (actual_arrival > actual_departure)))),
                    CONSTRAINT flights_status_check CHECK (((status)::text = ANY (ARRAY[('On Time'::character varying)::text, ('Delayed'::character varying)::text, ('Departed'::character varying)::text, ('Arrived'::character varying)::text, ('Scheduled'::character varying)::text, ('Cancelled'::character varying)::text])))
                );

            seats
            --pk seat_no&aircraft_code => одно место - один пассажир
            --определяет схему салона КАЖД модели самолета(схема мест в салоне(кол-во мест и распределение по классам))
                CREATE TABLE seats (
                    aircraft_code character(3) NOT NULL,
                    #кажд место имеет свой номер
                    #схема данных не контролирует что места в посадочных талонах соответствуют имеющимся в салоне
                    seat_no character varying(4) NOT NULL,
                    fare_conditions character varying(10) NOT NULL,
                    CONSTRAINT seats_fare_conditions_check CHECK (((fare_conditions)::text = ANY (ARRAY[('Economy'::character varying)::text, ('Comfort'::character varying)::text, ('Business'::character varying)::text])))
                );

            ticket_flights
            --перелет
            --связывает КАЖД Ticket(s) с Flight(s) идентифицируясь их pk(номерами)
                CREATE TABLE ticket_flights (
                    ticket_no character(13) NOT NULL,
                    flight_id integer NOT NULL,
                    fare_conditions character varying(10) NOT NULL,                                 #класс
                    amount numeric(10,2) NOT NULL,                                                  #стоимость
                    CONSTRAINT ticket_flights_amount_check CHECK ((amount >= (0)::numeric)),
                    CONSTRAINT ticket_flights_fare_conditions_check CHECK (((fare_conditions)::text = ANY (ARRAY[('Economy'::character varying)::text, ('Comfort'::character varying)::text, ('Business'::character varying)::text])))
                );

            tickets
            --билет
            --ВСЕ Ticket(s)(пассажиры) уникальны
            --КАЖД Ticket(s) ВКЛЮЧ один|неск Tickets_flight(s)
                --неск if:
                    --нет прямого рейса между пунктами(Airports|?Airports.city)
                    --билет туда-обратно
            --passager_id & passager_name != const => нельзя однозначно найти билеты одного пассажира
                CREATE TABLE tickets (
                    ticket_no character(13) NOT NULL,                  #уникален
                    book_ref character(6) NOT NULL,                    #номер брони
                    passenger_id character varying(20) NOT NULL,       #номер удостоверения личности
                    passenger_name text NOT NULL,                      #first_name&last_name
                    contact_data jsonb                                 #контакты
                );

        ПОСЛЕДОВАТЕЛЬНОСТИ
            flights_flight_id_seq
                CREATE SEQUENCE flights_flight_id_seq
                    START WITH 1
                    INCREMENT BY 1
                    NO MINVALUE
                    NO MAXVALUE
                    CACHE 1;
        FUNCTIONS
            now
                --принадлеж Bookings
                --позиция среза ПРИНАДЛЕЖ Bookings(Bookings.now)(bookings?bookings.now?(видимо в книге опечатка))
                --может использоваться now() на реальной бд
                --val fx определяет текущую версию бд(на момент среза)
    суммарный размер схемы bookings около 1.3 гб => возможно остальное в схеме public
УСТАНОВКА ДЕМО БД
    edu.postgrespro.ru/demo-[small|medium|big].zip
    #данные за месяц|3мес|12мес, файл [21|62|232]mb,бд - [280|702|2638]mb
файлы содержат логический бекап бд demo, созданный pg_dump
#if уже СУЩ бд demo - она будет удалена и заменена на версию из бекапа
владельцем demo станет пользователь выполнивший восстановление
pg_dump
#утилита для бекапа бд
    LINUX
        $ sudo -su
        #переключиться на пользователя postgres
        $ wget https://edu.postgrespro.ru/demo-small.zip
        #скачать дамп бд
        $ zcat demo-small.zip | psql
        #видимо распаковать и отдать psql
    WIN
        #по идее рабочая папка psql должна совпадать с расположением дампа -> думаю востановиться можно из любого каталога => permission denied при доступе к C:
        скачать бд
        распаковать *.sql в C:\Program Files\PostgreSQL\12
        psql=> postgres# \i <dumb_name>.sql
	Arch
		скопировать бд в /var/lib/postgres
		psql=> postgres# \i <dumb_name>.sql

ПРЕДСТАВЛЕНИЯ(VIEWS)
#НЕСОДЕРЖ никаких данных владельца, автоматом выбирает данные из других таблиц
CREATE VIEW <view_name>
    AS SELECT *
    FROM ...
    WHERE ...;
ОТНОШЕНИЯ
    таблицы
    представления
    последовательности
походу вместо точечной нотации используется _
#~seats.fare_conditions.check
seats_fare_conditions_check