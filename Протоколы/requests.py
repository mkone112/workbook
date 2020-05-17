requests
#стандартный инструмент составления http-запросов python
#простой api создания запросов
Δ/приспособление requests к ∀ ситуациям
предотвращение влияния сторонних служб которые могут замедлить app
создание запросов с исп популярнейших HTTP методов
редактирование заголовков запросов и данных при помощи строки запроса и содержимого сообещния
создание авторизованных запросов
настройка запросов для предотвращения сбоев и замедления работы app
установка при исп Pipenv
	pipenv install requests
Pipenv
#виртуальная среда для работы с пакетами
	pipenv install <packet>
	
МЕТОД GET
#методы определяют какие действия будут exe при запросе
#указывает что нужно извлечь данные из ресурса
	request.get()
	
		#выполним запрос к Root REST API на GitHub
		response = request.get('https://api.github.com')	>> <Response [200]>
		response.status_code 	>> 200
		if response.status_code == 200:
			print('Sucsess')
		elif response.status_code == 404:
			print('not found')
		
OBJ Response
#получение ответа на запрос
#obj для анализа результатов запроса
#при приведении к bool
	200..400	>> True
	else 		>> False
	#также считает за True
		204 No Content
		304 Not Modified
.raise_for_status()
#вызывает except if status code ⊂ ошибкам
#if не нужно проверять код состояния в if -> можно расширить диапазон exept для неудачных результатов
	import requests
	from requests.exceptions import HTTPError
	
	for url in ['https://api.github.com', 'https://api.github.com/invalid']:
		try:
			response = requests.get(url)
			#if ответ успешен -> exept не вызывается
			#при вызове exept через .raise_for_status() к некоторым кодам состояния применяется HTTPError
			response.raise_for_status()
		except HTTPError as http_err:
			print(f'HTTP error occured: {http_err}')
		else:
			print('Sucsess!')
ПОЛУЧЕНИЕ СОДЕРЖИМОГО
#тело = payload

	.content	-> <bytes>
	#получения содержимого запроса(?ответа) тела
	.text	-> <utf8_str>
	#~.content
	#декодирование происходит в соотв с содержимым .encoding
	.encoding
	#⊃ кодировку ответа
		response.encoding	>> 'UTF-8'
	#данные берутся из заголовка 
	#мб Δ
		response.encoding = 'utf-8'
	.header -> <dict>
	#заголовки
		response.headers	>> 
		{'Server': 'GitHub.com',
		'Date': 'Mon, 10 Dec 2018 17:49:54 GMT',
		'Content-Type': 'application/json; charset=utf-8', 
		'Transfer-Encoding': 'chunked', 
		'Status': '200 OK',
		'X-RateLimit-Limit': '60',
		'X-RateLimit-Remaining': '59',
		'X-RateLimit-Reset': '1544467794', 
		'Cache-Control': 'public, max-age=60, s-maxage=60',
		'Vary': 'Accept',
		'ETag': 'W/"7dc470913f1fe9bb6c7355b50a0737bc"',
		'X-GitHub-Media-Type': 'github.v3; format=json', 'Access-Control-Expose-Headers': 'ETag, Link, Location,		Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type', 
		'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload',
		'X-Frame-Options': 'deny',
		'X-Content-Type-Options': 'nosniff',
		'X-XSS-Protection': '1; mode=block',
		'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 
		'Content-Security-Policy': "default-src 'none'",
		'Content-Encoding': 'gzip',
		'X-GitHub-Request-Id': 'E439:4581:CF2351:1CA3E06:5C0EA741'}
	#http заголовки регистронезависимы -> можно не париться о регистре
		response.headers['content-type']	>> 'application/json; charset=utf-8'
		response.headers['content-tYpe']	>> 'application/json; charset=utf-8'
		
		
ОБРАТНАЯ СЕРИАЛИЗАЦИЯ JSON
	response = requests.get('https://api.github.com')
	response.text
	>>
	'{\n  "current_user_url": "https://api.github.com/user",\n  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}
	в данном случае ответ - сериализованный JSON контент
	можно взять str ⊃ text воспользовавшись dict и провести обратную сериализацию исп json.loads()
		#но можно и проще
		response.json()	>>	{'current_user_url': 'https://api.github.com/user', 'curren ...}
		#разумеется это обычный dict
ПАРАМЕТРЫ ЗАПРОСА
	ПЕРЕДАЧА VAL В ПАРАМЕТРАХ СТРОКИ ЗАПРОСА(В URL)
	#max простой способ настройки GET
	#данные передаются в params
	#параметры можно передавать в 
		dict
				#просмотрим requests используя Search API GitHub
				import requests
				
				#поиск местонахождения для запроса на GitHub
				response = request.get(
					'https://api.github.com/search/repositories',
					params={'q': 'requests+language:python'}
				)
				json_response = response.json()
				repository = json_response['items'][0]
				print(f'Repository name: {repository["name"]}')
				print(f'Repository description: {repository["description"]}')
		в списке кортежей
				requests.get(
					'https://api.github.com/search/repositories',
					params=[('q', 'requests+language:python')],
				)
				>> <Response [200]>
		bytes(str вроде тоже пашет)
				requests.get(
					'https://api.github.com/search/repositories',
					params=b'q=requests+language:python'
				)
				>> <Response [200]>
	НАСТРОЙКА ЗАПРОСОВ ДОБАВЛЕНИЕМ/Δ ЗАГОЛОВКОВ
		#требуется передать dict этого заголовка через параметр headers
		#Δзапрос подсветив совпадения в результате
		import requests
		
		response = requests.get(
			'https://api.github.com/search/repositories',
			params={'q': 'requests+language:python'},
			#типы контента которые можно исп в этом app
			#'application/vnd.github.v3.text-match+json
				#уникальный заголовок Accept для GitHub подсвечивающий ∀ совпадения
			headers={'Accept':'application/vnd.github.v3.text-match+json'},
		)
		#просмотр нового массива 'text-matches' ⊃ данные о поиске в результатах
		json_response = response.json()
		repository = json_response['items'][0]
		print(f'Text matches: {repository["text_matches"]}')

POST
	requests.post('https://httpbin.org/post', data={'key':'value'})
	#передадим данные в json
	response = requsts.post('https://httpbin.rog/post', json={'key':'value'})
	json_response = response.json()
	#сервер получил данные и заголовки
	json_response['data']	>> '{"key": "value"}'
	json_response['headers']['Content-Type']	>> 'application/json'
	
PUT
	requests.put('https://httpbin.org/put', data={'key':'value'})
	
	
DELETE
	requests.delete('https://httpbin.org/delete')
	
	
HEAD
	requests.head('https://httpbin.org/get')
	
	
PATCH
	requests.patch('https://httpbin.org/patch', data={'key':'values'})
	

OPTIONS
	requests.options('https://httpbin.org/get')
	

МЕТОДЫ
	POST
	PATCH
	PUT
	#передают данные в теле запроса
	#requsts принимает эти данные через аргумент data
		data
		#~params
		#принимает
			dict
			список кортежей
			bytes( и видимо str )
			#это важно тк сервер может требовать определенный тип данных
	при необходимости отправить данные в JSON можно исп соотв arg
	#при передаче в json, requests сериализует данные и добавит правильный Content-Type заголовок
httpbin.org
#создатель Кеннет Рейтц, внедрившим исп requests
#создан для тестовых запросов


АНАЛИЗ ЗАПРОСА
#перед отправкой запросов requests производит его подготовку
	проверка заголовков
	сериализация JSON
#requests также предоставляет информацию в форме PreparedRequests
PreparedRequests
#информация о exe запросе
	пейлоад
	URL
	заголовки
	аутентификация
	...
#прмеры
	response = requests.post('https://httpbin.org/post', json={'key':'value'})
	response.requests.headers['Content-Type']	>> 'applications/json'
	response.requests.url	>> 'https://httpbin.org/post'
	response.requests.body	>> b'{"key": "value"}
	
	
АУТЕНТИФИКАЦИЯ HTTP AUTH
#данные авторизации передаются в заголовке
	Authorization
∀ fx запросов ⊃ arg "auth" для передачи учетных данных
#пример: Authenticated User API GitHub - конечная точка сервиса предоставляющая данные о профиле аутентифицированного пользователя
данные авторизации передаются через кортеж в .get()
	from getpass import getpass
	#при успехе -> 200
	#при запросе без учетных данных(| кривыми) -> 401 Unauthorized
	#передача логина/пароля в auth использует базовую схему аутентификации HTTP
	requests.get('https://api.github.com/user', auth=('username', getpass() ))
тоже самое
	from requests.auth import HTTPBasicAuth
	from getpass import getpass
	requests.get(
		'https://api.github.com/user',
		auth=HTTPBasicAuth('username', getpass())
	)
	
	
getpass.getpass() -> str
#вроде выводит запрос для ввода пароля в консоль без отображения вводимых символов(как в unix)
#prompt for password with echo off, using Windows getch()
#дополнительно позволяет не хранить пароль в исходниках


хотя не требуется явно указывать HTTPBasicAuth, может потребоваться исп другие методы
	HTTPDigestAuth
	HTTPProxyAuth
	OAuth
	...
	
	
СОЗДАНИЕ СВОЕГО МЕХАНИЗМА АУТЕНТИФИКАЦИИ
#требуют высокой квалификации во избежание уязвимостей - if служба не трубует кастомный механизм аутентификации стоит исп базовые
	import requests
	from requests.auth import AuthBase
	
	class TokenAuth(AuthBase):
		'''Implements a custom authentification scheme'''
		
		def __init__(self, token):
			self.token = token
			
		def __call__(self, r):
			'''Attach an API token to a custom auth header'''
			r.headers['X-TokenAuth'] = f'{self.token}'
			return r
	#механизм TokenAuth получает токен, включающийся в заголовок запроса
	requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))
	
ПРОВЕРКА SSL СЕРТИФИКАТА
#requests by def делает ∀ сам
	ОТКЛЮЧЕНИЕ ПРОВЕРКУ SSL СЕРТИФИКАТА
		requests.get('https://api.github.com', verify=False)
		>> InsecureRequestWarning: Unverified HTTPS request is being made...
		<Response [200]>

certifi
#пакет(следует почаще обновлять)
#используется requests для предоставления сертификатов


ПРОИЗВОДИТЕЛЬНОСТЬ APPS
	КОНТРОЛЬ ТАЙМАУТА
		при отправке встроенного(?) запроса внешней службе, сисма ждет ответ 
			if app ждет ответа слишком долго
				запросы к службе мб сохранены(?)
				gui может упасть
				фоновые задачи могут зависнуть
		by def таймаут requests INF -> следует ∀ указывать таймаут
			timeout=<int|float>|(<conn_timeout>,<read_timeout>)
			#arg
			#<conn_timeout> таймаут соединения - время на установку соединения
			#<read_timeout> время ожидания после установки соединения
				requests.get('https://api.github.com', timeout=3.05) >> <Response [200]>
				requests.get('https://api.github.com', timeout=(2, 5))
		при истечении таймаута вызовет Timeout exept ⊃ requests.exceptions
			from requests.exceptions import Timeout
			
			try:
				response = requests.get('https://api.github.com', timeout=1)
			except Timeout:
				print('The request timed out')
			else:
				print('The request did not time out')

======================проверил_до_сюда
	
	СЕАНСЫ
	#сессии
	#исп для сохранения параметров в запросах
		Sessions
		#класс реализующий работу таких высокоуровневых абстракций как .get()/.post()/...
		#исп для 
			настройки контроля над exe запросов
			повышения perf запросов
			использование одну аутентификацию для неск запросов
				#после ∀ инициализации с учетными данными при запросе session -> учетные данные будут сохранены
				#первичная оптимизация perf в форме постоянных соединений, сохраняемых Session в пуле соединений
					#if app снова нужно будет подключится к серверу -> исп уже готовое соединение из пула
				import requests
				from getpass import getpass
				#исп with для гарантии освобождения ресурсов после исп сессии
				with requests.Session() as session:
					session.auth = ('username', getpass())
					# Instead of requests.get() use session.get()
					response = session.get('https://api.github.com/user')
				print(response.headers, response.json())
	
	
	ОГРАНИЧЕНИЯ ПОВТОРНЫХ ПОПЫТОК
		
		HTTPAdapter
		#max число повторов запроса при сбое
		#by def requests не exe повторный запрос
			#для исп fx повторного запроса нужно реализовать свой транспортный адаптер
				ТРАНСПОРТНЫЙ АДАПТЕР
				#позволяет опредеделить свой набор кофигурация для ∀ службы с которой exe взаимодействие
					#повтор 3раза до ConnectionErro
					#создадим транспортный адаптер ⊃ параметр max_retries и подключим его к Session obj
					import requests
					from requests.adapters import HTTPAdapter
					from requests.exceptions import ConnectionError