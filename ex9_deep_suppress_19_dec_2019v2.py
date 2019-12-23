

class suppress:

    def __init__(self, *exception_to_deal_with):
        self.exception_to_deal_with =exception_to_deal_with

    def __enter__(self):
        pass

    
    def __exit__(self, exception_type, exception, traceback):
        if isinstance(exception, self.exception_to_deal_with):
            return True
        else:
            return False





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