
class record_calls:

    def __init__(self,funkcja):
        self.funkcja = funkcja
        self.call_count = 0

    def __call__(self,*args):
        self.call_count += 1
        print("przed wywolaniem fukcji")
        try:
            return self.funkcja(args[0])
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

