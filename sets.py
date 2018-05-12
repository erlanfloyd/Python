                                 #----------Sets----------#
t = {1, 2, 3, 4, 5}
x = set(['spam', 'eggs', 'sausage'])
print(3 in t)
print('spam' not in x)



letters = {'a', 'b', 'c', 'd'}
if 'e' not in letters:
  print(1)
else:
  print(2)
  
  

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)




first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
