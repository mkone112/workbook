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
	
Δ модели -> makemigration -> You are trying to add a non-nullable field <field_name> to <model_name> without a default...
	1) Provide a one-off default... -> ввод def val для уже ∃ полеи
	#допускаются валидные python exp ⊃ django.utils.timezone & datetime модули
	2) Quit & let me add a defaut in models.py -> самому добавить null=True|default=<default_val> в модель