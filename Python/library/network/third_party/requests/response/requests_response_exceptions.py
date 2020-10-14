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