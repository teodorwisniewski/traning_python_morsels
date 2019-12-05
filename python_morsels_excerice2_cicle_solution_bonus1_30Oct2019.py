import math


class Circle:

    def __init__(self, radius=1):
        self.radius = radius
    
    @property
    def radius(self):
        # _radius encapsulation uzycie lokalne
        return self._radius
    
    @radius.setter
    def radius(self,value):
        if value <0:
            raise ValueError("Radius cannot be neggative")
        # _radius encapsulation uzycie lokalne
        self._radius = value


# ten decorator dziala jak definicja gettera
    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter # zwroc uwage na ten synteax tego decoratora
    def diameter(self, value):
        self.radius = value/2

    @property 
    def area(self):
        return math.pi*self.radius**2


    def __repr__(self):
        return f"Circle({self.radius}) diameter {self.diameter} area = {self.area}"


a = Circle()
print(a)

a.radius =3

print(a)

a.diameter = 3

print(a)

a.radius =- 5