походу команды можно объединять
	docker run -i -t	>> docker run -it
	
whoami  >> user name
pwd
#print working directory
#работает в ps
cd
#Без параметров ~ pwd
#change directory
rm
#
    #удалить файл
        rm
    #удалить каталог
        rm -r
mv
#перемещение файлов
    mv <currentPath> <newPath>
mkdir
#Unix|Win
cp
#копирование файлов Unix

To suppress error output in bash, append 2>/dev/null to the end of your command. This redirects filehandle 2 (STDERR) to /dev/null. There are similar constructs in other shells, though the specific construct may vary slightly
Redirect the error message (STDERR) to /dev/null:
    root@ubuntu:~$ cp /srv/ftp/201*/wha*/*.jj ~/. 2>/dev/null

supress all output and errors
    &> /dev/null


args+=(val) скобки точно нужны для добавления к элту массива, иначе добавится к первому элту

https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash

declare -A animal=( ["moo"]="cow" ["woof"]="dog")
${animal['moo']}
