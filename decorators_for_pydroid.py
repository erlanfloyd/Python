                                 #--------------- Общее понимание как образуется декоратор -----------------# 

def outside(func):
	def inside():
		return func() + 5
	return inside
	
def func_old():
	return 5

func_old = outside(func_old)
print(func_old())


                                 #--------------- Сам декоратор через синтаксис @ ---------------------#

def outside(func):
	def inside():
		return func() + 5
	return inside
@outside	
def func_old():
	return 2

print(func_old())




