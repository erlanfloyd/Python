           #------------------------- Decorators -------------------------#

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






        #--------------------- Python's Decorator Syntax ---------------------#

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))





def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))    





 
        #--------------------- Debugging decorated functions ---------------------#

from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name

print(get_text.__name__) # get_text
print(get_text.__doc__) # returns some text
print(get_text.__module__) # __main__





       
       #-------------------- Passing arguments to decorators --------------------#

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name

print(get_text("John"))





    #-------------------- Decorating Methods --------------------#
    
def p_decorate(func):
   def func_wrapper(self):
       return "<p>{0}</p>".format(func(self))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print(my_person.get_fullname())    


"""
A much better approach would be to make our decorator useful for functions and methods alike. This can be done by putting args and *kwargs as parameters for the wrapper, then it can accept any arbitrary number of arguments and keyword arguments.
"""

def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()

print(my_person.get_fullname())
