


# def compact(lista):

#     out = []
#     last_index = 0
#     if len(lista)>0:
#         out.append(lista[last_index])
#     for i in range(1,len(lista)):
#         if out[last_index] != lista[i]:
#             out.append(lista[i])
#             last_index +=1
#     return out

def compact(lista):

    out = []
    last_index = 0
        
    for el in lista:
        if last_index==0:
            out.append(el)
            last_index +=1     
        if out[last_index-1] != el:
            out.append(el)
            last_index +=1
    
    return iter(out)



lis1 = [1, 1, 2, 2, 3, 5,5,5,2]

print(compact(lis1))

print(compact([]))

print(compact([1, 1, 1]))