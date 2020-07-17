from functools import wraps, update_wrapper
import wrapt
from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass

@dataclass
class Call():
    args: tuple
    kwargs: dict

def record_calls(fun):

    @wraps(fun)
    def inner_wrapper(*args,**kwargs):
        inner_wrapper.call_count += 1
        inner_wrapper.calls.append(Call(args, kwargs))
        return fun(*args,**kwargs)

    inner_wrapper.call_count = 0
    inner_wrapper.calls = []

    return inner_wrapper


# class record_calls(wrapt.ObjectProxy):

#     def __init__(self,fun):
#         super().__init__(fun)
#         self.call_count = 0
#         self.Call = namedtuple('Call', 'args kwargs')
#         self.calls = []

#     def __call__(self,*args,**kwargs):
#         self.call_count += 1
#         self.calls.append(self.Call(args=args, kwargs=kwargs))
#         return self.__wrapped__(*args,**kwargs)       

@record_calls
def greet(name="world"):
    """ 
        docstring of greet
    """
    """Greet someone by their name."""
    print(f"Hello {name}")


@record_calls
def greet2(name="world"):
    """ 
        docstring of greet2
    """
    """Greet someone by their name."""
    print(f"LS503 {name}")

@record_calls
def cube(n):
    return n**3

if __name__ == "__main__":


    greet("Trey")
    greet2("Trey")
    greet2("Trey3")
    greet2("Trey4")
    greet(name="Trey")
    print(greet.call_count)
    greet()
    print(greet.call_count)
    print(greet2.call_count)
    print(help(greet))
    print(greet.__name__)

    print(help(greet2))

    print(greet.calls[0].args)
    print(greet.calls[0].kwargs)
    print(greet.calls[1].args)
    print(greet.calls[1].kwargs)

    cube(3)
    cube(5)
    print(cube.calls)
    cube(None)
    print(cube.calls[-1])