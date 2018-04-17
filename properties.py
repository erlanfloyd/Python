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
print(person.age)





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
      if password == 'GGG':
        self._pineapple_allowed = value
      else:
        raise ValueError('Alert! Intruder!')

pizza = Pizza(['cheese', 'tomato'])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)


