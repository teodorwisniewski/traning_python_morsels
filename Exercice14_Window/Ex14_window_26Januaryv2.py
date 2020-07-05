from itertools import tee, islice

class window:

    def __init__(self,lista,number):

        # self.lista = iter(lista) if isinstance(lista, list) else lista
        self.lista = lista
        self.lista, self.copy_lista  = tee(self.lista,2)
        self.copy_lista = list(self.copy_lista)
        self.wielkosc = len(self.copy_lista)
        # self.last = self.copy_lista[-1]
        self.number = number
        self.first_el = 0
        if self.wielkosc:
            self.last_el = next(self.lista)

    def __iter__(self):
        return self

    def __next__(self):
        if self.number and self.first_el<len(self):
            out = tuple(islice(self.copy_lista,self.first_el,self.first_el+self.number))
            if len(out) <self.number:
                raise StopIteration()    
            self.first_el +=1
            return out
        # elif self.number and self.first_el<=len(self)+1 and self.number==1:
        #     out = (self.last_el,)
        #     self.last_el = next(self.lista) if self.first_el<=len(self) else None
        #     if self.first_el == len(self): 
        #         raise StopIteration()
        #     self.first_el +=1
        #     return out
        elif self.number==0 and self.first_el<1:
            raise StopIteration()
        else:
            raise StopIteration()  
            

    def __len__(self):
        return self.wielkosc-self.number+1











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
  
    print(next(window(numbers, 3)))
    inputs = (n**2 for n in [1, 2, 3, 4, 5])
    iterable = window(inputs, 2) #(1, 4)
    print(next(iterable))
    print(next(iterable))
    print(next(inputs)) # 9