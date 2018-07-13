#---- filter(func, iterable)


#---- Найти "о" в списке и вывести на экран списка ----#

def has_o(string):
	return 'o' in string.lower()

l = ['one', 'two', 'three', '27Fhkri']

n_l = list(filter(has_o, l))
print(n_l)


#---- Также можно записать через анонимную ф-цию lambda ----#

new_l = list(filter(lambda string: 'o' in string.lower(), l))
print(new_l)



#---- но лучше сделать через генератор списка(list comprehension) ----#

n_l2 = [string for string in l if has_o(string)]
print(n_l2)
