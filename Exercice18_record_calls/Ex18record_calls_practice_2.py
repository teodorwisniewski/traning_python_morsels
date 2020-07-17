from functools import wraps
from dataclasses import dataclass
from typing import Tuple, Dict

@dataclass
class Call:
    args: Tuple
    kwargs: Dict



def record_calls(fun):
    @wraps(fun)
    def inner_wrapper(*args,**kwargs):
        inner_wrapper.call_count += 1
        inner_wrapper.calls.append(Call(args,kwargs))
        return fun(*args,**kwargs)
    inner_wrapper.call_count = 0
    inner_wrapper.calls = []

    return inner_wrapper




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
    print(greet.calls[1].args)
    print(greet.calls[1].kwargs)