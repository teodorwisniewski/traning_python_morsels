from contextlib import contextmanager

@contextmanager
def suppress(*errors):
    exception, traceback = (None, None)
    try:
        yield
    except errors as e:
        exception = e 
        traceback = "costam"
    return exception, traceback

# class suppress(object):

#     def __init__(self,*errors):
#         self.errors = errors
#         self.exception = None
#         self.traceback = None


#     def __enter__(self):
#         return self.test_number

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         if exc_value == None:
#             print 'Test %d passed' % self.test_number
#         else:
#             print 'Test %d failed: %s' % (self.test_number, exc_value)
#         return Tru



if __name__ == "__main__":
    with suppress(NameError):
        print("Hi!")
        print("It's nice to meet you,", name)
        print("Goodbye!")

    # with suppress(TypeError):
    #     print("Hi!")
    #     print("It's nice to meet you,", name)
    #     print("Goodbye!")

    with suppress(ValueError, TypeError) as context:
        x = int('hello')

    print(context)