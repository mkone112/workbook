поковырять параметры моделеи
#что пишется в бд, как с этим работать
	get_latest_by
		взаимодеиствие с
			order_with_respect_to
			ordering
что if модель ⊃ неск полеи дат?(latest)
разумеется на передачу '+<field_name>' кидается exept(напр <model>.objects.latest('+<field_name>'))

переписывание fx ~ командам manage.py бессмысленно
#⊃ возвращаемое val, в большинстве ~ друг другу параметры(порои самодокументирующиеся)


проверить поля в шаблоне при сохранении

поковырять команды manage.py с -v3

future
	отследить поток данных из формы -> МОЖНО ИСП ORM & ТУПОИ ПРОСМОТР БД
	#да по сути он исп ORM -> нет особого смысла в этом разбираться
	#| исп print_sql shell_plus/runserver_plus ⊂ django_extensions
	
	что происходит при указании UNIQUE в бд?
	#проверить на примере параметров полеи модели
	#это легко можно провернуть используя orm
	проверить поведение полеи с бд !~ sqlite
	#вероятно dj может не перекладывать часть fx(напр валидацию) на бд if она не ⊃ подобныи fx
		#особенно проверить эти поля(наверняка за их поведение отвечает какои-нибудь валидатор)
		unique
		unique_for_date
		unique_for_month
		unique_for_year
	
	просмотреть http запрос
	#не особо понял как это сделать -> firefox не отобразил POST запрос ->
		попробовать chrome?
		может это делает сам dj?(~подключению jupyter?)
		исп pycharm?

			
	exe сайты djgirls и dronov еще раз
	#на данныи момент не имею достаточно данных


	возможно нужно перенести описания валидации(стандартнои) полей в валидаторы
	
	
	как просмотреть историю запросов разных бд
		sqlite
			можно через консоль, но требует соответствующих познании
			⊃ служебную таблицу с историеи запросов
		