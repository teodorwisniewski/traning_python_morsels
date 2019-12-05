# Assigned 


# For example:

# >>> compact([1, 1, 1])
# [1]
# >>> compact([1, 1, 2, 2, 3, 2])
# [1, 2, 3, 2]
# >>> compact([])
# []




def compact(sequence):
    out = []
    sequence = list(sequence)
    for i, el in enumerate(sequence):
        if i == 0 or sequence[i-1] != el:
            yield el



print(list(compact([1, 1, 1])))
print(list(compact([1, 1, 2, 2, 3, 2])))
print(list(compact([])))

