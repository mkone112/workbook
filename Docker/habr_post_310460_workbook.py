сокращения
	docker:d
ДОКЕР
#авто деплой и управление app в среде виртуализации на уровне ос
#позволяет "упаковать" app с env и зависимостями в контейнер(стандартизированный модуль для разработки)
#предоставляет среду управления контейнерами
#деплой в песочнице(контейнере) для запуска на целевой ос
#взлетел мнгновенно в ~14, создан лет за 10 до этого, сделал контейнеры распространеннее
#предоставляет стандартный api упрощающий исп контейнеров позволяя сообществу вместе работать на lib'ами для работы с контейнерами
#эффективен, портативен, более зависим от ос
docker
	run [OPTION_0 val OPTION_1 val ...] IMAGE [COMMAND] [ARG...]
	#OPTIONS:<type>:<default>
		--add-host:list
		#добавить кастомное отображение host:ip
		
		-a, --attach:list
		#привязаться к STDIN|STDOUT|STDERR
				
		--blkio-weight:uint16:0
		#блокировка IO(относительно) 10-1000, 0 - откл
		--blkio-weight-device:list:[]
		#block IO weight(relative device weight)
				
		--cap-add:list
		#add linux capabilities
		--cap-drop:list
		#drop linux capabilities
				
		--cgroup-parent:string
		#опциональный родитель cgroup для контейнера
				
		--cidfile:string
		#записать container ID в файл
				
		--cpu-period:int
		#предел cpu cfs периода
		--cpu-quota:int
		#предел cpu cfs квоты
		--cpu-rt-period:int
		#предел cpu real-time период(мс)(видимо для O(1) scheduler)
		--cpu-rt-runtime:int
		#предел cpu real-time runtime(время работы?)(мс)(видимо для O(1) scheduler)
		-c, --cpu-shares:int
		#доля ресурсов cpu достающихся группе(?)(относительная величина)
		--cpus:decimal
		#число цп
		--cpuset-cpus:string
		#cpus на которых разрешено exe (0-3, 0, 1)
		--cpuset-mems:string
		#mems на которой разрешено exe (0-3, 0, 1)
				
		-d, --detach
		#запуск контейнера в фоне и вывод container ID
		#detached mode, контейнер будет работать даже if терминал закрыт
		
		--detach-keys:string
		#переназначить ключевую {xn}(?) для отключения контейнера
				
		--device:list
		#добавить устройство хоста
		--device-cgroup-rule:list
		#добавить правила ⊃ разрешенный список устройств в cgroup
				
		--device-read-bps:list:[]
		#ограничить read rate(bytes/sec) устройства
		--device-read-iops:list:[]
		#~--device-read-bps, iops
		--device-write-bps:list:[]
		#~--device-read-bps
		--device-write-iops:list:[]
		#~--device-read-iops
				
		--disable-content-trust:bool:true
		#пропуск image verification
				
		--dns:list
		#custom dns
		--dns-option:list
		#
		--dns-search:list
		#custom dns search domains
		--domainname:string
		#container NIS domain anme
				
		--entrypoint:string
		#перезапись ENTRYPOINT образа by def
		-e, --env:list
		#env v
				
		--expose:list
		#выставить порт|диапазон портов
				
		--gpus:gpu-request
		#gpu для добавления в контейнер
			'all'
			#проброс ∀
				
		--group-add:list
		#add additional groups to join
				
		--health-cmd:string
		#check health
		--health-interval:duration:0s
		#период между check health(ms|s|m|h)
		--health-retries:int
		#число {xn} неудач до отчета о unhealthy
		--health-start-period:duration:0s
		#начальный период инициализации контейнера до начала health-retries (ms|s|m|h)
				
		-h, --hostname:string
		#container host name
				
		--init
		#run an init inside the container that forwards signals and reaps processes
				
		-i, --interactive
		#оставить STDIN открытым даже if не подключен
				
		--ip:string
		#ipV4 адрес
		--ip6:string
		#ipV6 адрес
				
		--ipc:string
		#режим IPC
				
		--isolation:string
		#технология изоляции контейнера
				
		--kernel-memory:bytes
		#kernel memory limit
				
		-l, --label:list
		#мета-данные для контейнера
		--label-file:list
		#read in a line delimited file of labels
				
		--link:list
		#ссылка на другой контейнер
		--link-local-ip:list
		#ipv4/6 ссылка на локальный контейнер
				
		--log-driver:string
		#драйвер логгирования для контейнера
		--log-opt:list
		#опции драйвера логгирования
				
		--mac-address:string
		#mac контейнера
				
		-m, --memory:bytes
		#лимит mem
		--memory-reservation:bytes
		#mem soft limit
		--memory-swap:bytes
		#предел подкачки = mem + swap
			'-1'
			#unlimited swap
		--memory-swappiness:int:-1
		#tune container memory swappiness(0-100) видимо % в swap|mem
				
		--mount:mount
		#примонтировать к контейнеру фс
				
		--name:string
		#имя контейнера
				
		--network-alias:list
		#network-scoped alias для контейнера
				
		--no-healthcheck
		#отключить ∀ контейнер-специфичную HEALTCHECK
				
		--oom-kill-disable
		#disable OOM Killer
				
		--pid:string
		#PID ns to use
		--pids-limit:int:-1
		#container pids limit
			-1
			#unlim
				
		--platform:string
		#установить платформу if сервер совместим с мн-вом платформ
		
		--privileged
		#дать доп права контейнеру
		
		-p, --publish:list
		#опубликовать порт контейнера хосту
		-P, --publish-all
		#publish all exposed ports to random ports
		
		--read-only
		#mount container's root fs as ro
		
		--restart:string:"no"
		#политика перезапуска исп if контейнер ∃
		
		--rm
		#авто удаление контейнера при выходе
		
		--runtime:string
		#среда exe для контейнера
		
		--security-opt:list
		#security options
		
		--shm-size:bytes
		#размер /dev/shm
		
		--sig-proxy:bool:true
		#прокси получает сигналы в процессе
		--stop-signal:string:"SIGTERM"
		#сигнал для остановки контейнера
		--stop-timeout:int
		#таймаут остановки контейнера(sec)
		
		--storage-opt:list
		#storage driver options
		
		--sysctl:map:map[]
		#Sysctl options
		
		--tmpfs:list
		#монтировать tmpfs dir
		
		-t, --tty
		#выделить псевдо-TTY
		
		--ulimit:ulimit:[]
		#ulimit options
		
		-u, --user:string
		#username|UID
		#format: <name|uid>[:<group|gid>]
		
		--userns:string
		#username для использования
		#чем отличается от -u(?)
		
		--uts:string
		#UTS ns to use
		
		-v, --volume:list
		#привязать точку монтирования к тому
		
		--volume-driver:string
		#опциональный драйвер тома для контейнера
		
		--volumes-from:list
		#монтировать тома из указанных контейнеров
		
		-w, --workdir:string
		#workdir в контейнере
	
	OPT COMBINATIONS
		-it
		#подключение интерактивного tty в контейнер
		
		
tty
#абстракция
#подсисма unix
#исп одного терминала несколькими процессами


eng:consecutive:последовательно
eng:expose:выставить	


iops
#io/sec


CFS
#Completely Fair(справедливый) Scheduler
#исп red-black дерево с ключем
	wait-runtime
	#∀ процесса
	#число недоработанных(>0)/переработанных(<0) нс
	
	
КОНТЕЙНЕР
#в отличие от vm создают меньший оверхед
#предоставляют схожий с vm уровень изоляции, но за счет исп низкоуровневых механизмов ос хоста с меньшей нагрузкой
#позволяет запускать app в процессе с изолированием ресурсов
#создаются на основе образа из запускают app

DOCKER DAEMON
#фоновый сервис на хосте для взаимодействия с клиента
	создает контейнеры
	запуск контейнеров
	удаляет контейнеры

DOCKER CLIENTS
	docker
	#консольный
	Kinematic
	#gui
	#⊂ docker toolbox
	#https://kitematic.com/
	
DOCKER HUB
#регистр образов

можно создать свой регистр образов


УСТАНОВКА
	Docker Community Edition
		Ubuntu
			#подключение репозитория Docker для доступа к новейшим версиям
				sudo apt update
				#установка пакетов используемых apt для доступа по HTTPS
				sudo apt install apt-transport-https ca-certificates curl software-properites-common
				
				#введем ключ GPG ⊂ docker repo чтобы убедиться в действительности загруженной версии
				curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
				#добавим источник дистра
				sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
				#обновим бд пакетов инфой о пакетах docker из новой репы
				sudo apt update
				#убедимся что ставим docker из репы docker а не ubuntu
				apt-cache policy docker-ce
				#установим дист
				sudo apt install docker-ce
				#убедимся что процесс пашет
				sudo systemctl status docker
			ИСПОЛЬЗОВАНИЕ DOCKER БЕЗ SUDO
			#клиент требует принадлежности пользователя к docker|sudo
				sudo usermod -aG docker ${USER}
				su - ${USER}
			#проверим
				id -nG
	PYTHON
		sudo apt-instal
		nano ~/.bash_aliases
			alias py=python3
			alias pip=pip3
			source ~/.bash_aliases
			
		sudo apt install pip3
		
		
BusyBox
#набор unix-утилит 
#способ упаковки утилит 
	ls
	echo
	#по идее эхо возвращает посланную команду
	sh
	#оболочка sh
	uptime
	#возвращает текущий uptime
	exit 
	#выход
ПРАКТИКА
	#проверим ∀ ли пашет
		docker run hello-world
	#скачаем образ busybox из регистра docker и сохраним его локально
		docker pull busybox
	#просмотрим список образов в сисме
		docker images
	#запустим контейнер с образом busybox
		#docker-клиент ищет образ, загружает контейнер, запускает указанную комманду в контейнере и выходит из него
		#при успехе не выведет ничего тк команда не указана(пустая)
		docker run busybox
	#пошлем команду	
		docker run echo "hello from busybox"
			>>
			hello from busybox
	#вывод ∀ запущенных контейнеров
		docker ps
		#⊃ поля
			CONTAINER ID
			IMAGE COMMAND
			CREATED
			STATUS
			PORTS
			NAMES
	#∀ запускавшиеся контейнеры	
		docker ps -a
	#запуск sh в контейнере, позволяет принимать мн-во команд
		docker run -it busybox sh
	#при запуске d создает создает новый контейнер -> Δ не сохраняются
		docker run -it busybox sh
		rm -rf /bin
		ls	>> ls not found
		exit
		docker run -it busybox sh
		ls	>> ok
		

УДАЛЕНИЕ КОНТЕЙНЕРОВ
#docker ps -a -> остатки завершенных контейнеров мусор, жрут место
	docker 
		rm:list
		#удаление контейнеров
			docker ps -a
			...
			docker rm 305297d7a235 ff0a5c3750b9
		#исп v
			docker rm $(docker ps -a -q -f status=exited)
				-q
				#возвращать только численные id
				-f
				#фильтрация на основе условий
		--rm
		#флах автоматического удаления контейнера
		rmi
		#удаление ненужных образов

IMAGE
#образ
#схема app, основа контейнеров

ДЕПЛОЙ STATIC
	#скачаем заранее созданный образ с веб-приложением
	#docker run позволяет скачать образ напрямую(не новость)
		#тк образ ∃ локально - будет загружен
		docker run prakhar1989/static-site
			>> Nginx is running
	#как проверить, на каком порту, как достучаться до контейнера из хоста
	#в данном случае клиент не открывает никакие порты 
		-> нужно перезапустить docker run чтобы сделать порты публичными
		#заодно сделаем так чтобы терминал не был прикреплен к запущенному контейнеру(контейнер будет работать даже при закрытии терминала)
		docker run -d -P --name static-site prackhar1989/static-site
			>> <id>
			#-P : ∀ открытые порты - публичны и случайны
			#--name: имя контейнера
	#теперь можно увидеть порты с помощью docker port [container-name]
		docker port static-site
ДЕПЛОЙ СТАТИЧНОГО САЙТА НА AWS


ДЕПЛОЙ ДИНАМИЧНЫХ ВЕБ-APP НА EC2 С ИСП Elastic Beanstalk и Elastic Container Service


МЫСЛИ О ИСОПЛЬЗОВАНИИ VM ИЗ WIN ПО SSH
#	ip ~ 
#	ifconfig
#
#sudo apt install openssh-server
#
#settings -> apps -> ... -> openssh
#C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe C:\Users\mkone\VM\kubuntu64\kubuntu64.vmx nogui
#
#ssh root@192.168.1.202
#172.17.0.2
#адрес вроде адаптера wmware