asyncio

    aiohttp

    gevent

        requests



рефакторинг
    ветвление
        карта карно



os



процессы/потоки



примеры использования v env



абстрактные [базовые] классы



__all__



вывод табличных данных
#пример вывести в консоль два столбца из os.environ



monkey patching



как писать файлы на диск надежно?
#временный файл?



как правильно получить путь к desktop
#лучше чем 
    user_profile_path = os.getenv('USERPROFILE')
    user_desktop_path = os.path.join(user_profile_path, 'desktop')



как обойти gil?



как показать в help норм заголовок if fx принимает *args?



декоратор класса?