
class float_range:

    def __init__(self,*args):

        if len(args) == 3:
            (self.start, self.stop,self.step) = args
    
    def __iter__(self):
        return self

    def __next__(self):
        num = self.start
        if num<self.stop:
            self.start += +self.step 
            return num
        else:
            raise StopIteration
            


    




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