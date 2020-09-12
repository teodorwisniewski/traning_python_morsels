
from math import sqrt
import cmath
from decimal import Decimal

def is_perfect_square(number,*,complex=False):

    if complex:
        complex_number = cmath.sqrt(number)
        return complex_number.real.is_integer() and complex_number.imag.is_integer()
    if number<0: return False    
    return int(Decimal(number).sqrt())**2 == number




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
