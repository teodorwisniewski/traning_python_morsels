# 27 octobre 2019 powtorka
#Python's built-in zip function stops at the shortest list when zipping.

# Blog part 1
def add_sublists(*lists):

    output = []
    for lists_of_lists in lists:
        podlista = []
        for sublist in lists_of_lists:
            podlista.append(sum(sublist))
        output.append(podlista)

    return output 

def add_sublists(*lists):

    output = [
        [
            sum(sublist)
            for sublist in lists_of_lists
        ]
        for lists_of_lists in lists
    ]    
        
    return output
    


# Blog part 2

list1 = [[5, -1], [1, 2, 30,67]]
list2 = [[2, -2], [1, -2], [5.5]]
list3 = [[50, 50], [33.33333333333, 66.67]]

print(add_sublists(list1,list2))

from itertools import zip_longest
def add(*lists):
    # set_lists_sizes = {
    #     tuple(len(r) for r in list_of_lists) # it has to be a tuple, because a set does not accept hashable
    #     for list_of_lists in lists 
    # }
    # print(set_lists_sizes)
    # if len(set_lists_sizes)>1:
    #     raise ValueError("Ej co jest kurlaaa to nie sa tego samego rozmiaru macierze macierzys")
    try:
        return [
            [
                sum(elements)
                for elements in zip_longest(*sublists)
            ]
            for sublists in zip_longest(*lists)
        ]
    except TypeError as e:
        print(e)
        print("Ej, ej te macierze nie sa tego samego rozmiaru")

#######################
def get_shape(lista_lists):
    return [len(r) for r in lista_lists]
def add(*lists):
    shape_list_0 = [len(l) for l in lists[0]]
    if any(shape_list_0 != get_shape(sublist) for sublist in lists):
        raise ValueError("Ej ziomek, cos z tymi rozmiarami macierzy sie nie zgadza")

    return [
            [
                sum(elements)
                for elements in zip_longest(*sublists)
            ]
            for sublists in zip_longest(*lists)
        ]


matrix1 = [[1, -2], [-3, 4,3]]
matrix2 = [[2, -1], [0, -1,3]]

print(add(matrix1,matrix2))


#########################################""""


def multliply(*lists):
    out = []
    for sublists in zip(*lists):
        row =[]
        for elements in zip(*sublists):
            product = 1
            for el in elements: product = product*el
            row.append(product)
        out.append(row)

    return out

def multliply(*lists):
    out = []
    for sublists in zip_longest(*lists, fillvalue=[]):
        row =[]
        for elements in zip_longest(*sublists,fillvalue=0):
            product = 1
            for el in elements: product = product*el
            row.append(product)
        out.append(row)

    return out
   


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

print(multliply(matrix1,matrix2))