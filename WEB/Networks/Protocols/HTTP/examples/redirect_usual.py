#] компания Example Corp. ⊃ осн сайт http://example.com и домен псевдоним example.org, клиент посылает запрос страницы "О компании" на вторичный домен
		#браузер не указал фрагмент в запросе, тк нужен документ
		GET /about.html HTTP/1.1
		Host: example.org
		User-Agent: MyLonelyBrowser/5.0
		...
		
		сервер вернет код для постоянного перенаправления указав в Location целевой URL
		
		#браузер прокрутит страницу до фрагмента #contacts после загрузки
		#тело ⊃ ссылку для посетителя
		#Content-Type ⊃ харки тела, а не документа по URI перенаправления
		HTTP/1.x 301 Moved Permanently
		Location: http://example.com/about.html#contacts
		Date: Thu, 19 Feb 2009 11:08:01 GMT
		Server: Apache/2.2.4
		Content-Type: text/html; charset=1251
		Content-Length: 110
		</n>
		<html><body><a href="http://example.com/about.html#contacts">Click here</a></body></html>
	#] Example Corp ⊃ несколько сайтов с разными ccTLD -> запрос главной страницы example.com может быть таким
		GET / HTTP/1.1
		Host: example.com
		User-Agent: MyLonelyBrowser/5.0
		Accept: text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8
		Accept-Language: ru, en-us;q=0.7,en;q=0.3
		Accept-Charset: windows-1251,utf-8;q=0.7,*;q=0.7
		
		#сервер учитывая Accept-Language формирует ответ с временным перенаправлением на example.ru
		HTTP/1.x 302 Found
		Location: http://example.ru/
		Cache-Control: private
		Date: Thu, 19 Feb 2009 11:08:01 GMT
		Server: Apache/2.2.6