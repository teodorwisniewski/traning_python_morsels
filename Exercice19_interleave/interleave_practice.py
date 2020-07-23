from itertools import zip_longest, chain


def interleave(*iterables):
    sentinel = object()
    zipped_ters = zip_longest(*iterables,fillvalue=sentinel)
    flattened = chain.from_iterable(zipped_ters)
    for el in flattened:
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