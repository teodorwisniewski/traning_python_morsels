import math


# class Circle:
    
#     def __init__(self,radius=1):
#         self.radius = radius
#         self.diameter = 2*math.pi*self.radius




# class Circle:
    
#     def __init__(self,radius=1):
#         self.radius = radius
    
#     @property
#     def diameter(self):
#         return 2*math.pi*self.radius
    
#     @diameter.setter
#     def diameter(self,value):
#         self.radius = value/2

class Circle:
    
    def __init__(self,radius=1):
        self.radius = radius
    
    def get_diameter(self):
        return 2*math.pi*self.radius

    def set_diameter(self,value):
        self.radius = value/2

    diameter = property(get_diameter,set_diameter)

if __name__ == "__main__":

    c = Circle()
    c.radius = 100

    d = Circle(radius=10)
    d.diameter = 1000

    print(f"c cirle: radius={c.radius}, diameter={c.diameter: .2f}")
    print(f"d cirle: radius={d.radius}, diameter={d.diameter: .2f}")