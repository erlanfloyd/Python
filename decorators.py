          #------------------------ Decorators ------------------------#

def addOne(myFunc):
  def addOneInside():
    return myFunc() + 1
  return addOneInside
  
def oldFunc():
  return 3
  
oldFunc = addOne(oldFunc)
print(oldFunc())





def addOne(myFunc):
  def addOneInside():
    return myFunc() + 1
  return addOneInside
  
@addOne
def oldFunc():
  return 3

print(oldFunc())  






def outside():
  x = 5
  def printHam():
    print(x)
  return printHam
  
myFunc = outside()
myFunc()




def outside():
  def printHam():
    print("Ham")
  return printHam
  
myFunc = outside()
myFunc()





def Outside():
  def Inside():
    print("Let us know")
  return Inside()
  
myFunc = Outside
myFunc()






def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
 
@makebold
@makeitalic
def hello():
    return "hello habr"
 
print(hello()) ## выведет <b><i>hello habr</i></b>
