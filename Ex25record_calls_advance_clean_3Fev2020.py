from collections import namedtuple
from pprint import pprint


def record_calls(funkcja):
    
    def obudowa(*args, **kwargs):
        obudowa.call_count += 1
        
        if len(args) or len(kwargs):
            cos = funkcja(*args, **kwargs)
            obudowa.calls.append(obudowa.Argumenciki(args,kwargs,cos,"None"))
            return cos
        else:
            cos = funkcja("world") 
            obudowa.calls.append(obudowa.Argumenciki(args,kwargs,cos,"None"))
            return cos     
    obudowa.__name__ = funkcja.__name__
    obudowa.__qualname__ = funkcja.__qualname__
    obudowa.__doc__ = funkcja.__doc__
    obudowa.__annotations__ = funkcja.__annotations__
    obudowa.call_count = 0
    obudowa.calls = []
    obudowa.Argumenciki = namedtuple('Argumenciki', 'args kwargs return_value exception')
    return obudowa




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
