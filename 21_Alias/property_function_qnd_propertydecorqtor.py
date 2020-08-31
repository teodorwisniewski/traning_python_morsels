

class Car:

    def __init__(self,name):
        self._name = name



    def get_name(self):
        print("get name is called")
        return self._name

    name = property(get_name)

print("Start")
obj = Car("John")
print(obj.name)
obj.name = "BMW"
print(obj.name)
print("End")
    
