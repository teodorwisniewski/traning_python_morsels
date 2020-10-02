
from functools import wraps

def _proxy(func_name):
    @wraps(func_name)
    def inner_func(self,*args,**kwargs):
        ret = getattr(self.data,func_name)(*args,**kwargs)
        if isinstance(ret,str) and (func_name !='__str__' and func_name !='__repr__'): ret = MutableString(ret)
        return  ret
    return inner_func



class MutableString:

    def __init__(self,data=""):
        self.data = data

    def __eq__(self, other):
        return self.data == other

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self.data + other.data)
        else:
            return MutableString(self.data + other   )

    def __setitem__(self,index,val):
        characters = list(self.data)
        characters[index] = val
        self.data = "".join(characters)
        
    def __getitem__(self,index):
        characters = list(self.data)
        return characters[index]  

    def __delitem__(self,index):
        characters = list(self.data)
        del characters[index]
        self.data = "".join(characters)

    def append(self,chara):
        characters = list(self.data)
        characters.append(chara)
        self.data = "".join(characters)

    def insert(self,index,chara):
        characters = list(self.data)
        characters.insert(index,chara)
        self.data = "".join(characters)        

    def pop(self,index=None):
        if index is None: index = len(self)-1
        characters = list(self.data)
        chara = characters[index]
        del characters[index]
        self.data = "".join(characters)  
        return MutableString(chara)


    __str__ = _proxy('__str__')
    __repr__ = _proxy('__repr__')
    __len__ = _proxy('__len__')
    __getitem__ = _proxy('__getitem__')
    __contains__ = _proxy('__contains__')
    replace = _proxy('replace')
    lower = _proxy('lower')
    upper = _proxy('upper')
    endswith = _proxy('endswith')

if __name__ == "__main__":

    greeting = MutableString("Hello world!")
    print(greeting)
# 'Hello world!'
    greeting[4] = "a"
    print(greeting)
# 'Hella world!'



    greeting = MutableString("Hello world!")
    print(greeting.endswith('!'))
    # True
    print(greeting + MutableString('!'))
    # 'Hella world!!'
    print((greeting + '?').lower())
    # 'hello world!?'
    print('la' in greeting)
    # True
    print(len(greeting))
    # 12

    greeting = MutableString("hiya")
    print(greeting[-3:]== "iya")

# Bunus 1

    greeting = MutableString("Hello world!")
    greeting[6:-1] = "there"
    print(greeting)
   # 'Hello there!'
    del greeting[5:-1]
    print(greeting)
   # 'Hello!'
    del greeting[-1]
    print(greeting)
    #'Hello world'

# Bonus 2

# For the second bonus, you should make sure various operations on your class return MutableString objects:

    greeting = MutableString("Hello world!")
    exclamation = greeting[-1]
    hello = greeting[:5]
    print(type(exclamation), type(hello))
    # (<class 'MutableString'>, <class 'MutableString'>)
    double_exclamation = exclamation + "!"
    lowercased_hello = hello.lower()
    print(type(double_exclamation), type(lowercased_hello))
    # (<class 'MutableString'>, <class 'MutableString'>)
    characters = list(double_exclamation)
    print([type(c) for c in characters])
    # [<class 'MutableString'>, <class 'MutableString'>]


# Bonus 3
    greeting = MutableString("Hello world")
    greeting.append("!")
    print(greeting)
    # 'Hello world!'
    greeting.insert(5, "o")
    print(greeting)
    # 'Helloo world!'
    greeting.pop(5)
    print(greeting)
    # 'Hello world!'
    greeting.pop()
    print(greeting)
    # 'Hello world'

    greeting = MutableString("heya")
    print(greeting.pop(-2))
    print(greeting)