КЛАССЫ СОСТОЯНИЯ

	1XX		INFORMATIONAL
	#информирование о процессе передачи
	#HTTP/1.0	игнорируются
	#HTTP/1.1	клиент должен быть готов принять этот класс msg как обычный ответ, но ничего не возвращать
	#msg сервера ⊃ только стартовую строку и(if требуется) неск специфичных для ответа полей заголовка
	#прокси должны отправлять такие msg клиенту
	#!⊃ тело
	
	2XX		SUCCESS
	#успешное принятие и обработка, в зависимости от статуса может ⊃ еще заголовки и тело
	
	
	3XX		REDIRECTION
	#сообщает что для успешного exe нужен еще запрос(обычно по другому URI)
	#адрес передается в заголовке Location(допускается исп фрагментов целевого URI)
	
	
	4XX		CLIENT ERROR
	#ошибка со стороны клиента
	#при исп ∀ методов кроме HEAD тело должно ⊃ гипертекстовое пояснение для пользователя(вроде 404)
	
	
	5XX		SERVER ERROR
	#ошибка сервера
	#при исп ∀ методов кроме HEAD тело должно ⊃ гипертекстовое пояснение для пользователя
	
	
	
КОДЫ СОСТОЯНИЯ
#определяют дальшейшее содержимое и поведение клиента
#⊃ первой строки ответа
	<класс_состояния>XX
#стандарт описываемый соотв RFC
#введение новых согласуется с IETF
#клиент может не знать ∀ состояния но должен реагировать в соотв с классом кода	

	
	200 Ok
	#в тело ответа следует включить msg об итоге exe запроса
	#ответ на PUT if ресурс Δ?
	
	
	201 Created
	#Webpage Created
	#должен ⊃ Location
	
	203
	#запрашиваемые данные отделены от заголовка двумя переводами строки CRLF CRLF
	
	204 No Content
	#ответ на PUT if ресурс Δ
	#!⊃ тело
	
	
	206 Partial Content
	#вроде исп при докачке(запросе с не первого байта файла)
	#см примеры-> докачка
	
	
	300 Multiple Choices
	#исп в типе согласования AGENT-DRIVEN
	#может ⊃ список вариантов для выбора
	
	301 Moved Permanently
	#относится непосредственно к перенаправлению
	
	
	302 Found
	#относится непосредственно к перенаправлению
	
	303 See Other
	#относится непосредственно к перенаправлению
	
	304 Not Modified
	#!⊃ тело
	#возвращается при ∃ в запросе If-Modified-Since с корректной датой и Δ ресурса с этого времени
	
	305
	#относится непосредственно к перенаправлению
	
	
	307 Temporary Redirect
	#относится непосредственно к перенаправлению
	
	
	401 Unauthorize
	#пользователь не авторизован
	
	
	403 Access Forbidden
	#Access allowed only for registered users
	
	
	
	404 Not Found
	#
	
	
	405 Method Not Allowed
	#метод известен, но неприменим к конкретному ресурсу
	#серверу следует включить в msg заголовок Allowed ⊃ список поддерживаемых методов
	
	406 Not Acceptable
	#исп в типе согласования AGENT-DRIVEN
	#может ⊃ список вариантов для выбора
	
	416 Requested Range Not Satisfiable
	#может исп для окончания загрузки файла без указания его размера в ответе(видимо напр для потокового видео)


	501	Not Implemented
	#сервер не распознал метод|заголовок или он не допустим в текущих условиях
	#серверу следует включить в msg заголовок Allowed ⊃ список поддерживаемых методов
	#сервер не должен игнорить некорректные заголовки Content-*	
	
	
	507
	#Insufficient Storage