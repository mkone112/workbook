"""
Проход всех директорий с '.' и выводом всех файлов на 'g'.
"""
for (root, subs, files) in os.walk('.'):
    for name in files:
        if name.startswith('g'):
            print(root, name)

"""
>>
    .\demos gui_demo_gtk.py
    .\demos gui_demo_pyside.py
    .\demos gui_demo_qt4.py
    .\demos gui_demo_tk.py
    .\demos gui_demo_wx.py
"""