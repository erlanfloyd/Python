                  #---------------- Генераторы списков ---------------№
jack = {
	'name': 'jack',
	'car': 'bmw'
}                  

john = {
	'name': 'john',
	'car': 'audi'
}



users = [jack, john]

#jack, john = person

cars = [person['car'] for person in users]
print(cars)

                   #------------------------ Тоже самое разложение только через традиционный цикл for -----------------------------#

cars = []  
for person in users:
    cars.append(person['car'])

print(cars)                    


                    #------------------------ Теперь можно записать из этого цикла более короткий вариант ------------------#

new_cars =  [person['car'] for person in users]
print(new_cars)


                     #------------------------ Общая формула выглядит так ----------------------#

(values) = [ (expression) for (value) in (collection) ]

                      
                      #------------------------- Традиционный вариант выглядит так --------------#

(values) = []
for (value) in (collection):
    (values).append( (expression) )
                          