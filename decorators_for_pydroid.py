                                 #--------------- Общее понимание как образуется декоратор -----------------# 

def decorator(func_to_decorate):
	def wrapper():
		return func_to_decorate() + 5
	return wrapper
	
def func_old():
	return 5

func_old = decorator(func_old)
print(func_old())


                                 #--------------- Сам декоратор через синтаксис @ ---------------------#

def decorator(func_to_decorate):
	def wrapper():
		return func_to_decorate() + 5
	return wrapper

@decorator	
def func_old():
	return 2

print(func_old())




