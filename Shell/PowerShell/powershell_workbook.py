alt+enter : fullscreen

%HomePath%
#домашняя dir

powershell поддерживает кучу unix команд
pwd
#print working directory
#работает в ps
cd
#Без параметров ~ pwd
#change directory
mkdir
#Unix|Win
rmdir
#удаление файла Win
del
#удаление win
copy
#копирование файла win
    copy <currentPath> <newPath>


get cli location

gcm <cli>


последовательно выполнить похожие команды
foreach ($c in 'makemigrations', 'migrate', 'createsuperuser') {py manage.py $c}
