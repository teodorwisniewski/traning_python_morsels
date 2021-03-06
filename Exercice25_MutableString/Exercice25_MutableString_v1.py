from collections import UserString


class MutableString(UserString):

    def __getitem__(self,indexes):
        list_char = list(self.data)
        if isinstance(indexes,slice):
            return ''.join(list_char[indexes])    
        else:
            return list_char[indexes]
    
    def __setitem__(self,index,value:str)->None:
        list_char = list(self.data)
        list_char[index] = value
        self.data = ''.join(list_char)

    def __delitem__(self,indexes):
        list_char = list(self.data)
        del list_char[indexes]
        self.data = ''.join(list_char)





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
