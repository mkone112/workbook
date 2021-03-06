#исп ip как уникальный адрес
		V4
		#4 байта
		V6
		#16байт
		#разделители :
			201:0ви8:85ф3:000:000:8ф2у:0370:7334
		#можно опускать ведущие нули(max 1 пропуск)
			fe80:0:0:0:0:0:0:1	->	fe80::1
#⊃ <номер сети> <номер узла>
#номер узла назначается независимо от локального адреса узла
#маршрутизатор ⊂ нескольким сетям -> ∀ его  порт ⊃ свой ip
#∀ узел может входить в неск сетей имея неск адресов ->
	IP адрес характеризует одно соедниение, а не один узел
#адрес изолированной сети ⊂ блокам
	10.0.0.0/8
	172.16.0.0/12
	192.168.0.0/16
#
	ТИПЫ АДРЕСАЦИИ
	#∃ два способа определеить сколько бит ⊂ маске, а сколько ip-адресу
		классовая адресация
		#INET
		#устарела
		#обычная запись без указания маски
		бесклассовая адресация
		#вытеснила INET во второй половине 90х
		#колво адресов опред маской подсети
			СРАВНЕНИЕ
			#запись вида 
				192.168.5.0/24 
				#заменяет указание диапазона адресов
				#CIDR-адрес
				#число после / - колво единичных разрядов в маске
					24 -> 11111111 11111111 11111111 00000000 -> 255.255.255.0
					#24 разряда - номер сети, остальные 32-24=8 под адреса хостов сети ->
						192.168.5.0.24
						#диапазон 192.168.5.1 - 192.168.5.254
						#адрес сети 192.168.5.0
							#формула
								ip.∀_компа_сети AND mask
								#адрес сети позволяет определить что компы в одной сети
						#широковещательный адрес сети 192.168.5.255
							#формула
								ip.∀_компа_сети OR NOT(mask)
							#восприниматеся ∀ компами сети как доп свой адрес -> пакет на этот адрес получают ∀ хосты сети как адресованный лично им
							#if на сетевой интерфейс хоста не явл маршрутизатором пакетов попадет пакет не предназначенный ему - он будет отброшен
						#в некоторых сисмах
							адрес сети
							широковещательный адрес
							#мб Δ
ОСОБЫЕ IP АДРЕСА
	if ∀ двоичные разряды = 1 -> пакет с таким назначением рассылается ∀ узлам этой сети(в которой находится источник)
	#ограниченное широковещательное msg(limited broadcast)
	if ∀ поле номера узла ⊃ только 1 -> пакет рассылается ∀ узлам сети с заданным номером сети
	#напр в сети 192.168.5.0 с маской 255.255.255.0 пакет с адресом 192.168.5.255 доставляется ∀ узлам сети
	#широковещательное сообщение(directed broadcast)
