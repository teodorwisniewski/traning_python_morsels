from operator import add,sub
from numbers import Number

class Vector:

    __slots__ = "x","y","z"

    def __init__(self,x,y,z):
        super().__setattr__("x",x)
        super().__setattr__("y",y)
        super().__setattr__("z",z)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
    
    def __eq__(self,other):
        return tuple(self) == tuple(other)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(*(a + b for a, b in zip(self, other)))

    def __sub__(self,other):
        if not isinstance(other,Vector): return NotImplemented
        return Vector(*(a - b for a, b in zip(self, other)))

    def __mul__(self, scalar):
        if not isinstance(scalar, Number):
            return NotImplemented
        return Vector(*(scalar * a for a in self))
    __rmul__ = __mul__

    def __truediv__(self,scalar):
        if not isinstance(scalar, Number):
            return NotImplemented
        return self.__mul__(1/scalar) 

    def __setattr__(self,name,values):
        raise AttributeError("Vector objects are immutable")      


if __name__ == "__main__":

    #Base problem
    v = Vector(1, 2, 3)
    print(v.x)
    x, y, z = v
    print(x, y, z)
    print(v == Vector(1, 2, 4))
    print(v == Vector(1, 2, 3))



    print(v)
    var = tuple(v)
    print(var)
# Vector object is an iterable
    for el in v:
        print(el)

    try:
        print(v.__dict__)
    except:
        print("It is a memory efficent object")

    # Bonus 1 
    v2 = Vector(1, 2, 3) + Vector(4, 5, 6)
    print(v2 == Vector(5, 7, 9))
#True
    print((Vector(5, 7, 9) - Vector(3, 1, 2)) == Vector(2, 6, 7))
#True
    # v3 = v + (1, 2, 3)
    # print(v3)
    spr = Vector(1, 2, 3)*3
    print(spr)
    print(3 * Vector(1, 2, 3) == Vector(3, 6, 9))

    print(Vector(1, 2, 3) * 2 == Vector(2, 4, 6))

    print(Vector(1, 2, 3) / 2 == Vector(0.5, 1, 1.5))


    v = Vector(1, 2, 3)
    v.x = 4
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     raise AttributeError("Vectors are immutable")
# AttributeError: Vectors are immutable