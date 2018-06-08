
def one():
	l = []
	for i in range(10**4):
		if i % 2 == 0:
			l.append(i)
	return l
	
l1 = one()
print(l1)



                         #---------------------------- Same thing --------------------#

def two():
	l = [i for i in range(10**4) if i % 2 == 0]
	return l

l2 = two()
print(l2)
