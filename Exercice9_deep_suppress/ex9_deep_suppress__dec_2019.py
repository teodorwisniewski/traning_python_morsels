from contextlib import contextmanager


# class ExceptionInfo:
#     exception = None
#     traceback = None


# @contextmanager
# def suppress(*errors):
#     info = ExceptionInfo()
#     try:
#         yield info
#     except errors as e:
#         info.exception = e
#         info.traceback = e.__traceback__

class suppress:

    def __init__(self, *wyjatki):
        
        self.wyjatki = wyjatki
        self.exception = None
        self.traceback = None

    def __call__(self,)

    def __enter__(self):

        return self

    def __exit__(self, exception_type, exception, traceback): 
        self.exception = exception
        self.traceback = traceback        

        return isinstance(exception, self.wyjatki)




if __name__ == "__main__":
    with suppress(NameError):
        print("Hi!")
        print("It's nice to meet you,", name)
        print("Goodbye!")

    x = 0
    with suppress(ValueError, TypeError) as context:
        x = int('hello')
    print(x)
    print(context.exception)
    print(context.traceback)

    @suppress(TypeError)
    def len_or_none(thing):
        return len(thing)