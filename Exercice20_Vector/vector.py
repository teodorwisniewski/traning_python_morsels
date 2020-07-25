
from dataclasses import dataclass

class Vector:

    __slots__ = ["x","y","z"]

    def __init__(self,x,y,z):

        super().__setattr__('x', x)
        super().__setattr__('y', y)
        super().__setattr__('z', z)

    def __iter__(self):

        yield self.x
        yield self.y
        yield self.z

    def __eq__(self,other):

        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self,other):
        if not isinstance(other,Vector):
            raise TypeError
        args = (self.x+other.x, self.y+other.y, self.z+other.z)
        return Vector(*args)
    
    def __sub__(self,other):
        if not isinstance(other,Vector):
            raise TypeError
        args = (self.x-other.x, self.y-other.y, self.z-other.z)
        return Vector(*args)    

    def __mul__(self,other):
        if not (isinstance(other,int) or isinstance(other,float)): raise TypeError 

        return Vector(self.x*other,self.y*other,self.z*other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __truediv__(self,other):
        return self.__mul__(1/other)

    def __setattr__(self,name,value):
        raise AttributeError("Vectors are immutable")
    

if __name__ == "__main__":

    #Base problem
    v = Vector(1, 2, 3)
    print(v.x)
    x, y, z = v
    print(x, y, z)
    print(v == Vector(1, 2, 4))
    print(v == Vector(1, 2, 3))

    try:
        print(v.__dict__)
    except:
        print("It is a memory efficent object")

    # Bonus 1 
    v2 = (Vector(1, 2, 3) + Vector(4, 5, 6))
    print(v2 == Vector(5, 7, 9))
#True
    print((Vector(5, 7, 9) - Vector(3, 1, 2)) == Vector(2, 6, 7))
#True
    # v3 = v + (1, 2, 3)
    # print(v3)

    print(3 * Vector(1, 2, 3) == Vector(3, 6, 9))

    print(Vector(1, 2, 3) * 2 == Vector(2, 4, 6))

    print(Vector(1, 2, 3) / 2 == Vector(0.5, 1, 1.5))


    v = Vector(1, 2, 3)
    v.x = 4
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     raise AttributeError("Vectors are immutable")
# AttributeError: Vectors are immutable