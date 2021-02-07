STEPS
	git init
	git add <file>|--all
	git commit -m "msg"
	git remote add origin <....git>
	git push -u origin master
NOTES
	#∀ проект ⊃ одну ветвь по умолчанию
	#staged можно пропустить указав в repo конкретный файл
	#commit не происходит без message
	#поддерживает re
		*.txt
	#staged ⊃ информацию о next commit
	#при копировании repo копируется .git !⊃ working
	#файл в working=файл в .git=> файл commited
	#.gitignore можно вносить в .gitignore, но я не думаю что это ⊂ смысл т.к. тогда при переносе этот список потеряется
	#офф руководство: рекомендуется использовать git из оболочки в составе mSysGit вместо powershell, т.к. некоторые примеры могут работать некорректно в ps

SMARTGIT
	remove repo
	#только отключает repo от smartgit(~atom project) фс не затрагивается
	dark in journal - in remote repo
	#может редактировать commit msg
git	опции
	-C
	#сменить папку repo
	-с параметр-val
	#изменить параметры конфигурации
	-p
	#прокручивать ∀ вывод с помощью less
git commands
	add <file>|--all
	#добавить файлы/папки в repo
	#untracked->unmodified
	am
	#применить ∀ патчи из email
	archive
	#создать архив файлов
	bisect
	#бинарный поиск коммита
	branch
	#управление ветвями проекта
		git branch <branc_name>
		#создать новую ветвь
		git branch -a
		#просмотр текущих ветвей
	bundle
	#перемещение obj и ссылок в архиве
	checkout
	#переключение между ветвями
	#git->working
	cherry-pick
	#внести изменения в ∃ коммиты
	#перенести в master только определенные коммиты
	push
	#коммит на remote
		git push origin
	log
	#список коммитов
	clean
	#удалить все неотслеживаемые
	clone
	#создать копию remote repo в dir(видимо локальную)
	#создает каталог с именем repo, копирует туда(checkout) рабочую копию последней версии(⊃ last commit) и каталог .git
	#поддерживает
		http(s)
		git
		<user@server>:/(ssh)
	commit
	#сохранить изм в репозитории
	#staged->.git
	diff
	#посмотреть изм между коммитами
	#содержимое index и рабочего каталога => вывод содержимого lastcommit?
	fetch
	#скачать remote repo
	init
	#создать repo
	merge
	#слияние двух ветвей(ветвь с которой выполняется слияние м.б. удалена)
	#файлы удаленные в feature branch - удаляются в master при слиянии
		#слить изменения в <name> в текущую ветвь
	pull
	#подтягивание изменений(интегрировать remote с local)
	tag?
	#кажется можно добавить тег к коммиту и создать из него branch(а без этого?)
	worktree
	#управление деревьями разработки
	reset
	#unmodified->untracked
	
git аргументы

CONFIGS
	WIN
		Program Files
		users/<user_name>
		ProgramData
	Unix
		/etc/gitconfig
		#системный конфиг
git config
#утилита настройки параметров(⊃ внешиний вид)
#некоторые ключи могут ⊂ нескольких конфигах(∃ приоритеты)
	--system
	#работа с системным конфигом
	--list
	#список настроек(q выход)

.gitignore
	comments #
	∀ comment на отдельной строке
		<command> #comment -> err
	glog шаблоны
		.../
		#каталог
		*
		#{xn} символов
		?
		#один символ
		[abc]
		#один из char
		[0-9]
		#один char ⊂ интервалу
	  ПРИМЕРЫ
			#исключить ∀ файлы *.a, но не lib.a
				*.a
				!lib.a
			#исключить файл TODO
			  /TODO
			  #~TODO
			#исключить содержимое каталога
			  build/
			#исключить ∀ *.txt ⊂ doc/
			  doc/**/*.txt