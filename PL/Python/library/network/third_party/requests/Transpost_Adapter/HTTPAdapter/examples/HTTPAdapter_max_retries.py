"""
повтор 3 раза до ConnectionError
создадим транспортный адаптер ⊃ параметр max_retries и подключим его к Session obj
"""
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

#исп адептер для ∀ запросов начинающихся с 'https://api.github.com', github_adapter)
#session будет поддерживаться своей конфигурации для ∀ запроса к этому url
try:
    session.get('https://api.github.com')
exept ConnectonError as ce:
    print(ce)
