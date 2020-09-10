from math import sqrt
from numbers import Number

def is_perfect_square(number,complex=False):
    try:
        number = float(number)
    except:
        try:
            abs(number)
        except:
            raise TypeError("It has to be a number.")


    if not isinstance(number,(int,float,Number)):
        raise TypeError("It has to be a number.")
    if complex:
        squared_number = round(abs(number)**0.5,1)
        if abs(squared_number*squared_number) == abs(number): return True
    else:
        if number<0: return False
        squared_number = round(sqrt(number),1)
        if squared_number*squared_number == number: return True

    return False
        



if __name__ == "__main__":

    print(is_perfect_square(64))
    print(is_perfect_square(65))
    print(is_perfect_square(100))
    print(is_perfect_square(1000))
    print(is_perfect_square(33))

# The first bonus is to make sure your function returns False for negative numbers. ✔️

    print(is_perfect_square(-1))
    print(is_perfect_square(-4))

#The second bonus is to make sure your function works for really big numbers. ✔️

    print(is_perfect_square(4624000000000000))
# True
    print(is_perfect_square(4623999999999999))
#False

    print(is_perfect_square(-4, complex=True))
 #   True
    print(is_perfect_square(-5, complex=False))
 #   False
    print(is_perfect_square(512j, complex=True))
#True
