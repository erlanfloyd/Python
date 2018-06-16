# Имеется вложенный список

l = [21, 2, [3, 12, True], [10, 13, 'Hello', False] ]

# Надо заменить 'Hello'на 'Goodbye' 

l[3][2] = 'Goodbye'
print(l)
