#---- map(func, *iterable)

def upper(string):
	return string.upper()


l = ['one', 'two', 'three']

new_list = list(map(upper, l))
print(new_list)	



#---- map применяется когда есть анонимная ф-ция lambda ----#

new_l = list(map(lambda string: string.upper(), l))
print(new_l)


#---- но лучше сделать через генератор списка(list comprehension) ----#

n_l = [string.upper() for string in l]
print(n_l)
