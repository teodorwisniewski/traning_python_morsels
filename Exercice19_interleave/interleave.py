

from itertools import zip_longest, chain
# class interleave:

#     """Iterator that counts upward forever."""

#     def __init__(self, iter1,iter2):
#         self.iter1 = iter1
#         self.iter2 = iter2

#     def __iter__(self):
#         return self

#     def __next__(self):
#         num = self.num
#         self.num += 1
#         return num




    # out = []
    # val_to_skip = object()
    # for elements in zip_longest(*iters,fillvalue=val_to_skip):
    #     for el in elements: 
    #         if el is not val_to_skip: 
    #             yield el
# def interleave(*iters):
#     sentinel = object()
#     zipped = zip_longest(*iters,fillvalue=sentinel)
#     flattened = chain.from_iterable(zipped)
#     return (x for x in flattened if x is not sentinel)

def interleave(*iterables):
    sentinel = object()
    for elements in zip_longest(*iterables,fillvalue=sentinel):
        for el in elements:
            if el is not sentinel:
                yield el




if __name__ == "__main__":

    numbers = [1, 2, 3, 4]
    for el in interleave(numbers, range(5, 9)):
        print(el)
#[1, 5, 2, 6, 3, 7, 4, 8]
    print(list(interleave(numbers, (n**2 for n in numbers))))
# [1, 1, 2, 4, 3, 9, 4, 16]


    print(list(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9])))
    # [1, 4, 7, 2, 5, 8, 3, 6, 9]

    print(list(interleave([1, 2, 3], [4, 5, 6, 7, 8])))
    # [1, 4, 2, 5, 3, 6, 7, 8]

    print(list(interleave([1, 2, 3], [4, 5], [6, 7, 8, 9])))
    # [1, 4, 6, 2, 5, 7, 3, 8, 9]

    in1 = [1, 2, 3, None]
    in2 = [4, 5, 6, 7]
     
    print(list(interleave(in1,in2)))
    #[1, 4, 2, 5, 3, 6, None, 7]