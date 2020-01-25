from math import ceil

class float_range:


    def __init__(self,start,stop=None,step=1):

        if stop is None:
            start,stop = 0, start
        
        self.start,self.stop,self.step = (start,stop,step)

    def __iter__(self):
        
        out = self.start
        for _ in range(len(self)):
            yield out
            out += self.step



    def __len__(self):

        # len(float_range(10, 5, 1.5))
        if self.start>self.stop and self.step>0: 
            return 0
        # len(float_range(5, 10, -1.5))
        elif self.start<self.stop and self.step<0:
            return 0

        # any other case
        result = abs((self.stop - self.start)/self.step)
        rounded_result = ceil(result)
        return rounded_result

    def __reversed__(self):
        out = self.start + (len(self)-1)*self.step
        for _ in range(len(self)):
            yield out
            out -= self.step

    def __eq__(self,other):

        if isinstance(other,(float_range,range)):
            if len(self) == len(other) <= 1:
                return list(self) == list(other)
            tuple_one = (self.start,self.start + (len(self)-1)*self.step,self.step)
            tuple_other = (other.start,other.start + (len(other)-1)*other.step,other.step)
            return tuple_one == tuple_other
        else:
            return NotImplemented




if __name__ == "__main__":
    for n in float_range(0.5, 2.5, 0.5):
        print(n)

#     0.5
# 1.0
# 1.5
# 2.0

    # print(list(float_range(3.5, 0, -1)))
    # [3.5, 2.5, 1.5, 0.5]
    for n in float_range(0.0, 3.0):
        print(n)

# ...
# 0.0
# 1.0
# 2.0
    for n in float_range(3.0):
        print(n)

    for n in float_range(3.5, 0, -1):
        print(n)


##################"#################################################""""
################## Bonus 1 ##################
# "#################################################""""
    print(len(float_range(0.5, 2.5, 0.5)))
    print(len(float_range(10, 5, 1.5)))
    print(len(float_range(10, 5, -1.5)))
    print(len(float_range(5, 10, -1.5)))

##################"#################################################""""
################## Bonus 2 ##################
# "#################################################"""
    for el in reversed(float_range(0.5, 2.5, 0.5)):
        print(el)

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