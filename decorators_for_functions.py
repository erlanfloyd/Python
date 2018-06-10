#--------- Декоратор - это ф-ция которая оборачивает нашу функцию print_string() -----------#

def decorator(func_to_decorate):
	def wrapper():
		print("Before function runs")
		func_to_decorate()
		print("After function runs")
	return wrapper
	
@decorator

#--------- Ф-ция (основная, все идет от нее) которую мы оборачиваем -----------#

def print_string():
	print("I'am print_string() function!")
print_string()			






#--------- Передача параметров в ф-ции окруженные декоратором (проброс) -----------#

def decorator_passing_arguments(func_to_decorate):
	def wrapper_with_arg(arg1, arg2):
		print("I got args! Look:", arg1, arg2)
		func_to_decorate(arg1,arg2)
	return wrapper_with_arg
	
@decorator_passing_arguments

def print_fullname(first_name, last_name):
	print("My name is", first_name, last_name)

print_fullname("kostya", "kokorin")


