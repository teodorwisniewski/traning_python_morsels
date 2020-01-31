
class record_calls(object):

    def __init__(self,initial_function):

        self.initial_function = initial_function
        self.call_count = 0

    def __call__(self,*args,**kwargs):
        print("To jest przed wywolaniem orginalnej classy")
        return self.initial_function(*args,**kwargs)

@record_calls
def greet(name):
    """Greet someone by their name."""
    print(f"Hello {name}")

def arg_dec(html_sign):
    def p_decorate(funkja):
        def funkcja_wrapper(self):
            return html_sign + funkja(self).casefold() + html_sign.replace("<","</")
        return funkcja_wrapper
    return p_decorate

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @arg_dec("<p>")
    def get_fullname(self):
        return self.name+" "+self.family



if __name__=="__main__":
    greet("Joghnn")
    my_person = Person()
    print(my_person.get_fullname())
    greet("Trey")

    print(greet.call_count)
# 1
    greet("world")
# Hello world
    print(greet.call_count)
# 2

