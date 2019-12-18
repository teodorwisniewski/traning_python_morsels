

class suppress(object):

    def __init__(self,*errors):
        self.errors = errors
        self.exception = None
        self.traceback = None


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback):
        if not exc_type in self.errors:
            pass
        elif exc_type:
            self.exception = exc_type
            self.traceback = exc_traceback
            return self
        else:
            return self
        
        
        
        

if __name__ == "__main__":
    with suppress(NameError) as cos:
        print("Hi!")
        print("It's nice to meet you,", name)
        print("Goodbye!")
    print(cos)
    with suppress(TypeError):
        print("Hi!")
        print("It's nice to meet you,", name)
        print("Goodbye!")
    x = 0
    with suppress(ValueError, TypeError) as context:
        x = int('hello')
    print(x)


    print(context)