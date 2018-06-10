#------------- Декоратор метода def sayYourAge(self, lie) -------------#

def method_decorator(method_to_decorate):
	def wrapper(self, lie):
		lie = lie - 3
		return method_to_decorate(self, lie)
	return wrapper
	

class Liza():
	def __init__(self):
		self.age = 35

	@method_decorator
	def sayYourAge(self, lie):
		print("I'am {}, what did you think?".format(self.age + lie))

liza = Liza()
liza.sayYourAge(-3)
