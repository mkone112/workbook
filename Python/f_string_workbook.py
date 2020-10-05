 ФОРМАТИРОВАННЫЕ СТРОКОВЫЕ ЛИТЕРАЛЫ
 #подробнее: https://www.python.org/dev/peps/pep-0498/
 #пробелы вокруг exp недопустимы
 	f'{ x }'		>> ok
 	f'{ x:.2f }'	>> err
 #быстрее .format|%|templates
 #при exe exp в них оцериваются в собственной(?отдельной) ns 
	f'<chars>{exp}<chars>'
	F'<chars>{exp}<chars>'
	#exp оцениваются по мере exe и заменяются своими val при помощи __format__
	#примеры
		f'{2 * 37}'
		f'{sum(1,2)}'
		#разумеется присвоения запрещены
		f'{a=1}'	>> SyntaxErr
	#для obj исп их str представление(__str__)|__repr__ при его отсутствии
		class Comedian:
			def __init__(self, first_name, last_name, age):
				self.first_name = first_name
				self.last_name = last_name
				self.age = age
			
			def __str__(self):
				return f'{self.first_name} {self.last_name} is {self.age}.'
				
			def __repr__(self):
				return f'{self.first_name} {self.last_name} is {self.age}. Surprise!'
		
		new_comedian = Comedian("Eric", "Idle", "74")
		
		print(f'{new_comedian}')	>> 'Eric Idle is 74.'
	
	ФЛАГИ ПРЕОБРАЗОВАНИЯ
		!r
		#исп __repr__ вместо __str__
			class C:
				def __init__(self):
					...
				
				def __str__(self):
					return 'str'
				
				def __repr__(self):
					return 'repr'
			
			c_instance = C()
			
			print(f'{c_instance}')	>> 'str'
			print(f'{c_instance!r}')	>> 'repr'

МНОГОСТРОЧНЫЕ F-STRINGS
#~str
	#разумеется f' должен быть у ∀ str
	#без скобок - вернет только последнюю строку(~обычным str)
	msg = {
		f'Hi {name}'
		f'You are a {profession}'
	}
	f'''
	sadf
	'''
СКОБКИ
#доп четные скобки вроде как отключают оценку exp
	f'{ age }'			>> '74'
	f'{{ age }}'			>> '{age}'
	#хз почему
	f'{{{ age }}}'		>> '{74}'
	f'{{{{ age }}}}'	>> '{{age}}'
	f'{{{{{ age }}}}}'	>> '{{74}}'
	
ПРОБЕЛЬНЫЕ СИМВОЛЫ ИГНОРИРУЮТСЯ
	f'{		age }'		>> '74'
	
exp не может ⊃ '\' '#' и ничего
	f'{"\t"}'		>> SyntaxErr: f-string expression part cannot include a backslash
	#можно оценивать exp заранее
	tab = "\t"
	f'{tab}'		>> ok
	f'{}'			>> SyntaxErr
	f'{1 #}'		>> SyntaxErr

КОМБИНАЦИЯ С RAW СТРОКАМИ
fr'asdf'

