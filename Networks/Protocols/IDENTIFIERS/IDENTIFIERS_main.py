НОРМАЛИЗАЦИЯ URL
#исп поисковыми сисмами для снижения индексации дубликатов страниц и их расположения в порядке val
	типы
		сохраняющие исх адрес
			конвертация в lower case
			перевод управляющих конструкций в upper case
				http://www.example.com/a%c2%b1b -> http://www.example.com/a%C2%B1b
			перекодировка управляющих конструкций в явные символы
			#для связности процентные конструкции переводятся в символы
				Альфа			%41-%5A и %61-%7A
				Цифровые		%30-%39
				Дефис			%2D
				Точка			%2E
				Подчеркивание	%5F
				Тильда			%7E
			#не должны создаваться URI поставщиками и такие URI должны приводиться к символам
				http://www.example.com/%7Eusername/ -> http://www.example.com/~username/
			удаление def порта 
				http://www.example.com:80/bar.html -> http://www.example.com/bar.html
		НЕ сохраняющие исх адрес
			частично сохраняющие
			#для http и https могут привести к ~ url, не RFC 3986 это не гарантирует
				добавление /
				#демонстрация каталога
					нет способа узнать ⊂ ли URL путь каталогу
					#rfc 3986 : if url перенаправляет на нормализованный url -> это признак эквивалентности
			Δ исх адрес
				удаление головного индекса
					http://www.example.com/default.asp -> http://www.example.com/
				удаление фрагментов
				#не виден на сервере -> мб удален
					http://www.example.com/bar.html#section1 -> http://www.example.com/bar.html
				#одноко AJAX часто применяет var в таких фрагментах
				замена ip на домен
				#обратная замена мб небезопасной из-за исп виртуальных серверов
				удаление дублированных слешей
					http://www.example.com/foo//bar.html -> http://www.example.com/foo/bar.html
				удаление/добавление www как элта верхнего доменного уровня
				#некоторые сайты оперируют двумф интернет-доменами
					http://example.com/ и http;//www.example.com/
					#могут вести на один ресурс(перенаправляют с www на не www и наоборот)
				сортировка параметров запросов
				#напр в алфавитном с пересозданием
					http://www.example.com/display?lang=en&article=fred ->
					http://www.example.com/display?article=fred&lang=en
					#однако порядом мб значимым(не регламентируется стандартами) и var могут появляться неск раз
				удаление неисп var
				#хз как определять
				#параметр без val не означает что он не исп
				удаление параметров по def
				#
				удаление "?" при пустом запросе


PURL
#Persistent Uniform Resource Locator(локатор)
#определитель местонахождения
#механизм и надежность ~ dns
#формат основан на URL, но в отличие от него неΔ
#предотвращает 404(тк dns+url не хватает гибкости)
#альтернатива URN
#создан в 96
#указывает на на расположение ресурса а запись в бд PURL ⊃ url перенаправляющий запрос через HTTP redirect
#при Δ url требуется Δ только бд purl
	СТРУКТУРА PURL
		<protocol>://<server>/<name>
		#пример
			http://purl.oclc.org/OCLC/PURL/FAQ
		#не поддерживает "~" и "#"
	НЕДОСТАТКИ
		лишнее звено
			лишний трафик
	ПРЕИМУЩЕСТВО
		URN сформируется нескоро
		PURL - быстрое, рабочее решение прямо сейчас
		может исп ∀ желающий
		формат полностью совместим с URN
		opensource


УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ URL
#процентные конструкции?
#что-то вроде управляющих {xn} unicode
#вроде начинаются с %
	http://www.example.com/a%C2%B1b
	#управляющие конструкции
		%C2%B1

uri
#uniform resource identifier - единообразный id ресурса(ранее universal resource identifier)
#{xn} символов идентифицирующая абстрактный |физический ресурс(файл, службу, email) прежде всего речь о ресурсах www
#простой/расширяемый способ id ресурсы
	#⊃ неск схем идентификации, еще неск в процессе создания
#т.к. не всегда указывате как получить ресурс -> это дает возможность описывать ресурсы которые нельзя получить через интерет(личность, авто, город) через RDF
#считается созданым вместе с url, концепция документирована в июне 94 в RFC 1630
#развивается в основном Консорциумом Всемирной паутины
#ПРИМЕРЫ
	АБСОЛЮТНЫЕ URI
		https://ru.wikipedia.org/wiki/URI
		ftp://ftp.is.co.za/rfc/rfc1808.txt
		file://C:\UserName.HostName\Projects\Wikipedia_Articles\URI.xml
		file:///C:/file.wsdl
		file:///Users/John/Documents/Projects/Web/MyWebsite/about.html
		ldap://[2001:db8::7]/c=GB?objectClass?one
		mailto:John.Doe@example.com
		sip:911@pbx.mycompany.com
		news:comp.infosystems.www.servers.unix
		data:text/plain;charset=iso-8859-7,%be%be%be
		tel:+1-816-555-1212
		telnet://192.0.2.16:80/
		urn:oasis:names:specification:docbook:dtd:xml:4.1.2
		urn:oid:1.2.840.113549.1.1.1
	ОТНОСИТЕЛЬНЫЕ URI
		/relative/URI/with/absolute/path/to/resource.txt
		//example.org/scheme-relative/URI/with/absolute/path/to/resource.txt
		relative/path/to/resource.txt
		../../../resource.txt
		resource.txt
		/resource.txt#frag01
		#frag01
		[пустая строка] — эквивалентно разбору идентификатора парсером с результатом [пустая строка], то есть ссылка ведёт на объект по умолчанию в схеме по умолчанию


СТРУКТУРА URI
	URI = [ схема ":" ] иерархическая часть [ "?" запрос ] [ "#" фрагмент ]
		схема
		#часто указывает на протокол
			http
			ftp
			file
			ldap
			mailto
			urn
		иерархическая часть
		#данные часто иерархически организованные совместно с данными неиерархической компоненты "запрос" идентифицируют ресурс в пределах видимостьи uri-схемы
		#обычно путь к ресурсу(может ⊃ адрес сервера)| id ресурса(в случае URN)
		фрагмент
		#необязателен
		#описан в RFC 3986
	#часть URI без схемы часто называют ссылкой(reference) URI
		#могут исп в 
			HTML
			XHTML
			XML
			XSLT


РАЗРЕШЕНИЕ URI
#превращение ссылки URI в абсолютный URI
XSLT
#?



НЕДОСТАТКИ URI
#тк URL фундаментальное нововведение интернета -> uri документально закреплялся ⊃ полную обратную совместимость
	#как и в URL можно исп ограниченный набор символов меньше ASCII -> ссылки приходится кодировать
		uri
		"https://ru.wikipedia.org/wiki/Кириллица"
		кодируется в url как	 
		"https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D1%80%D0%B8%D0%BB%D0%BB%D0%B8%D1%86%D0%B0"
		#нарушает принцип интернационализма провозглашаемые ∀ организациями интернета вроде W3C ISOC
IRI
#Internationalized(международный) Resource Identifier
#решает проблемы URI/URL поддержкой юникода
#хз когда будет исп



XRI
#Extensible Resource Identifier
#разработан OASIS
#формат стремящийся создать id независимые от контекста(протокола/домена/пути/app/платформы)


ПАРСИНГ URI
#исп re
#RFC рекомендует шаблон
	^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?
	#подробнее:https://ru.wikipedia.org/wiki/URI
	
RDF
#Resource Desctiption Framework
#новейшая технология семантической паутины
#основан на URI

СВЯЗЬ URI,URL,URN
#URI =  URL|URN|URL+URN
#в посл время URI обозначают ∀ id str -> возм URL и URN скоро исчезнут
URL
#URI предоставляющий информацию о местонахождении ресурса кроме идентификации
#создан Тимом Бернсом-Ли в 1990 в Женеве в CERN(Conseil European pour la Recherche Nucleaire)
URN
#URL только идентифицирующий ресурс в опред ns(и соотв в опред контексте), без указания местонахождения
#примеры
	ISBN:0-395-36341-1
	#URI указывающий на книгу в ns ISBN, но не указывает где ее взять
