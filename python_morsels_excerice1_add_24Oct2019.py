
def add(*listy):
    return [
            [
            sum(elements)
            for elements in zip(*sublisty)
            ] 
        for sublisty in zip(*listy)]


matrix1 = [[9, 1], [5, 6]]
matrix2 = [[1, 9], [7, 3]]
matrix3 = [[1, 1], [1, 1]]

results = add(matrix1,matrix2,matrix3,matrix3,matrix3)

print(results)