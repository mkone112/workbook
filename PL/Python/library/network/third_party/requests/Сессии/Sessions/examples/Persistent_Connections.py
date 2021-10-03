"""
После ∀ инициализации с учетными данными при запросе session -> учетные данные будут сохранены.
Первичная оптимизация perf в форме постоянных соединений, сохраняемых Session в пуле соединений.
If app снова нужно будет подключится к серверу -> исп уже готовое соединение из пула.
"""
from getpass import getpass

import requests

#исп with для гарантии освобождения ресурсов после исп сессии
with requests.Session() as session:
    session.auth = ('username', getpass())
    # Instead of requests.get() use session.get()
    response = session.get('https://api.github.com/user')
print(response.headers, response.json())