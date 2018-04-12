
 #------------------ Classes ---------------#
  
      
class Dog:
  legs = 4
  def __init__(self,name,color):
    self.name = name
    self.color = color
  
 
fido = Dog('Fido', 'brown')    
print(fido.legs)
print(Dog.legs)



class Student:
  def __init__(self,name):
    self.name = name
    
  def sayHi(self):
    print('Hi from' + self.name)
    
s1 = Student('Amy')
s1.sayHi()



class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
rect = Rectangle(7,8)
print(rect.color)



class Student:
  def __init__(self,name):
    self.name = name
test = Student('Bob')
print(test.name)












