car = {'miles': '54000', 'model': 'nova', 'color': 'red', 'weight': '1250'}
print car
    for key in car:
    	print key + "=" + car[key]




def PrintDictionary(TheDictionary):
	for key in TheDictionary:
		print key + "=" + TheDictionary[key]


PrintDictionary(car)


software = {'title': 'Odoo', 'type': 'Buisness'}

PrintDictionary(software)


ages = {'John': 23, 'Saul': 55, 'GGG': 35}
print(ages['Saul'])
print(ages['GGG'])


cars = {'BMW': '7 series', 'Audi':'A6'}
print(cars['BMW'])


primary = {'red': [255,7,9], 'green': [3,55,77]}
print(primary['red'])
print(primary['green'])


nums = {1:'one', 2:'two', 3:'three'}
print(1 in nums)
print('three' in nums)
print(4 not in nums)


pairs = {1:'apple', 'orange':[2,3,4], True:False, None: 'True'}
print(pairs.get('orange'))
print(pairs.get(7))
print(pairs.get(12345, 'not in dictionary'))







