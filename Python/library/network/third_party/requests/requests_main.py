#max часто используемый инструмент составления http-запросов python
#простой api создания запросов
#основан на urllib3

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
	
	
METHODS


	.get(...)
	#es:
		#запрос к Root REST API на GitHub
		response = request.get('https://api.github.com')	>> <Response [200]>
		response.status_code 	>> 200
		if response.status_code == 200:
			print('Sucсess')
		elif response.status_code == 404:
			print('Not found')
	
	.post(...)
	#es:
		requests.post('https://httpbin.org/post', data={'key':'value'})
		#передадим данные в json
		response = requsts.post('https://httpbin.rog/post', json={'key':'value'})
		json_response = response.json()
		#сервер получил данные и заголовки
		json_response['data']	>> '{"key": "value"}'
		json_response['headers']['Content-Type']	>> 'application/json'
		
	.put(...)
	#es:
		requests.put('https://httpbin.org/put', data={'key':'value'})
		
		
	.delete(...)
	#es:
		requests.delete('https://httpbin.org/delete')
		
		
	.head(...)
	#es:
		requests.head('https://httpbin.org/get')
		
		
	.patch(...)
	#es:
		requests.patch('https://httpbin.org/patch', data={'key':'values'})
		
	
	.options(...)
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
#es:
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




PERFORMANCE
	КОНТРОЛЬ ТАЙМАУТА
	#обеспечивает эффективность кода, и стабильность app
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
	
	
	
	