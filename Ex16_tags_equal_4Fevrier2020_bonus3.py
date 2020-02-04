from pprint import pprint
from collections import Counter

def _cleaning_duplicates(aux_str: list):
    out = []
    lista_attributes = [el.split("=")[0] for el in aux_str ]
    d = dict.fromkeys(lista_attributes, True)
    for el in lista_attributes:
        if d[el]:
            for el2 in aux_str:
                if  el in el2:
                    out.append(el2)
                    d[el] = False
                    break
    return " ".join(out)
    


    



def tags_equal(str_1,str_2):
    str_1 = _cleaning_duplicates(str_1.casefold().split())
    str_2 = _cleaning_duplicates(str_2.casefold().split())

    if len(str_1.split())>=len(str_2.split()):
        zbior = str_1[1:-1].casefold().split() 
        z2 = str_2[1:-1].casefold()
    else:
        str_1,str_2 = str_2,str_1
        zbior = str_1[1:-1].casefold().split() 
        z2 = str_2[1:-1].casefold() 

    out_bool = []
    for el in zbior:
        out_bool.append(el in z2)
    return all(out_bool)







if __name__=='__main__':
    print(tags_equal("<img src=cats.jpg height=40>", "<IMG SRC=Cats.JPG height=40>"))
# True
    print(tags_equal("<img src=dogs.jpg width=99>", "<img src=dogs.jpg width=20>"))
# False
    print(tags_equal("<p>", "<P>"))
# True
    print(tags_equal("<b>", "<p>"))
# False
    print(tags_equal('<IMG height=200 width=400>','<img Width=400 Height=200>'))
# True
    print(tags_equal('<img height=400 WIDTH=200>','<Img width=400 HEIGHT=200>'))
# False
    print(tags_equal("<OPTION NAME=Hawaii SELECTED>", "<option selected name=hawaii>"))
# True
    print(tags_equal("<option name=hawaii>", "<option name=hawaii selected>"))
# False
    print(tags_equal(
        '<input type=hidden type=input>',
        '<input type=hidden>',
    ))
# True
    print(tags_equal(
        '<img type=input type=hidden>',
        '<Img type=hidden>',
    ))
# False
    print(tags_equal(
        '<input TYPE=hidden type=input>',
        '<input type=hidden>',
    ))
# True