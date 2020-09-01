
# Descriptors are Python objects that implement a method of the descriptor protocol,
#  which gives you the ability to create objects that have special behavior
#   when they’re accessed as attributes of other objects.
#  Here you can see the correct definition of the descriptor protoco

# __get__(self, obj, type=None) -> object
# __set__(self, obj, value) -> None
# __delete__(self, obj) -> None
# __set_name__(self, owner, name)


# he example above makes use of decorators to define a property, 
# but as you may know, decorators are just syntactic sugar. 
# The example before, in fact, can be written as follows:

#property(fget=None, fset=None, fdel=None, doc=None) -> object

class Positive_Attributes():
    def __init__(self,value=0):
        self.att = value

    def __get__(self,obj,type=None) -> object:
        print("getting value of the parameter")
        return self.att*10
    
    def __set__(self,obj,value) -> None:
        print("setting value of the parameter")
        if value<0: raise AttributeError("Values of this parameter have to be positive")
        self.att = value

class Foo0():
    attribute1 = Positive_Attributes(value=0) 

    def __str__(self):
        return f"Our object hqs the folliwing values {self.attribute1}"

class Foo():
    @property
    def attribute1(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    @attribute1.setter
    def attribute1(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


a = Foo0()
print(a)
a_x = a.attribute1
print(a_x)
a.attribute1 = 3
a.attribute1 = 33

b = Foo0()
print(b) 

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)