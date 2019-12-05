

def compact(lista):

    out = []
    last_index = 0
    for el in lista:
        if last_index == 0:
            out.append(el)
            last_index +=1
        if out[last_index-1] != el:
            out.append(el)
            last_index += 1
    return out








print(compact([1, 1, 1]))
print(compact([1, 1, 2, 2, 3, 2]))
print(compact([]))