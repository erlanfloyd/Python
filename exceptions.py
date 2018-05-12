
try:
  word = 'spam'
  print(word/0)
except:
  print('An error occurred')
  

try:
  num1 = input(':')
  num2 = input(':')
  print(float(num1)/float(num2))
except:
  print('Invalid input')
  

try:
  print('Hi')
  print(1/0)
except ZeroDivisionError:
  print('Divided by zero')
finally:
  print('This code will run no matter what')
  

try:
  print(1)
except:
  print(2)
finally:
  print(3)
  
  
try:
  num = 5/0
except:
  print('An error occurred')
  
  
try:
  with open('test.txt') as f:
    print(f.read())
except:
  print('Error')  

