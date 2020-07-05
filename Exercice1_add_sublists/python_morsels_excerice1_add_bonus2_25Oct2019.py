
def add(*argv):
    out = [[0.0]*len(argv[0][0])]*len(argv[0])
    for i_listinlist in argv: # ilist = [[][]]
        if not len(i_listinlist) == len(argv[0]):
            raise ValueError("Given matrices are not the same size.")
        for indice_sublist,sub_list in enumerate(i_listinlist): #sub_out= [0 , 0]
            if not len(sub_list) == len(argv[0][0]):
                raise ValueError("Given matrices are not the same size.")
            out[indice_sublist]= [el  + sub_list[indice_el] for indice_el,el in enumerate(out[indice_sublist])]
                
    return out


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
matrix3 = [[-3, 3], [3, -3]]
matrix4 = [[5, 5], [10,3]]
results = add(matrix1,matrix2,matrix3,matrix4)

print(results)