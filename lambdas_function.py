ggg = lambda x: x * 2 
print(ggg(5))


a = (lambda x: x*x)(8)
print(a)


b = (lambda x: x + 5)(10)
print(b)


triple = lambda x: x*3
add = lambda x,y: x + y 
print(add(triple(10),5))



z = (lambda x: x**2 + 5*x + 4)(-4)
print(z)


def hhh(x):
  return x**2 + 5*x + 4
print(hhh(-4))