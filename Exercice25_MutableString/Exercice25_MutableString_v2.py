from collections import UserString

class MutableString(UserString):
    def __setitem__(self, index, value):
        chars = list(self.data)
        chars[index] = value
        self.data = "".join(chars)

    def __delitem__(self, index):
        chars = list(self.data)
        del chars[index]
        self.data = "".join(chars)

    def append(self,text):
        self.data += text

    def insert(self,index,value):
        self.data = self.data[:index] + value + self.data[index:]

    def pop(self, index=None):
        chars = list(self.data)
        
        if index is None: pop_char = chars.pop()
        else: 
            pop_char = chars[index]
            del chars[index]
        self.data = "".join(chars)
        return MutableString(pop_char)

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