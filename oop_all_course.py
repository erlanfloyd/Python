
         #------------------ Magic Methods --------------#

class GGG:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __add__(self,other):
		return GGG(self.x + other.x, self.y + other.y)

first = GGG(5,7)
second = GGG(3,9)
result = first + second
print(result.x)
print(result.y)



class Saul:
	def __init__(self,cont):
		self.cont = cont

	def __truediv__(self,other):
		line = '='*len(other.cont)
		return '\n'.join([self.cont, line, other.cont])

spam = Saul('spam')
hello = Saul('Mexico!')
print(spam/hello)		
		

           #------------------ Inheritance ---------------#

class Animal:
	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight

class Cat(Animal):
    def purr(self):
    	print('Purr...')

class Dog(Animal):
	def bark(self):
		print('Woof!')

fido = Dog('Fido', 'brown', ',' ' ' '25 kg')
burak = Cat('Burak', 'smoke', '5 kg')

print(fido.color, fido.weight)	
fido.bark()

print(burak.name, burak.color, burak.weight)
burak.purr()	


	

class Wolf:
    def __init__(self, name, color):
    	self.name = name
    	self.color = color

    def bark(self):
        print('Grr...')


class Dog(Wolf):
    def bark(self):
        print('Woof')

wolf = Wolf('Arlan', 'black')
print(wolf.name, wolf.color)
wolf.bark()

hasky = Dog('Max', 'grey')
hasky.bark()





class A:
	def method(self):
		print('A method')

class B(A):
	def another_method(self):
		print('B method')

class C(B):
    def third_method(self):
        print('C method')

c = C()
c.method()
c.another_method()
c.third_method()        		



class A:
	def a(self):
		print(1)

class B(A):
    def a(self):
        print(2)

class C(B):
    def c(self):
        print(3)

c = C()
c.a()     




class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()
B().spam()





             #----------- Class Methods -----------#

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
         return self.width * self.height

    @classmethod
    def saiHi(cls):
        print('Hi')




class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())    





class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == 'pineapple':
            raise ValueError('No pineapples!')
        else:
            return True 

ingredients = ['cheese', 'onions', 'spam']
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)





             #------------ Properties ------------#

class Person:
    def __init__(self, age):
        self.age = int(age)

    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else: 
            return False

person = Person(25)
print(person.isAdult)                                                               




class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings
		self._pineapple_allowed = False

	@property
	def pineapple_allowed(self):
	    return self._pineapple_allowed

	@pineapple_allowed.setter
	def pineapple_allowed(self, value):
	    if value:
	        password = input('Enter the password:')
	        if password == 'GGG!':
	            self._pineapple_allowed = value
	        else:
	            raise ValueError('Alert! Intruder!')

pizza = Pizza(['cheese', 'tomato'])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed) 	                        	