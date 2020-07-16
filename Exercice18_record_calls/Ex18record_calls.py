from functools import wraps


def record_calls(funkcja):
    @wraps(funkcja)
    def inner_wrapper(*args, **kwargs):
        inner_wrapper.call_count +=1
        return funkcja(*args, **kwargs)
    inner_wrapper.call_count = 0
    return inner_wrapper

# class record_calls:

#     def __init__(self,funkcja):
#         self.call_count = 0
#         self.fukcja = funkcja

    
#     def __call__(self,*args,**kwargs):
#         self.call_count += 1
#         print(self.fukcja.__name__ + " was called")
#         return self.fukcja(*args,**kwargs)


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

greet("Trey")
greet2("Trey")
greet2("Trey3")
greet2("Trey4")
print(greet.call_count)
greet()
print(greet.call_count)
print(greet2.call_count)
print(help(greet))
print(greet.__name__)

print(help(greet2))