django 2.1
контроллеры?
Разграничение доступа?
Аутентификация через соцсети?
вывод графических миниатюр?
CAPTCHA?
#обработка ...
Angular?
BBCode?
#форматирование текста
программирование web-служб REST?
средства обработки пользовательского ввода?
выгрузка файлов?
посредники?
сигналы?
средства отправки email?
подсис-ма кэширования?
административный сайт dj - одно из его преимуществ
маршруты и маршрутизатор
рендеринг шаблонов. Сокращения?
параметры полей и моделей?
редактор модели?
связи между моделями
строковое представление модели?
url-параметры и параметризованные запросы?
обратное разрешение интернет-адресов?
Формы связанные с моделями?
Контроллеры-классы?
Наследование шаблонов?
БАЗОВЫЕ ИНСТРУМЕНТЫ DJ?
	интернет адрес модели и его формирование?
	методы модели?
	валидация модели. Валидаторы?
		стандартные валидаторы dj?
		вывод собственный сообщений об ошибках
		написание своих валидаторов?
		валидация модели?
МИГРАЦИИ
	формирование миграций?
	слияние миграций?
	файлы миграций?
	вывод списка миграций?
ЗАПИСЬ ДАННЫХ?
	правка записей?
	создание записей?
	.save()?
	удаление записей?
	особенности обработки связанных записей?
		особенности обработки связи "один-со-многими"?
		особенности обработки связи "один-с-одним"?
		особенности обработки связи "многие-со-многими"?
	произвольное переупорядочивание записей?
	массовая запись данных?
	выполнение валидации модели?
ВЫБОРКА ДАННЫХ?
	извлечение данных из полей записи?
	доступ к связанным записям?
	выборка записей?
		выборка ∀ записей?
		извлечение одной записи?
		получение числа записей в наборе?
		поиск записи?
		фильтрация записей?
		написание условий фильтрации?
		фильтрация по val полей связанных записей?
		сравление с val других полей?
		сложные условия фильтрации?
		выборка уникальных записей?
		выборка указанного кол-ва записей?
	сортировка записей?
	агрегатные вычисления?
		вычисления по ∀ записям модели?
		вычисление по группам записей?
		агрегатные fx?
	вычисляемые поля?
		простейшие вычисляемые поля?
		fx СУБД?
		условные exp СУБД?
		вложенные запросы?
	объединение наборов записей?
	извлечение val только из заданных полей?
	получение val из полей списком?
МАРШРУТИЗАЦИЯ?
	как работает маршрутизатор?
	списки маршрутов уровня проекта и уровня приложения?
	объявление маршрутов?
	передача данных в контроллеры?
	именованные маршруты?
	namespaces. Корневое приложение?
	указание шаблонных путей в виде re?
КОНТРОЛЛЕРЫ-FX
	написание контроллеров-fx
		однозадачные контроллеры?
		многозадачные контроллеры?
	формирование ответа?
		низкоуровневые средства формирования ответа?
		формирование ответа на основе шаблона?
		класс TemplateResponse: отложенный рендеринг шаблона?
	получение сведений о запросе?
	перенаправление?
	формирование интернет-адресов путем обратного разрешения?
	выдача сообщений об ошибках и обработка особых ситуаций?
	специальные ответы?
		потоковый ответ?
		отправка файлов?
		отправка файлов в формате JSON?
	сокращения dj?
	доп настройки контроллеров?
КОНТРОЛЛЕРЫ-КЛАССЫ?
	базовые контроллеры-классы?
		контроллер View: диспетчеризация по HTTP-методу?
		примесь ContextMixin: создание контекста шаблона?
		примесь TemplateResponseMixin: рендеринг шаблона?
		контроллер TemplateView: ∀ вместе?
	классы выводящие сведения о выбранной записи?
		примесь SingleObjectMixin: извлечени записи из модели?
		примесь SingleObjectTemplateResponseMixin: рендеринг шаблона на основе найденной записи?
		контроллер DeltaView: ∀ вместе?
	классы выводящие наборы записей?
		примесь MultipleObjectMixin: извлечение набора записей из модели?
		примесь MultipleObjectTemplateResponseMixin: рендеринг шаблона на основе набора записей?
		контроллер ListView: ∀ вместе?
	классы работающие с формами?
		классы для вывода и валидации форм?
			Примесь FormMixin: создание формы?
			Контроллер ProcessFormView: вывод и обработка формы?
			контроллер-класс FormView: создание, вывод и обработка формы
		классы для работы с записями?
			примесь ModelFormMixin: создание формы связанной с моделью?
			контроллер CreateView: создание новой записи?
			контроллер UpdateView: исправление записи?
			примесь DeletionMixin: удаление записи?
			контроллер DeleteView: удаление записи с подтверждением
	классы для вывода хронологических списков?
		вывод последних записей?
			примесь DateMixin: фильтрация записей по дате?
			контроллер BaseDateListView: базовый класс
ArchiveIndexView
#вывод последних записей
#класс для вывода хронологических списков
#контроллер
YearMixin
#примесь
#класс для извлечения года
YearArchiveView
#класс для вывода записей за год
MonthMixin
#класс для извлечения месяца
#примесь
MonthArchiveView
#класс для вывода записей за месяц
#контроллер
WeekMixin
#класс для извлечения номера недели
#примесь
WeekArchiveView
#класс для вывода записей за неделю
#контроллер
DayMixin
#класс для извлечения текущего дня
#примесь
DayArchiveView
#контроллер
#класс для вывода записей за день
TodayArchiveView
#класс для вывода записей за текущее число
#контроллер
DateDetailView
#контроллер
#класс для вывода одной записи за указанное число
RedirectView
#класс-контроллер для перенаправления
контроллеры-классы смешанной fx?
настройки проекта касающиеся шаблонов?
вывод данных. Директивы?
Теги шаблонизатора?
фильтры?
настройка подсис-мы static файлов?
обслуживание static файлов?
формирование url static файлов?
ПАГИНАТОР?
	Paginator
	#класс для создания пагинатора
	#сам пагинатор
	Page
	#класс для вывода пагинатора
	#часть пагинатора
ФОРМЫ СВЯЗАННЫЕ С МОДЕЛЯМИ
	создание форм связанных с моделями?
		создание форм фабрикой классов?
		создание форм быстрым объявлением?
		создание форм полным объявлением?
			как выполняется полное объявление?
			параметры поддерживаемые ∀ типами полей?
			доступные классы полей форм?
			классы полей форм, применяемые по умолчанию?
		задание эл-тов управления?
			классы эл-тов управления?
			эл-ты управления применяемые по умолчанию?
		задание эл-тов управления?
			классы эл-тов управления?
			эл-ты управления применяемые по умолчанию?
		обработка форм
			добавление записи посредством формы?
				создание формы для добавления записи?
				повторное создание формы?
				валидация данных занесенных в форму?
				сохранение данных занесенных в форму?
				доступ к данным занесенным в форму?
			правка записи посредством формы?
			удаление записей?
		вывод форм на экран?
			быстрый вывод форм?
			расширенный вывод форм?
НАБОРЫ ФОРМ СВЯЗАННЫЕ С МОДЕЛЯМИ
	создание наборов форм связанных с моделями?
	обработка наборов форм связанных с моделями?
		создание набора форм связанного с моделью?
		повторное создание набора форм?
		валидация и сохранение набора форм?
		доступ к данным в наборе форм?
		реализация переупорядочивания записей?
	вывод наборов форм на экран?
		быстрый вывод наборов форм?
		расширенный вывод наборов форм?
	валидация в наборах форм?
	встроенные наборы форм?
		создание встроенных наборов форм?
		обработка встроенных наборов форм?
РАЗГРАНИЧЕНИЕ ДОСТУПА:БАЗОВЫЕ ИНСТРУМЕНТЫ?
	подсис-ма разграничения доступа?
	подготовка подсис-мы разграничения доступа?
		настройка подсисмы разграничения доступа?
		создания superuser?
		смена пароля user'а?
	работа со списками пользователей и групп?
		список пользователей?
		группы пользователей. Список групп?
	аутентификация и служебные процедуры?
LoginView
#контроллер
#вход на сайт
LogoutView
#контроллер
#выход с сайта
PasswordChangeView
#контроллер
#смена пароля
PasswordChangeDoneView
#контроллер
#уведомление об успешной смене пароля
PasswordResetView
#контроллер
#отправка письма для смены пароля
PasswordResetDoneView
#контроллер
#уведомление об отправке письма для сброса пароля
PasswordResetConfirmView
#контроллер
#сброс пароля
PasswordResetCompleteView
#контроллер
#уведомление об успешном сбросе пароля
получение сведений о текущем пользователе?
авторизация?
	авторизация в контроллерах?
		императивный подход к авторизации?
		декларативная авторизация в контроллерах-fx?
		декларативная авторизация в контроллерах-классах?
	авторизация в шаблонах?
РАСШИРЕННЫЕ ИНСТРУМЕНТЫ И ДОПОЛНИТЕЛЬНЫЕ БИБЛИОТЕКИ?
	МОДЕЛИ:РАСШИРЕННЫЕ ИНСТРУМЕНТЫ?
		управление выборкой полей?
		связи "многие-со-многими" с доп данными?
		полиморфные связи?
		наследование моделей?
			прямое наследование моделей?
			абстрактные модели?
			прокси-модели?
		создание своих диспетчеров записей?
			создание диспетчера записей?
			создание диспетчеров обратной связи?
		создание своих наборов записей?
		управление транзакциями?
			∀|ничего:два высокоуровневых режима управления транзакциями?
				ничего:режим по умолчанию?
				∀:режим для максималистов?
			управление транзакциями на низком уровне?
				включение режима "∀" на уровне контроллера?
				обработка подтверждения транзакции?
				выключение режима "∀" для контроллера?
				управление транзакциями вручную?
ФОРМЫ И НАБОРЫ ФОРМ:РАСШИРЕННЫЕ ИНСТРУМЕНТЫ И ДОПОЛНИТЕЛЬНАЯ БИБЛИОТЕКА?
	формы не связанные с моделями?
	наборы форм не связанные с моделями?
	расширенные средства для вывода форм и наборов форм?
		указание css-стилей для форм?
		настройка выводимых форм?
		Настройка наборов форм?
	Библиотека Django Simple Captcha: поддержка CAPTCHA?
		установка Django Simple Captcha?
		настройка Django Simple Captcha?
		дополнительные команды?
			captcha_clean?
			captcha_create_pool?
	дополнительные настройки проекта имеющие отношение к формам?
ШАБЛОНЫ:РАСШИРЕННЫЕ ИНСТРУМЕНТЫ И ДОП БИБЛИОТЕКИ?
	библиотека django-precise-bbcode: поддержка BBCode?
		установка django-precise-bbcode?
		поддерживаемые BBCode теги?
		обработка BBCode?
			обработка BBCode в процессе вывода?
			хранение BBCode в модели?
		создание дополнительных BBCode-тегов?
		создание смайликов?
		настройка django-precise-bbcode?
	Библиотека django-bootstrap4: интеграция с Bootstrap?
		установка django-bootstrap4?
		использование django-bootstrap4?
		настройка django-bootstrap4?
	написание своих фильтров и тегов?
		организация исходного кода?
		написание фильтров?
			написание и использование простейших фильтров?
			управление заменой недопустимых знаков HTML?
		написание тегов?
			написание тегов выводищих элементарные val?
			написание шаблонных тегов?
		регистрация фильтров и тегов?
	переопределение шаблонов?
ОБРАБОТКА ВЫГРУЖЕННЫХ ФАЙЛОВ?
	подготовка подсис-мы обработки выгруженных файлов?
		настройка подсис-мы обработки выгруженных файлов?
		указание маршрута для выгруженных файлов?
	хранение файлов в моделях?
		типы полей модели, предназначенные для хранения файлов?
		поля, валидаторы и эл-ты управления форм служащие для указания файлов?
		обработка выгруженных файлов?
		вывод выгруженных файлов?
		удаление выгруженного файла?
	хранение путей к файлам в моделях?
	низкоуровневые средства для сохранения выгруженных файлов?
UploadedFile
#низкоуровневое средство для сохранения выгруженных файлов
#выгруженный файл
		вывод выгруженных файлов низкоуровневыми средствами?
django-cleanup
#библиотека
#автоматическое удаление ненужных файлов
easy-thumbnails
#библиотека
#вывод миниатюр
		установка easy-thumbnails?
		настройка easy-thumbnails?
			пресеты миниатюр?
			остальные параметры библиотеки?
		вывод миниатюр в шаблонах?
		хранение миниатюр в моделях?
		thumbnail_cleanup
		#дополнительная команда
РАЗГРАНИЧЕНИЕ ДОСТУПА: РАСШИРЕННЫЕ ИНСТРУМЕНТЫ И ДОП БИБЛИОТЕКИ?
	настройки проекта, касающиеся разграничения доступа?
	работа с пользователями?
		создание пользователей?
		работа с паролями?
	аутентификация и выход с сайта?
	валидация паролей?
		стандартные валидаторы паролей?
		написание своих валидаторов паролей?
		выполнение валидации паролей?
	Python Social Auth
	#библиотека
	#регистрация и вход через соцсети
		создание приложения вконтакте?
		установка и настройка Python Social Auth?
		использование Python Social Auth?
	указание своей модели пользователя?
	создание своих прав пользователя?
ПОСРЕДНИКИ И ОБРАБОТЧИКИ КОНТЕКСТА?
	посредники
		стандартные посредники?
		порядок выполнения посредников?
		написание своих посредников?
			посредники-fx?
			посредники-классы?
	обработчики контекста?
Cookie, сессии, всплывающие сообщения и подписывание данных?
		Cookie?
		сессии?
			настройка сессий?
			использование сессий?
			доп команда clearsessions?
		всплывающие сообщения?
			настройка всплывающих сообщений?
			уровни всплывающих сообщений?
			создание всплывающих сообщений?
			вывод всплывающих сообщений?
			объявление своих всплывающих сообщений?
		подписывание данных?
СИГНАЛЫ?
	обработка сигналов?
	встроенные сигналы Django?
	объявление своих сигналов?
ОТПРАВКА email?
	настройка подсис-мы отправки email?
	низкоуровневые инструменты для отправки email?
		EmailMessage
		#класс обычного email
		формирование email на основе шаблонов?
		использование соединений. Массовая рассылка email?
		EmailMultiAlternatives
		#класс email состоящего из нескольких частей
	высокоуровневые инструменты для отправки email?
		отправка email по произвольным адресам?
		отправка писем зарегистрированным пользователям?
		отправка писем админам и редакторам сайта?
КЭШИРОВАНИЕ?
	кеширование на стороне сервера?
	подготовка подсис-мы кэширования на стороне сервера?
		настройка подсис-мы кэширования на стороне сервера?
		создание таблицы для хранения кэша?
	высокоуровневые ср-ва кэширования?
		кэширование всего сайта?
		кэширование на уровне отдельных контроллеров?
		управление кэшированием?
	низкоуровневые ср-ва кэширования?
		кэширование фрагментов веб-страниц?
		кэширование произвольных val?
	кеширование на стороне клиента?
		автообработка заголовков?
		условная обработка запросов?
		прямое указание параметров кэширования?
		запрет кэширования?
АДМИНКА DJANGO?
	регистрация моделей в админке?
	редакторы моделей?
		параметры списка записей:
			состав выводимого списка?
			фильтрация и сортировка?
			прочие?
		параметры страниц добавления и правки записей?
			набор выводимых полей?
			эл-ты управления?
		регистрация редакторов в админке?
	встроенные редакторы?
		объявление встроенного редактора?
		параметры встроенного редактора?
		регистрация встроенного редактора?
	действия?
РАЗРАБОТКА ВЕБ-СЛУЖБ REST.
Django REST framework
#библиотека?
	установка и подготовка к работе?
	вывод данных?
		сериализаторы?
		веб-представление JSON?
		вывод данных на стороне клиента?
		первый принцип REST: идентификация ресурса по интернет-адресу?
	ввод и правка данных?
		второй принцип REST: идентификация действия по HTTP-методу?
		парсеры веб-форм?
	контроллеры-классы Django REST framework?
		контроллер-класс низкого уровня?
		контроллеры-классы высокого уровня: комбинированные и простые?
	метаконтроллеры?
	разграничение доступа?
		третий принцип REST: данные клиента хранятся на стороне клиента?
		классы разграничения доступа?
СРЕДСТВА ДИАГНОСТИКИ И ОТЛАДКИ?
	средства диагностики?
		настройка средств диагностики?
		объект сообщения?
		форматировщики?
		фильтры?
		обработчики?
		регистраторы?
		пример настройки диагностических средств?
	средства отладки?
		веб-страница сообщения об ошибке?
		отключение кэширования static?
деплой?
	подготовка сайта к деплою?
		веб-страницы с сообщениями об ошибках и их шаблоны?
		указание настроек эксплутационного режима?
		подготовка static?
		удаление ненужных данных?
		окончательная проверка сайта?
	публикация с использованием Apache?
		подготовка платформы для публикации?
		конфигурирование сайта?
		особенности публикации сайта, работающего по HTTPS?
		
		