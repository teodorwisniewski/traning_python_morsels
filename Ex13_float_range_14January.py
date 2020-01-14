from pprint import pprint


import math
                  


class float_range:

    def __init__(self, first,second=None,step=1.0):
        if second is None:
            second = first
            first = 0.0        
        self.first = first
        self.second = second
        self.step = step

    def __iter__(self):
        last_point = self.first
        if self.first<self.second and self.step>0:
            while last_point<self.second:
                yield last_point
                last_point += self.step
        elif self.first>self.second and self.step<0:
            while last_point>(self.second):
                yield last_point
                last_point += self.step  

    def __len__(self):
        wielkosc = 0
        last_point = self.first
        if self.first<self.second and self.step>0:
            wielkosc = int(math.ceil((self.second - self.first)/self.step))
        elif self.first>self.second and self.step<0:
            wielkosc = int(math.ceil((self.second - self.first)/self.step))
        return wielkosc

    def __reversed__(self):
        self.first, self.second, self.step = self.second-self.step, self.first, -self.step
        last_point = self.first
        if self.first<self.second and self.step>0:
            while last_point<=self.second:
                yield last_point
                last_point += self.step
        elif self.first>self.second and self.step<0:
            while last_point>=(self.second):
                yield last_point
                last_point += self.step  

    def __eq__(self, other):
        if isinstance(other,range):
            if self.second is None:
                return range(int(self.first)) == other
            else:
                return range(int(self.first),int(self.second),int(self.step)) == other    
        elif isinstance(other,float_range):
            return (self.first, self.second, self.step) == (other.first, other.second, other.step) 
        else:
            return False



# def float_range(first,second=None,step=1.0):

#     if second is None:
#         second = first
#         first = 0.0

#     last_point = first
#     if first<second and step>0:
#         while last_point<second:
#             yield last_point
#             last_point += step
#     elif first>second and step<0:
#         while last_point>(second):
#             yield last_point
#             last_point += step  


if __name__ == "__main__":
    for n in float_range(0.5, 2.5, 0.5):
        print(n)

#     0.5
# 1.0
# 1.5
# 2.0

    print(list(float_range(3.5, 0, -1)))
    # [3.5, 2.5, 1.5, 0.5]
    for n in float_range(0.0, 3.0):
        print(n)

# ...
# 0.0
# 1.0
# 2.0
    for n in float_range(3.0):
        print(n)
    a = list(float_range(1, 6, -1))
    print(a)

    print(len(float_range(0.5, 2.5, 0.5)))
    print(len(float_range(10, 5, 1.5)))
    print(len(float_range(10, 5, -1.5)))
    print(len(float_range(5, 10, -1.5)))


    print(list(reversed(float_range(0.5, 2.5, 0.5))))

    a = float_range(0.5, 2.5, 0.5)
    b = float_range(0.5, 2.5, 0.5)
    c = float_range(0.5, 3.0, 0.5)
    d = float_range(5)
    e = float_range(4)
    print(a == b)
    print(a == c)
    print(d == range(0, 5))
    print(e == range(5))
    print(e == 3)
# seconda == b

# True
# seconda == c
# False