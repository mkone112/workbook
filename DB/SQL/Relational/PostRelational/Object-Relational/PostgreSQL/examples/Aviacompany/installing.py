УСТАНОВКА ДЕМО БД
    edu.postgrespro.ru/demo-[small|medium|big].zip
    #данные за месяц|3мес|12мес, файл [21|62|232]mb,бд - [280|702|2638]mb
файлы содержат логический бекап бд demo, созданный pg_dump
#if уже СУЩ бд demo - она будет удалена и заменена на версию из бекапа
владельцем demo станет пользователь выполнивший восстановление

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