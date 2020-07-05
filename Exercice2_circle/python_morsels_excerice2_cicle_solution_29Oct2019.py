# w chuj wazne

import math

class Circle:

    def __init__(self, radius=1):

        self._set_radius(radius)
        # self.diameter = radius*2
        # self.area = math.pi*radius**2
    
    def _get_radius(self):
        return self._radius 

    def _set_radius(self, valeur):
        if valeur<0: raise ValueError("Radius cannot be negative")
        self._radius = valeur
        self._area = math.pi*valeur**2
    radius = property(_get_radius,_set_radius)

    def _get_diameter(self):
        return self.radius*2 

    def _set_diameter(self, valeur):
        self.radius = valeur/2

    diameter = property(_get_diameter,_set_diameter)

    def _get_area(self):
        return math.pi*self.radius**2

    def _set_area(self,value):

        raise AttributeError("Nie da sie tego zrobic, nieee")
    
    area = property(_get_area, _set_area)
    

    def __repr__(self):
        return f'Circle({self.radius})'
        # diameter = {self.diameter} and powierzchania = {round(self.area,2)}'

    
