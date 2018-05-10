       #------------------ Simple Function --------------#

def ggg(x):
  return x + 5
nums = [11,22,33,44,55]
result = list(map(ggg,nums))
print(result)

       #------------------ Map --------------#

nums = [11,22,33,44,55]
result = list(map(lambda x: x + 5, nums))
print(result)


nums = [11,22,33]
a = list(map(lambda x: x*2, nums))
print(a)


nums = (10,20,30)
b = tuple(map(lambda x: x*2, nums))
print(b)


nums = (10,20,30)
c = set(map(lambda x: x+5, nums))
print(c)

#------------------ Filter --------------#
 
nums = [11,22,33,44,55]
res = list(filter(lambda x: x%2 == 0, nums))
print(res)


nums = (11,22,33,44,55,66)
a = tuple(filter(lambda x: x%2 == 0, nums))
print(a)


nums = (11,22,33,44,55,66)
b = set(filter(lambda x: x%3 == 0, nums))
print(b)


nums = [1,2,5,8,3,0,7]
res = list(filter(lambda x: x<5, nums))
print(res)
