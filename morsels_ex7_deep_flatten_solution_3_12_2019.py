from pprint import pprint
from collections.abc import Iterable

def deep_flatten(liste_list):
    for el in liste_list: 
        if isinstance(el, Iterable) and type(el) != str:
            yield from deep_flatten(el)
        else:
            yield el




if __name__ == "__main__":
    ins = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
    pprint(list(deep_flatten(ins)))
    pprint(list(deep_flatten([[1, [2, 3]], 4, 5])))
    numbers_and_words = enumerate(['lime', 'pear', 'jujube'])
    flattened = deep_flatten(numbers_and_words)
    pprint(next(flattened))
    pprint(next(flattened))
    pprint(next(numbers_and_words))
    

    lista = []
    print(lista[0])