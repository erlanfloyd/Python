x = int(input('x: '))
y = int(input('y: '))

l = []
h = []

for i in range(x):
    l.append(i)

for i in range(y):
    h.append(i)

l_h = set(l) - set(h)
h_l = set(h) - set(l)

if l_h:
    print(x)
else:
    print(y)