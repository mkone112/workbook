ТЕРМИНОЛОГИЯ
    tkinter
    # От tk interface
    widget
    # Window gadget
tcl/tk
# Pl/инструмент создания GUI
# Кроссплатформенный
HISTORY
    2.X
    # Tkinter
    3.X
    # В соотв с PEP8 tkinter
СПРАВКА
    unix man-pages tcl/tk
    # ?⊃ ∀ UNIX-based сис-ме в разделе n|3tk
    # Так-же доступны на http://tcl.tk/
        # Разделы:
            # Tcl.tk/man/tcl8.5/
        # Виджеты & комманды
            # Tcl.tk/man/tcl8.5/TkCmd/contents.htm
        # Общие опции виджетов
            # Tcl.tk/man/tcl8.5/TkCmd/options.htm
tkinter
# Lib - интерфеис(достаточно прозрачныи) к tcl/tk
# Tk GUI API (Tkinter в python 2.x) реализовывает переносимый gui с присущим для конкретной ос видом/поведением
# Как и tcl/tk by def поддерживается в:
    Windows(по крайней мере 7+)
    OSX
    Linux
    # Не уверен насчет ∀ дистров
# Де-факто стандарт API-интерфейс
# Событийно-ориентированна
# Походу ∀ инструкции передаются интерпритатору tcl/tk & большая часть работы exe в нем
    # Создает 4 окна
    from tkinter import Tk
    ...
    for i in range(2):
        Tk()
    root = Tk()
    root.mainloop()



СОБЫТИЙНО-ОРИЕНТИРОВАННЫЕ ПРИЛОЖЕНИЯ
# ⊃ main loop обработки событии


ФУНКЦИИ ОБРАТНОГО ВЫЗОВА
# Для создания внутристрочных fx обратного вызова можно исп lambda
    # -> логика обработки щелчка находится прямо в вызове(обеспечивает кодовую близость)
# Откладывает выполнение обработчика до возникновения события
    # Examples
        # Создание кнопки, по щелчку выводящая в консоль msg
        # Работает и в IDLE
            import sys
            from tkinter import Button, mainloop    # Tkinter в 2.X
            # Создание <tkinter.Button object .<number(?id)>>
            # Сохранение obj в var не обязательно, команда приводит к открыти окна tk
            # Вызов создающий кнопку
            # Регистрируем обработчик обратного вызова, передав fx сгенерированной lambda в ключевом arg command
            x = Button(
                text = 'Press me',
                command=(lambda:sys.stdout.write('Hello\n')))
            # Создает кнопку в окне
            # Видимо сборка эл-тов gui
            x.pack()
            # М.б. необязателен в консольном режиме
            mainloop()
        # Рекурсивное создание кнопок
            from tkinter import Button
            def func():
                y = Button(
                    text='Newbutton',
                    command=func)
                y.pack()
            func()
    # Еще пример
        from tkinter import Button
        # Создает окно без кнопки
        Button(text='',command=None)
        # Создает кнопку
        Button(text='',command=None).pack()
        # Добавляет еще кнопку
        Button(text='',command=None).pack()
    .mainloop(n=0)
    # Run the main loop of Tcl
# Examples
    # Создание новой кнопки, указание текста и fx обратного вызова
    from tkinter import *
    widget = Button(text='Press me', command=func)
МЕТОДЫ
    
КЛАССЫ

    Tk()
    # Base class ∀ Tkinter app
    # Создание этого класса запускает интерпритатор tcl/tk и создает(но не отображает) базовое окно app
    # Methods
        .after(<latency>, callable)
        # Позволяет запуск нескольких интерпритаторов(!не окон) tcl/tk
            # Исп краине редко, для созданиия дополнительных окон исп Toplevel
        # При исп нескольких интерпритаторов требуется следить чтобы obj использовались только в родительском
        # Запуск callable с заданнои <latency> в фоне(асинхронно?)
            <latency>:int:<msec>
            # 
        # При многократном вызове вроде запускает несколько интерпретаторов
            ...
            >>
            root.after(0, root.mainloop)
                after# 0         # ?не уверен что нумерация начинается с нуля(проверить)
                аfter# 1
                ...
        # Examples
            root0 = Tk()
            root1 = Tk()
            root0.after(500, root.mainloop)
            # Без вызова этого метода напрямую, интерфеис не отобразится
            root1.mainloop()
            
        .mainloop()
        # Создает главный цикл обработки событии
        # Отображает созданный интерфеис
        
        
        .quit()
        # Явныи выход из интерпритатора tcl/tk & завершения main loop
        
        .__repr__()
        # >> '<tkinter.Tk object .>'
        
        .__str__()
        # >> '.'
        
        
    ВИДЖЕТЫ
    # Визуальные контролы ~ графические элты управления
    # Стандартизированные компоненты GUI для взаимодеиствия
    # Создаются конструктором соотв класса
        <Widget_class>([master=]<Parent_widget>,...)
        # 
            master
            # Альтернатива первого позиционного arg
                <Parent_widget>
                # Виджет в которыи будет помещен создаваемыи виджет
                # By def главное окно приложения(видимо экз Tk)
            font
            # Шрифт
            
            bg
            # Цвет фона виджета
            
            activebackground
            # Хз
            
            command
            # Комманда exe при активации виджета(fx обратного вызова)
        # Полныи lst ⊃ args
            # Man options:https://www.tcl.tk/man/tcl8.5/TkCmd/options.htm
            # Man-страницы соотв виджета, напр man button(разделы "STANDART OPTIONS" & "WIDGET-SPECIFIC OPTIONS":
                # Http://www.tcl.tk/man/tcl8.5/TkCmd/button.htm
        
        МЕТОДЫ ВИДЖЕТОВ

            .config[ure](**kwargs)
            # Δ конфигурации ∃ виджета(при exe app)
            # ~ <widget>['<opt>'] = new_val
            # Examples
                btn0 = Button()
                btn0.config(text='send')
            
            .cget
            # Обратен .config[ure]()
            # Получение параметров виджета
            # ~ val = <widget>['opt']
            
            .destroy()
            # Уничтожение виджета & ∀ его потомков
            
            .grid_remove()
            # Скрытие виджета, с сохранение взаимного расположения виджетов
            # Examples
                from tkinter import Tk, Label, Button
                ...
                ...
                def hide_show():
                    if label.winfo_viewable():
                        label.grid_remove()
                    else:
                        label.grid()
                root=Tk()
                label = Label(text='I\'m here')
                label.grid()
                button = Button(command=hide_show, text='Hide/Show')
                button.grid()
                root.mainloop()
            .grid()
            # Восстанавливает скрытый виджет(см .grid_remove())
                    
            .winfo_viewable()
            # Видимо >> True If (виджет отображается)
                
            .grap_*
            # Методы семейства grab_ ∃ для управления потоком события -> Виджет, захватившии поток получает ∀ события app|window
                
                .grab_set()
                # Передать поток событии виджету
                
                .grab_set_global()
                # Передать глобальный поток событии виджету -> получает ∀ события на дисплее
                # Исп с осторожностью тк другие виджеты не будут получать события
                
                .grab_release()
                # Освободить поток событии
                
                .grab_status() -> None | "local" | "global"
                # >> текушии статус потока событии
                
                .grab_current()
                # >> виджет получаюшии поток
        
            .focus_*
            # Управления фокусом клавиатуры - виджет ⊃ фокус получает ∀ события клавиатуры
                .focus()
                .focus_set()
                # Передать фокус виджету
                
                .focus_force()
                # Передать фокус даже if app ⊅ фокус
                # Может раздражать пользователеи
                
                .focus_get()
                # >> Виджет ⊃ фокус If (хоть один виджет ⊃ фокус) Else None
                
                .focus_displayof()
                #? >> Виджет ⊃ фокус, на дисплее ⊃ этот виджет If (такои ∃) Else None
                
                .focus_lastofor()
                # >> Виджет который получит фокус, когда фокус получит его окно
                
                .tk_focusNext()
                # >> Виджет который получит фокус следуюшим(обычно по Tab)
                # Порядок следования виджетов определяется {Xₙ} упаковки виджетов
                
                .tk_focusPrev()
                # .tk_focusNext() наоборот
                
                .tk_focusFollowsMouse()
                # Устанавливает что виджет получает фокус при наведении курсора
                    # Вернуть обычное поведение сложно
                    # Да и не логично вроде, тк эта группа виджетов ∃ для взаимодействия с клавиатурои
            
            
            СИСТЕМНЫЕ МЕТОДЫ
            # влияют на интерпритатор tcl/tk, а не виджеты напрямую(не виджет-специфичные) 
                
                ТАЙМЕРЫ
                # Позволяют отложить exe кода
                    .after(<ms>, <callable>)
                    #
                        ...
                        class Callable:
                            ...
                            # Без __name__ не пашет
                            __name__ = ''
                            ...
                            ...
                            def __call__(self):
                                print('hello')
                        ...
                        ...
                        obj = Callable()
                        root = Tk()
                        root.after(1000, obj)
                        root.mainloop()
                    
                    .after_idle(func)
                    # Exe fx после exe ∀ отложенных операций(обработки ∀ событии)
                    # По сути, тот-же .after(), но сам решает когда exe действие
                    # >> task_id который может быть исп в after_cancel
                    # Examles
                        # Здесь использования after_idle() логичнее .after()
                        ...
                        root = Tk()
                        btn = Button()
                        btn.pack()
                        # Exe после exe ∀ необходимых задач по созданию и отрисовке окна
                        root.after_idle(job)
                        root.mainloop()
                    # If задача тяжелая &| inf -> стоит исп .after() тк .after_idle никогда не дождется конца операции
                    
                    
                    .after_cancel(task_id)
                    # Отмена задания созданного .after_idle(?only)
                
                ####
                    .winfo_exists()
                    # Хз для чего, но >> except при вызове после .destroy | закрытия окна
                    
                    
                РАБОТА С ОЧЕРЕДЬЮ ЗАДАЧ
                # Exe отложенных задач(прорисовка/просчет расположения/... виджетов)
                    
                    .update()
                    # Обработка ∀ задач очереди
                    # Обычно исп при тяжелых расчётах, чтобы app сохраняло отзывчивость
                    # Examples
                        from tkinter import Tk, Button
                        import math
                        ...
                        ...
                        def hard_job():
                            # Иначе при закрытии >> _tkinter.TclError: can't invoke "update" command: app... has been destroyed
                            try:
                                x = 1000
                                while True:
                                    x = math.log(x) ** 2.8
                                    root.update()
                            # Хз какое except ловить
                            except:
                                ...
                        ...
                        ...
                        root = Tk()
                        btn = Button()
                        btn.pack()
                        root.after(500, hard_job)
                        root.mainloop()
                        
                    
                    
                    .update_idletasks()
                    # Exe задачи обычно откладываемые на потом при простое app
                    # Обычно исп после Δ состояния app & нужно мгновенное их отображение, без ожидания завершения сценария
                
                EXE tcl КОДА
                    
                    .eval(<str>)
                    # Exe str ⊃ код tcl pl
                    # Examples
                        from tkinter import Tk
                        ...
                        root = Tk()  
                        root.eval('package require tile; ttk::style theme use clam')
                        root.eval('ttk::button .b -text {ttk button}; pack .b')
                        root.mainloop()
                    
                    .evalfile()
                    # Exe код записанный в файл
                    
            
                
        .Button(master=None, cnf={}, **kwargs)
            # Button widget
        
        .Label()
        #просто надпись
        
        
        .Toplevel()
        # Создание дополнительных окон(окон верхнего уровня)
        # Обычно используется для создания многооконных программ|диалоговых окон
        # Methods
            title
            # Заголовок окна
            
            overrideredirect(<bool>)
            # Создание окон без обрамления
            # Указывает оконному менеджеру игнорировать это окно
            
            iconify()
            # Свернуть окно
            
            .deiconify()
            # Развернуть/показать окно
            # Противоположен .iconify() & .withdraw()
            
            .withdraw()
            # Сделать окно невидимым(спрятать)
            # ⌐ .deiconify()
            
            .minsize(width, height)
            # Min window size
            
            .maxsize(width, height)
            # Max window size
            
            
УПАКОВЩИКИ
# Без .pack() создатся несколько окон вместо одного окна с несколькими кнопками
упаковка
# Помещение одного элта(?виджета) в другой
    .grid()

EXAMPLES
    # Δ конфигурации виджета при exe app
        import time
        ...
        from tkinter import Tk, Button
        ...
        ...
        def button_clicked():
            button['text'] = time.strftime('%H:%M:%S')
        ...
        ...
        root = Tk()
        button = Button(root)
        button.configure(text=time.strftime('%H:%M:%S'), command=button_clicked)
        button.pack()
        root.mainloop()
    # >> цвет кнопки и его Δ при клике на кнопке
        from tkinter import
        ...
        from random import random
        ...
        ...
        def button_clicked():
            current_color = btn.cget('bg')
            btn.config(text=current_color)
            new_color = '#%0x%0x%0x' % (int(random() * 16), int(random() * 16), int(random() * 16))
            btn.config(bg=new_color, activebackground=new_color)
        ...
        ...
        root = Tk()
        btn = Button(root, command=button_clicked)
        btn.pack()
        root.mainloop()
    # Минимальное приложение
        from tkinter import Tk, mainloop
        root = Tk()
        root.mainloop()
    # Запуск нескольких интерпритаторов tcl/tk
        from tkinter import Tk
        ...
        root0 = Tk()
        root1 = Tk()
        root0.after(500, root.mainloop)
        root1.mainloop()

    # 
        from tkinter import Button, Tk
        ...
        ...
        def button_clicked():
            print('Click!')
        ...
        ...
        root = Tk()
        button0 = Button(bg="#2196f3", command=button_clicked)
        button0.pack()
        root.mainloop()
    # App захватывает глобальный поток и освобождает через 10сек
        from tkinter import Tk() 
        ...
        root = Tk()
        root.after(200, root.grab_set_global)
        root.after(10000, root.grab_release)
        root.mainloop()
    # Часы
        from tkinter import Tk, Label
        import time
        ...
        ...
        def tick():
            label.after(200, tick)
            label.config(text=time.strftime('%H:%M:%S'))
        ...
        ...
        root = Tk()
        label = Label(font='sans 20')
        label.pack()
        label.after_idle(tick)
        root.mainloop()
    