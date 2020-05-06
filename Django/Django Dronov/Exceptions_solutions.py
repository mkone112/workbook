 RuntimeError: Model class testapp.models.AdvUser doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
	0. ДОБАВИТЬ СВ-ВО МОДЕЛИ
		models.py
			class <Model>():
				...
				class Meta:
					app_label = 'testapp'
					
		0.1 ПРОИЗВЕСТИ МИГРАЦИЮ
			py manage.py makemigrations testapp
			py manage.py migrate					
			
			
	1. ОБЪЯВИТЬ BASE CLASS БАЗОВЫЙ ДЛЯ ∀ МОДЕЛЕЙ
		class BaseModel(models.Model):
			class Meta:
				abstract = True
				app_label = 'testapp'
		
		1.1 ПРОИЗВЕСТИ МИГРАЦИЮ
			py manage.py makemigrations testapp
			py manage.py migrate
			
			
	2.ДОБАВИТЬ APP В INSTALLED_APPS


при Δ проекта (напр моделей) консоль требуется перезапускать

при Δ полей содержимое таблицы не меняется
	перестрой отображение в pycharm(он не обновляет его автоматом)