ДЕКОРАТОРЫ
#2.4+
#замедляют вызовы fx
#можно создать декоратор отсоединяемый от fx(раздекорирование) (вроде bad)
#оборачивание может затруднить поддержку

	#превращаем ∀ декоратор в принимающий args
	#предыдущий декоратор принимающий args создавался другой fx
	#принимаем декоратор для расширения и возвращаем новый
	def decorator_with_args(decorator_to_enhance):
		def decorator_maker(*args, **kwargs):
			"""принимает только fx, сохраняя ∀ args переданные создателю"""
			def decorator_wrapper(func):
				"""возвращаем результат исходного декоратора"""
				"""должен принимать именно такие args -> иначе exept"""
				return decorator_to_enhance(func, *args, **kwargs)
			return decorator_wrapper
		return decorator_maker

	#использование
	#создаем fx используемую как декоратор и декорируем ее
	@decorator_with_args
	def decorated_decorator(func, *args, **kwargs):
		def wrapper(func_arg0, func_arg1):
			return func(func_arg0, func_arg1)
		return wrapper
	@decorated_decorator(1,2,3)
	def func(a, b):
		print(a, b)

	func(1,2)		>> 1 2

#отладка
	functools.wraps
	#копирует ∀ информацию о оборачиваемой fx в wrapper(имя, расположение, docstring)
		def foo():
#позволяет дополнять/ИЗМ/заменять логику fx с помощью аннотирования однострочным интерфейсом	
#подходят для 
	переноса административного кода из основного потока
#pep-0318: обсуждение декораторов
#pep-3129: первое появление декораторов в 3.0