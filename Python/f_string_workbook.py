ФОРМАТИРОВАННЫЕ СТРОКОВЫЕ ЛИТЕРАЛЫ
#подробнее: https://www.python.org/dev/peps/pep-0498/
#быстрее .format|%
#при exe exp в них оцериваются в собственной(?отдельной) ns 
	#оцениваются по мере exe и заменяются своими val при помощи __format__
	f'<chars>{exp}<chars>'
	F'<chars>{exp}<chars>'
#разумеется присвоения запрещены
	f'{a=1}'	>> SyntaxErr
#для obj исп их str представление(__str__ If (__str__ ∃) Else __repr__)
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
#флаги преобразования
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
#многострочные f-strings(~str)
	#разумеется f' должен быть у ∀ str
	#без скобок - вернет только последнюю строку(~обычным str)
	msg = {
		f'Hi {name}'
		f'You are a {profession}'
	}
	f'''
	sadf
	'''
#доп четные скобки вроде как отключают оценку exp(?хз почему)
	f'{ age }'			>> '74'
	f'{{ age }}'			>> '{age}'
	f'{{{ age }}}'		>> '{74}'
	f'{{{{ age }}}}'	>> '{{age}}'
	f'{{{{{ age }}}}}'	>> '{{74}}'
#пробельные символы игнорируются
	f'{		age }'		>> '74'
#exp не может ⊃ '\' '#' и ничего
	f'{"\t"}'		>> SyntaxErr: f-string expression part cannot include a backslash
#можно оценивать exp заранее
	tab = "\t"
	f'{tab}'		>> ok
	f'{}'			>> SyntaxErr
	f'{1 #}'		>> SyntaxErr
#комбинация с raw строками
	fr'asdf'
#examples
	f'{2 * 37}'
	f'{sum(1,2)}'

names = ['Adam', 'Bob', 'Cyril']
nl = '\n'
text = f"Winners are:{nl}{nl.join(names)}"
print(text)

MULTILINE/LONG
return (
	f'one{arg}\n'
	f'two{arg}'
)