






class Vector:

    #This is usually done to save memory (if you have one million class instances,
    # a tuple for each is much less memory intensive than a dictionary for each).
    #memory efficient feauture to avoir usin inefficient __dict__ to store attributes
    __slots__ = "x","y","z"

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z



    def __iter__(self):
        # it makes vector object also iterable
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self,other):
        return tuple(self) == tuple(other)

if __name__ == "__main__":

    #Base problem
    v = Vector(1, 2, 3)
    print(v.x)
    x, y, z = v
    print(x, y, z)
    print(v == Vector(1, 2, 4))
    print(v == Vector(1, 2, 3))

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

    print(3 * Vector(1, 2, 3) == Vector(3, 6, 9))

    print(Vector(1, 2, 3) * 2 == Vector(2, 4, 6))

    print(Vector(1, 2, 3) / 2 == Vector(0.5, 1, 1.5))


    v = Vector(1, 2, 3)
    v.x = 4
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     raise AttributeError("Vectors are immutable")
# AttributeError: Vectors are immutable