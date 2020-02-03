from collections import namedtuple
from pprint import pprint

class record_calls:

    def __init__(self,funkcja):
        self.funkcja = funkcja
        self.calls = []
        self.Argumenciki = namedtuple('Argumenciki', 'args kwargs return_value exception')

    
    @property
    def call_count(self):
        return len(self.calls)

    def __call__(self,*args,**kwargs):
        if len(kwargs) == 0:
            kwargs = {}
        if len(args) == 0:
            args = ()
        
        
        print("przed wywolaniem fukcji")
        try:
            cos = self.funkcja(*args,**kwargs)
        except Exception as ex:
            cos = self.funkcja("world")
        try:
            ex
        except:
            ex = None
        self.calls.append(self.Argumenciki(args,kwargs,cos,ex))
        return cos
      

@record_calls
def cube(n):
    return n**3
  




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
    pprint(cube(3))

    print(cube.calls)
