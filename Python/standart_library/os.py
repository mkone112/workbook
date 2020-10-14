os
#по сути запускает nt на win и posix На других ос
#СОДЕРЖИТ дескрипторные файлы

    .name:'posix'|'nt'|'mac'|'os2'|'ce'|'java'
    #имя ос
    
    .environ:dict
    #mutable словарь v окружения
    #obj сопоставления(proxy?) с dict v пользовательской среды
    #позволяет добавлять/удалять v окружения
    
    
    .getenv(key, default=None)
    #получение v окружения, в ОТЛ от .environ !>> exept при !СУЩ v
    #~ os.environ.get("key")
    
    
    .getlogin()
    #Unix:username вошедшего в терминал
    
    
    .getpid() -> current_process_pid
    
    
    .uname()
    #информация об ос
    #>> obj ВКЛЮЧ attrs
        .sysname
        #os name
        
        .nodename
        #имя машины в сети
        #?определяется реализацией
        
        .release
        #?релиз
        
        .version
        
        .machine
        #?id машины
    
    .access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
    #проверка доступа текущего пользователя к obj
    #?флаги(mode?)
        os.F_OK
        #obj СУЩ
        os.R_OK
        #obj доступен на чтение
        os.W_OK
        #obj доступен на запись
        os.X_OK
        #obj доступен на exe
    
    
    .chdir(path)
    #смена текущей dir
    
    
    
    .chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
    #ИЗМ прав доступа к obj
        mode
        #oct int
    
    
    .chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)
    #Unix:ИЗМ id владельца & группы
    
    
    .getcwd() -> current_working_dir
    
    
    .link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
    #создание жеской ссылки
    
    
    .listdir(path=".")
    #список файлов и dirs в директории
    
    
    .makedirs()
    #
    
    
    .mkdir(path, mode=0o777, exist_ok=False)
    #создание dir с созданием промежуточных директорий
    
    
    .remove(path, *, dir_fd=None)
    #?удаление файла
    
    
    .rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    #переимонование obj
    #без замены в случае СУЩ?
    
    
    .renames(old, new)
    #переименование с создание промежуточных dirs
    #без замены в случае СУЩ?
    
    
    .replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    #переимонование с принудительной заменой
    
    
    .rmdir(path, *, dir_fd=None)
    #удаление пустой dir
    
    
    .removedirs(path)
    #рекурсивно(?{xn}) удаляет директории в пути от последней пока они пусты
    
    
    .putenv()
    #
    
    
    .symlink(source, link_name, target_is_directory=False, *, dir_fd=None)
    #создать симлинк
    
    
    .startfile()
    #
    
    
    .sync()
    #Unix:запись ВСЕХ данных на диск
    
    
    .truncate(path, length)
    #обрезать файл до length
    
    
    .utime(path, times=None, *, ns=None, dir_fd=None, follow_symlink=True)
    #ИЗМ времени последнего доступа/ИЗМ файла
        times:(access:secs, mod:secs)
        #исключает ns
        
        ns:(access:nsecs, mod:nsecs)
        #исключает times
    
    
    
        
    .popen(cmd,mode='r',bufferung=-1)
    #запуск команд оболочки и(в отличие от .system) предоставляет интерфейс(подобный файлам) для чтения/записи в их стандартные потоки данных в отдельном процессе,подключается к потокам вывода программы
    #похож на fileobj но значетельно отличается интерфейсами
        f = os.popen('dir')
        f   >> <os._wrap_close obj ...>
        f.readline()    >> ' ’®¬ ў гбва®©бвўҐ C \xadҐ Ё¬ҐҐв ¬ҐвЄЁ.\n'
        bytes(f.readline(),'866')   >> build\n      #Не сработает для кириллицы
        #or
        os.popen('chcp')    >> 866
        os.popen('chcp 65001')
        os.popen('chcp')    >> 65001    #кодировка сохраняется для одного процесса
            #как это закрепить?
        #2.X кажется имеет свой итератор
        f = os.popen()
        f is iter(f)    >> True
        f.next()        >> #работает
        next(f)         >> #работает
        #3.x не имеет своего итератора, но умеет next
        f = os.popen('dir')
        f   >> <os._wrap_close obj ...>
        f.__next__()    >> #работает
        next(f)       >> TypeErr: '_wrap_close' obj is not an iterator
        f is iter(f)    >> False #действительно не итератор
        #истощается ?
            f = os.popen('chcp')
            f.readline()        >> 'Active character encoding 866'
            f.readline()        >>  ''
            f.seek(0)           >> ''

        os.popen('systeminfo')      >> запускает консоль(внутри py.exe),но сжирает весь вывод - результат не отображается без ручного вывода
    #выполняет команду, возвращает <os._wrap_close obj> и продолжает выполнение в отличие от os.system
    #может использоваться для
        чтения результатов сконструированной командной строки фиксирующей продолжительнсть выполнения кода(timeit?)(лутц:глава 21)
        сравнение выводов тестируемых сценариев(лутц: глава 25)
    
    
    .open() -> int  #descriptor
    #open a file a low level io
    
    .walk(top, topdown=True, onerror=None, followlinks=False) ->  <generator object walk>
    #генерация имен файлов дерева каталогов 
        topdown
            topdown=True
            #генерация сверху вниз
    #для КАЖД каталога >> (path, dirs_list, files_list)
    #старндартная генераторная(yield+yield from) fx рекурсивного прохода по каталогам -> не требует ожидания обхода всего дерева, а выдает результаты по мере поступления
    #возвращает кортеж кортежей вида
        (('dir_name',(contain_dir,...),[files,...]),...)
        #на КАЖД уровне дерева каталогов
        
    
    .system(command) -> int
    #ПРИНАДЛЕЖ nt
    #запуск команды оболочки в отдельном процессе, ждет завершения процесса прежде чем возобновить поток выполнения
    #возвращает 0 в случае успеха, 1 в случае неудачи, например отсутсвие команды;не возвращает вывод и не открывает консольные окна
        os.system('notepad')    >> открывает notepad и ждет
        os.system('cmd')       >> idle:ждет;из файла - запускает cmd
        os.system('dir')  >> 0
    
    
    .urandom(n)
    #>> n случайных байт
    #исп в криптографических целях
    
    
    .path
    #модуль
    #работа с путями