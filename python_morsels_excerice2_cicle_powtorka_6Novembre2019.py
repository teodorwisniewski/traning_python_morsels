import math

class Circle:

    def __init__(self,radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,value):
        if value<0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
        self._diameter = value * 2
        self._area = math.pi*value**2

    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self,value):
        self.radius = value/2

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self,value):
        raise AttributeError("Cannot attribure this shit")

    def __repr__(self):
        return f"Circle({self.radius})"




if __name__ == "__main__":

    c = Cirle(5)    
    print(f"rhe radius r={c.radius}, diameter ={c.diameter}, area ={c.area}")
    c.radius = 10
    print(f"rhe radius r={c.radius}, diameter ={c.diameter}, area ={c.area}")
    c.diameter = 23.33
    print(f"rhe radius r={c.radius}, diameter ={c.diameter}, area ={c.area}")

    c.area =3.33

        
