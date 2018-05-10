
#name = 'Yerlan'
#age = 31

#print('Имя {0} -- Возраст {1} лет.'.format(name, age))




class ShortInputException(Exception):
  def __init__(self, length, atleast):
    Exception.__init__(self)
    self.length = length
    self.atleast = atleast
  

try:
  text = input('Are you kidding me?')
  if len(text) < 3:
    raise ShortInputException(len(text), 3)

except EOFError:
  print('Why we created EOF?')
except ShortInputException as ex:
  print('ShortInputException: Length of string -- {0}; \
  hold on like one {1}'.format(ex.length, ex.atleast))
else:
  print('Do not transffering!')
  
  
  
  

  
  
 

