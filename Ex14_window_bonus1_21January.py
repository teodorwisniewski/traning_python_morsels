from itertools import tee


def window(numbers, calkowita):
    a = []
    if calkowita == 0 : return
    else:
        if not isinstance(numbers,list): 
            numbers, numbers2_it = tee(numbers)
            numbers2_it = list(numbers2_it)
        else:
            numbers2_it = numbers
            numbers = iter(numbers)
        licznik = 0 
        for i,el in enumerate(numbers2_it):
            if licznik == (len(numbers2_it)-calkowita+1):
                break
            element = tuple(numbers2_it[i:i+calkowita])
            print(next(numbers))
            yield element
            licznik +=1
            








if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5, 6]
    print(list(window(numbers, 0)))
    print(list(window(numbers, 1)))
    print(list(window(numbers, 2)))
    # [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    print(list(window(numbers, 3)))
    # [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
    squares = (n**2 for n in numbers)
    print(list(window(squares, 4)))
    # [(1, 4, 9, 16), (4, 9, 16, 25), (9, 16, 25, 36)]
    tekscik = "Teodoro"
    print(list(window(tekscik, 3)))

    some_stuff = window(numbers, 3)
    print(next(some_stuff))
    inputs = (n**2 for n in [1, 2, 3, 4, 5])
    iterable = window(inputs, 2) #(1, 4)
    print(next(iterable))
    print(next(inputs)) # 9