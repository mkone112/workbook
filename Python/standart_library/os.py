os
#по сути запускает nt на win и posix На других ос
#СОДЕРЖИТ дескрипторные файлы

    .name:'posix'|'nt'|'mac'|'os2'|'ce'|'java'
    #имя ос
    .environ
    

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
    .walk() ->  <generator object walk>
    #старндартная генераторная(yield+yield from) fx рекурсивного прохода по каталогам -> не требует ожидания обхода всего дерева, а выдает результаты по мере поступления
    #возвращает кортеж кортежей вида
        (('dir_name',(contain_dir,...),[files,...]),...)
        #на КАЖД уровне дерева каталогов
    #проход всех директорий с '.' и выводом всех файлов на 'g'
        for (root, subs, files) in os.walk('.'):
            for name in files:
                if name.startswith('g'):
                    print(root, name)

          >> .\demos gui_demo_gtk.py
            .\demos gui_demo_pyside.py
            .\demos gui_demo_qt4.py
            .\demos gui_demo_tk.py
            .\demos gui_demo_wx.py

    .system
    #ПРИНАДЛЕЖ nt
    #запуск команды оболочки в отдельном процессе, ждет завершения процесса прежде чем возобновить поток выполнения
    #возвращает 0 в случае успеха, 1 в случае неудачи, например отсутсвие команды;не возвращает вывод и не открывает консольные окна
        os.system('notepad')    >> открывает notepad и ждет
        os.system('cmd')       >> idle:ждет;из файла - запускает cmd
        os.system('dir')  >> 0