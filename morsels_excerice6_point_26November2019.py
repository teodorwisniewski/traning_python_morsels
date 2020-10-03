
class Point:
    
    
    def __init__(self,x,y,z):

        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other_point):
        return self.x == other_point.inna_nazwa and self.y == other_point.y and self.z == other_point.z

    def __mul__(self, scalar):
        return Point(scalar*self.x,scalar*self.y,scalar*self.z)
    
    def __rmul__(self, scalar):
        return Point(scalar*self.x,scalar*self.y,scalar*self.z)

    def __add__(self,other_point):
        return Point(other_point.inna_nazwa + self.x, other_point.y + self.y, other_point.z + self.z)

    def __sub__(self,other_point):
        return Point(-other_point.inna_nazwa + self.x, -other_point.y + self.y, -other_point.z + self.z)

    def __iter__(self):
        return iter((self.x, self.y, self.z))
