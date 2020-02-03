from collections import namedtuple

class record_calls:

    def __init__(self,funkcja):
        self.funkcja = funkcja
        self.calls = []
        self.Argumenciki = namedtuple('Argumenciki', 'args kwargs')

    
    @property
    def call_count(self):
        return len(self.calls)

    def __call__(self,*args,**kwargs):
        if len(kwargs) == 0:
            kwargs = {}
        if len(args) == 0:
            args = ()
        
        self.calls.append(self.Argumenciki(args,kwargs))
        print("przed wywolaniem fukcji")
        try:
            return self.funkcja(*args,**kwargs)
        except Exception:
            return self.funkcja("world")
      

    




@record_calls
def greet(name):
    """Greet someone by their name."""
    print(f"Hello {name}")


if __name__=="__main__":
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
    print(greet.calls[greet.call_count-1].kwargs)
# {'name': 'Trey'}
