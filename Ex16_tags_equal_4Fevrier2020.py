from pprint import pprint
import re

def tags_equal(str_1,str_2):

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