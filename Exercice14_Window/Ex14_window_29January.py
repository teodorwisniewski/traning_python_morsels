from itertools import islice, tee
from collections import deque


class window:

    def __init__(self, numbers, okno, fillvalue=None):

        self.numbers = iter(numbers) if isinstance(numbers,(list,str)) else numbers 
        self.okno = okno
        self.flag = 0
        self.fillvalue = fillvalue
        if okno:
            self.okno_out = deque(maxlen=self.okno)
        else:
            self.okno_out = 0


    def __iter__(self):
        return self

    def __next__(self):

        if self.okno_out==0:
            raise StopIteration

        if len(self.okno_out)==self.okno and self.flag==0:
            self.okno_out.append(next(self.numbers))
            return tuple(self.okno_out)

        if self.flag==0:
            while len(self.okno_out)<self.okno:
                try:
                    self.okno_out.append(next(self.numbers))
                except:
                    self.okno_out.append(self.fillvalue)    
            out = tuple(self.okno_out)      
            if self.fillvalue in out:
                self.flag = 1   
            return out              
        else:
            raise StopIteration
                    

if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5, 6]

    for i in window(numbers, 2):
        print(i)
    for i in window(numbers, 0):
        print(i)
    for i in window(numbers, 1):
        print(i)
    print(list(window([1, 2, 3], 0)) ==[])
    print(list(window([], 0)) == [])
    # print(list(window(numbers, 0)))
    # print(list(window(numbers, 1)))
    # print(list(window(numbers, 2)))
    # [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    print(list(window(numbers, 3)))
    # [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
    squares = (n**2 for n in numbers)
    for i in window(squares, 4):
        print(i)
    # [(1, 4, 9, 16), (4, 9, 16, 25), (9, 16, 25, 36)]
    tekscik = "Teodoro"
    for i in window(tekscik, 3):
        print(i)

    #Bonus 1    
    numbers = [1, 2, 3, 4, 5, 6]
    # print(next(window(numbers, 3)))
    inputs = (n**2 for n in [1, 2, 3, 4, 5])
    iterable = window(inputs, 2) #(1, 4)
    print(next(iterable))
    print(next(iterable))
    print(next(inputs)) # 9

    for i in list(window([1, 2, 3], 6)):
        print(i)

    for i in window([1, 2, 3], 5, fillvalue=0):
        print(i)