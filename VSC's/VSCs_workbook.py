УЧЁТ ВЕРСИИ
    При исп Subversion|CVS|RCS с Python
        '''
            Module docstring
            
        '''
        
        version__ = "$Revision: 68852 $"
        # $Source$


ЛОКАЛЬНЫЕ СКВ
#хранят записи о всех изменениях в файлах тем самым осуществляя контроль ревизий

	RCS
	#распространяется с компами(mac?)
	#хранит наборы патчей(различий версий)


ЦЕНТРАЛИЗОВАННЫЕ CVS
#поддерживает командную разработку
#цскв
	CVS
	Subversion(SVN)
	Perforce
#сервер содержит все версии файлов
#по сравнению с локальными скв
	каждый разраб в определенной степени знает чем заняты другие
	админы имеют полный контроль за доступом
	#обслуживание одного сервера проще чем группы локальных машин
#недостатки
    единая точка отказа
    
    
РАСПРЕДЕЛЕННЫЕ СКВ
#~РСКВ~PVCS
	Git
	Mercurial
	Bazaar
	Darcs
#клиенты скачивают весь реп, а не отдельные файлы/версии/снапшоты
#многие рскв могут одновременно взаимодействовать с неск удаленными репами => можно работать с различными группами людей, применяя несколько подходов в разработке, напр:
	иерархические модели
	#что невозможно в цскв
#постепенно замещают централизованные

