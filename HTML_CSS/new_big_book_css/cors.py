CORS
#cross-origin resource sharing
#механизм предоставления странице доступа с ресурсам ∀ домена(кросс-доменный запрос)
#без CORS сайт ограничен доступом только к ресурсам одного происхождения(через политику единого происхождения)
#def: браузер запрещает AJAX-запросы на другие ресурсы
#механизм HTML5 дополняющий политику единого происхождения для упрощения совместного исп ресурсов домена между ∀ веб-app
#спеки опред набор заголовков позволяющих браузеру&серверу идентифицировать разрешенные|запрещенные запросы для междоменных ресурсов
	изображения
	css
	скрипты
	данные
	..
#техника ослабления правила одного источника(типа инструмент настройки для Δ списка белых источников) позволяя js обрабатывать REST API запросы другого источника
#защитная оболочка браузера
#обычно исп для междоменных AJAX запросов
ОБМЕН ЗАПРОСАМИ
взаимодействие ресурсов обычно начинается с отправки GET/POST/HEAD запроса ресурсу сервера
	тип содержимого POST запроса ограничен "application/x-www-form-rulencoded"| "multipart/form-data"|"plaintext"
	запрос ⊃ заголовок Origin указывающий на происхождение клиентского кода
	web-app проверяет источник запроса(на основании Origin) и принимает|отвергает его
		if запрос принят-> отвечает заголовком Access-Control-Allow-Origin
		#заголовок указывает клиенту с каким происхождением будет разрешен доступ
		учитывая что Access-Control-Allow-Origin = Origin запроса -> браузер разрешает запрос
			при запросе на site.ru/resource с site.com/some будут след заголовки
				GET /resource
				Host:site.ru
				Origin: http://site.com
					if запрос принят-> запрашиваемый сервер добавляет к ответу заголовок Access-Control-Allow-Origin ⊃ домен запроса site.com

FIREFOX 68+
about:config
	privacy.file_unique_origin