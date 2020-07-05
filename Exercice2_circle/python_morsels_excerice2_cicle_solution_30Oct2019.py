import math

class Circle:

    def __init__(self, radius=1):

        self._set_radius(radius)

    def _get_radius(self):
        
        return self._radius

    def _set_radius(self, value):
        if value<0 :raise ValueError("Radius cannot be negative")
        self._radius = value
        self._diameter = value*2
        self._area = math.pi*value**2

    radius = property(_get_radius,_set_radius)

    def _getter_diameter(self):
        return self._diameter

    def _setter_diameter(self,value):
        
        self._set_radius(value/2)

    diameter = property(_getter_diameter,_setter_diameter)


    def _area_getter(self):
        return self._area()

    def _area_setter(self,value):
        raise AttributeError("nie da sie")

    area =property(_area_getter, _area_setter)
    
    def __repr__(self):
        return f'Circle({self.radius})'






print("*"*50)

a = Circle()
print(a)
a.diameter = 10
print(a)

a.radius = -10
