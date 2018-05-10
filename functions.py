def add(x, y):
	return x + y


add(1,10)
11
add('abc', 'def')
'abcdef'


----------------------------
#Функция может быть любой сложности и возвращать любые объекты (списки, кортежи, и даже функции!):	

def newfunc(n):
	def myfunc(x):
		return x + n
	return myfunc
	
new = newfunc(100)      # new - это функция
new(200)		
300


def func(a, b, c=2):    # c - необязательный аргумент
    return a + b + c


func(1, 2)              # a = 1, b = 2, c = 2 (по умолчанию)
5


func(a, 2, 3)           # a = 1, b = 2, c = 3
6


func(a=1, b=3)          # a = 1, b = 3, c = 2
6


def func(*args):
	return args


func(1, 2 ,3, 'abc')
(1, 2, 3, 'abc')


func()
()

func(1)
(1,)	


def func(**kwargs):
	return kwargs


func(a=1, b=2, c=3)
{'a': 1, 'c': 3, 'b':2}


func()
{}


func(a='python')
{'a': 'python'}


#Анонимная функция lambda:

func = lambda x, y: x + y
func(1,2)
3


func('a', 'b')
'ab'

(lambda x, y: x + y) (1, 2)
3

(lambda x, y: x + y) ('a','b')
'ab'

# lambda функции, в отличие от обычной, не требуется инструкция return, а в остальном, ведет себя точно так же:

func = lambda *args: args

func(1, 2, 3, 4)
(1, 2, 3, 4)





