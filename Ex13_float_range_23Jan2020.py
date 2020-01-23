
from math import ceil


class float_range:

    def __init__(self,start,stop=None,step=1):

        if stop == None:
            start,stop = 0,start

        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):

        i = self.start
        for _ in range(len(self)):
            yield i 
            i +=self.step
    
    def __len__(self):
        if self.start<self.stop and self.step>0:
            return ceil((self.stop-self.start)/self.step)
        elif self.start>self.stop and self.step<0:
            return ceil((self.stop-self.start)/self.step)
        else:
            return 0

    def __reversed__(self):

        i = self.start + (len(self)-1)*self.step
        for _ in range(len(self)):
            yield i 
            i -=self.step



    def __eq__(self,other):
        if isinstance(other, (float_range,range)):
            if len(self) == len(other) <= 1: #a < b < c   means   (a < b) and (b < c)
                return list(self) == list(other)
            first_element_boolean = next(iter(self)) == next(iter(other))
            last_element_boolean = next(reversed(self)) == next(reversed(other))
            steps_boolean = self.step == other.step

            return first_element_boolean and last_element_boolean and steps_boolean
        else:
            # we delegate comparison to another object
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