from pprint import pprint
from collections import Counter
import re



# def _parse_tag(html_tag):
#     """Return tuple of tag name and attrivutes """
#     name, *attributes = html_tag.casefold()[1:-1].split()
#     attributes_dict = dict(el.split("=") if len(el.split("="))>1 else [el,None]  for el in reversed(attributes))
#     return name, attributes_dict
def _parse_tag(html_tag):
#     """Return tuple of tag name and attrivutes """
    name, *attributes = html_tag.casefold()[1:-1].split()
    attributes_dict = {}
    for a in attributes:
        key, value = tuple(a.split("=")) if len(a.split("="))>1 else (a,None)
        attributes_dict.setdefault(key,value)

    return name, attributes_dict

def tags_equal(str_1,str_2):
    """Return True if the given html open tags represent the same thing """
    return _parse_tag(str_1) == _parse_tag(str_2)




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

    # bonus 1
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
    print(tags_equal("<input value='hello there'>", '<input value="hello there">'))
# True
    print(tags_equal("<input value=hello>", "<input value='hello'>"))
# True
    print(tags_equal("<input value='hi friend'>", "<input value='hi there'>"))
# False