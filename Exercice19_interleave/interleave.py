


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


def interleave(*iters):

    out = []
    for elements in zip(*iters):
        for el in elements: yield el



# def interleave(iter1,iter2):

#     out = []
#     for el1,el2 in zip(iter1,iter2):
#         out.extend([el1,el2])

#     return out



if __name__ == "__main__":

    numbers = [1, 2, 3, 4]
    print(list(interleave(numbers, range(5, 9))))
#[1, 5, 2, 6, 3, 7, 4, 8]
    print(list(interleave(numbers, (n**2 for n in numbers))))
# [1, 1, 2, 4, 3, 9, 4, 16]


print(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[1, 4, 7, 2, 5, 8, 3, 6, 9]