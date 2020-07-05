from contextlib import contextmanager

@contextmanager
def suppress(*errors):
    exception, traceback = (None, None)
    try:
        yield
    except errors as e:
        exception = e 
        traceback = "costam"
    # return exception, traceback
    return suppress



if __name__ == "__main__":
    with suppress(NameError):
        print("Hi!")
        print("It's nice to meet you,", name)
        print("Goodbye!")

    # with suppress(TypeError):
    #     print("Hi!")
    #     print("It's nice to meet you,", name)
    #     print("Goodbye!")
    x = 0
    with suppress(ValueError, TypeError) as context:
        x = int('hello')
    print(x)
    print(context)