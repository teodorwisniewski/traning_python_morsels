from functools import wraps
from dataclasses import dataclass
from typing import Any, Optional

NO_RETURN = object()

@dataclass
class Call:
    args: tuple
    kwargs: dict
    return_value: Any = NO_RETURN
    exception: Optional[BaseException] = None
    



def record_calls(funkja):

    @wraps(funkja)
    def inner_wraps(*args,**kwargs):
        inner_wraps.call_count += 1
        call = Call(args,kwargs)
        inner_wraps.calls.append(call)
        try:
            call.return_value = funkja(*args,**kwargs)
        except Exception as e:
            call.exception  = e
            raise
        return call.return_value   
    inner_wraps.call_count = 0
    inner_wraps.calls = []
    return inner_wraps


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