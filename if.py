number = 23
guess = int(input('Введите целое число : '))

if guess == number:
	print('Поздравляю, вы угадали!')
elif guess < number:
	print('Нет, загаданное число немного больше этого.') 
else:
	print('Нет, загаданное число немного меньше этого.')
	
print('Завершено')