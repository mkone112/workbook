response = requests.get('https://api.github.com')
response.text
>>
'{\n  "current_user_url": "https://api.github.com/user",\n  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}
в данном случае ответ - сериализованный JSON контент
можно взять str ⊃ text воспользовавшись dict и провести обратную сериализацию исп json.loads()
    #но можно и проще
    response.json()	>>	{'current_user_url': 'https://api.github.com/user', 'curren ...}
    #разумеется это обычный dict