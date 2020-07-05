from itertools import islice, tee
from collections import deque
# def window(numbers,okno):

#     numbers,numbers_kopia = tee(numbers,2)
#     numbers_kopia = list(numbers_kopia)
#     indice =0
#     if okno>=1:
#         for _ in numbers:
#             out = tuple(numbers_kopia[indice:indice+okno])
#             indice += 1
#             # print(cos)
#             if len(out) == okno:
#                 yield out
#     else:
#         return

def window(numbers,okno, *,fillvalue=None):
    out = deque(maxlen=okno) # przy dodawniu wujebie pierwszy i doda na koncu
    for item in numbers:
        out.append(item)
        if okno and len(out) == okno:
            yield tuple(out)
    while len(out)<okno:
        out.append(fillvalue)
        if okno and len(out) == okno:
            yield tuple(out)
        



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
    # self.assertIterableEqual(window([], 1), [(None,)])
    #     self.assertIterableEqual(window([1, 2], 3), [(1, 2, None,)])
    #     self.assertIterableEqual(window([1, 2, 3], 4), [(1, 2, 3, None)])

    # # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    # def test_fillvalue_as_keyword_argument_only(self):
    #     """Test can be called with fillvalue (but only as keyword arg)."""
    #     inputs = [1, 2, 3]
    #     outputs = [(1, 2, 3, 0)]
    #     self.assertIterableEqual(window(inputs, 4, fillvalue=0), outputs)
    #     with self.assertRaises(TypeError):
    #         window(inputs, 4, 0)