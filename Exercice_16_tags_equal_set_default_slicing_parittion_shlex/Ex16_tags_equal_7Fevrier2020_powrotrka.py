
import shlex

def parse_attributes(attribute_tag):
    key,_,value = attribute_tag.partition("=")
    return key, value


def parse_html(html_tag):
    if len(html_tag.split())>1:
        name, attributes_str = html_tag[1:-1].casefold().split(maxsplit=1)  
        attributes = {}
        for a in shlex.split(attributes_str):
            key,value = parse_attributes(a)
            attributes.setdefault(key,value)
    else:
        name, attributes = [html_tag[1:-1].casefold(), None]
    
    return name, attributes



def tags_equal(str1,str2):
    """returns boolean of comparison of equality between two html tags """
    return parse_html(str1) == parse_html(str2)


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