import shlex

def parse_html(html_tag):

    if len(html_tag.split())==1:
        name = html_tag.lower()[1:-1]
        attributes_dict = None
    else:
        name,attributes_str = html_tag.lower()[1:-1].split(maxsplit=1)
        attributes = shlex.split(attributes_str)
        attributes_dict = {}
        for a in attributes:
            cle,_, valeur = a.partition("=")
            attributes_dict.setdefault(cle,valeur)
    

    return name, attributes_dict




def tags_equal(str1,str2):
    
    return  parse_html(str1) == parse_html(str2)










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
# True
    print(tags_equal("<input value='hello there'>", '<input value="hello there">'))
# True
    print(tags_equal("<input value=hello>", "<input value='hello'>"))
# True
    print(tags_equal("<input value='hi friend'>", "<input value='hi there'>"))
# False