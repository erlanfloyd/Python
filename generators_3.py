                                     #--------------- Список через уикл for ------------------#

def one():
	l = []
	for i in range(10**4):
		if i % 2 == 0:
			l.append(i)
	return l
	
l1 = one()
print(l1)			



                                    #--------------- Список через генератор ------------------#

def two():
	l = [x for x in range(10**4) if x % 2 == 0]
	return l

l2 = two()
print(l2)
