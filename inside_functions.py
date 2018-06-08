                                   #------------------------ Вложенные функции ---------------------#
def Outside():
	def Inside():
		print("Canelo")
	return Inside()
	
myFunc = Outside
myFunc()




def outside():
	def inside():
		print("GGG")		
	return inside
	
myFunc = outside()
myFunc()




def outside():
	x = 5
	def inside():
		print(x)
	return inside 
	
myFunc = outside()
myFunc()
