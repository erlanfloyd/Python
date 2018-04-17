"""
Class methods are marked with a classmethod decorator
Example:

"""
class Person:
	def __init__(self, name):
		self.name = name

	@classmethod
	def sayHi(cls):
	    print('Hi')

person = Person('John')
print(person.name)
person.sayHi()	    	
