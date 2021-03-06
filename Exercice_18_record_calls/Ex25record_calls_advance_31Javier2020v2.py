

class record_calls(object):

    def __init__(self,initial_function):

        self.initial_function = initial_function
        self.call_count = 0

    def __call__(self,*args,**kwargs):
        print("To jest przed wywolaniem orginalnej classy")
        self.call_count +=1
        try:
            return self.initial_function(*args,**kwargs)
        except Exception:
            self.initial_function("world")
            
@record_calls
def greet(name):
    """Greet someone by their name."""
    print(f"Hello {name}")




if __name__=="__main__":
    greet("Joghnn")

    greet("Trey")

    print(greet.call_count)
# 1
    greet()
# Hello world
    print(greet.call_count)
# 2

    greet("Trey")
# Hello Trey
    print(greet.calls[0].args)
# ('Trey',)
    print(greet.calls[0].kwargs)
# {}
    greet(name="Trey")
# Hello Trey
    print(greet.calls[1].args)
# ()
    print(greet.calls[1].kwargs)
# {'name': 'Trey'}
