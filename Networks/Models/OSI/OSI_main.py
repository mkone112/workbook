Layers
	Data Link Layer
	#(2)канальный/передачи данных
	#исп
		доставка кадров между узлами	
		передача данных узла того же сегмента lan
		обнаружение/исправление err физического уровня
	#примеры
		Ethernet многоузловых lan
		PPP
		ADCCP
		#двухузловой(точка-точка)
	#кадры
		не пересекают границ сетевого сегмента
		передаются {xn} с обработкой кадров подтверждения отсылаемых обратно получателем
	#тк маршрутизация и глобальная адресация осущ на более высоких уровнях osi -> протоколы DLL сосредоточены на локальной доставке и адресации
	#заголовок кадры ⊃ аппаратные адреса отправителя и получателя
		#аппаратные адреса одноуровневые в отл от иерархических и маршрутизируемых addr -> ∀ часть адреса не указывает на принадлежность к ∀ логической|физической группе
	#if устройства пытаются исп среду одновременно -> коллизии кадров
		#протоколы DLL уменьшают/предотвращают их
	#многие протоколы DLL !⊃ подтверждения о приеме кадров, некоторые !⊃ checksums для проверки целостности кадра
	#в яп доступ через драйвер сетевухи
	#ос ⊃ интерфейс взаимодействия канального и сетевого уровноней
		ODI
		NDIS
	#длинна пакет ограничена MTU
	#подуровни
		MAC
		#media(medium) access Control
		#управление доступом к среде
		#регулирует доступ к разделяемой физической среде
		#адресация и управление доступом к каналам -> неск терминалов|точек доступа могут общаться в многоточечной сети(lan|man) эмулирует полнодуплексный логический канал связи
			#~протокол множественного доступа - деление одной среды передачи неск узлами
			#разделяемые физические среды
				шина
				кольцо
				сети с хабами/беспроводные
				сети с полудуплексным подключением точка-точка
		#предотвращает коллизии пакетов if режим конкурирующего доступа - метод доступа к каналу | зарезервированы ресурсы для создания логического канала(при исп метода доступа к каналу на основе метода кольцевого переключателя/разбиения среды на каналы)
		#механизм множественного доступа основан на схеме мультиплексирования
		#max используемый протокол множественного доступа основан на CSMA/CD используемым Ethernet
		#одно из расширений osi
		#нижний(интейфейс между LLC и физическим(первым) уровнем osi)
		#вроде стараются дать ∀ устройству свой
		#могут исп для доставки через мыльницы(повторители/хабы/свитчи)
		#не требуется при полнодуплексной связи точка-точка, но поля MAC-адреса ⊂ в некоторые протоколы точка-точка для совместимости
		LLC
		#logical link control
		#обслуживание сетевого уровня
		#верхний
	#fx
		получение доступа к среде передачи
		#требуется всегда кроме if реализована полносвязная топология
		выделение границ кадра
		#требуется всегда
		#возможные решения
			резервирование части {xn} обозначающей конец кадра
		аппаратная адресация
		#адресация канального уровня
		#исп if кадр могут получить неск адресатов
		#в lan всегда исп mac
		обеспечение корректности принимаемых данных
		адресация протоколов выше
		#при декапсуляции указание формата вложенного PDU(?) упрощает обработку -> чаще всего указывается протокол ⊂ в поле данных кроме if поле может ⊃ только один протокол