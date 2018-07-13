          #-------------- else у циклов for and while ------------#

for i in range(5):
	if i == 6:
		print(i)
		break
else:
	print('The end')	



         #-------------- Синтаксический сахар(тоже самое) ------------#

flag = False
for i in range(5):
	if i == 4:
		flag = True
		break

if flag:
	print('Six was found')
