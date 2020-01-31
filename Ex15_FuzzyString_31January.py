from functools import total_ordering
import unicodedata

def _normalized(tekscik):
    return unicodedata.normalize("NFD", tekscik.casefold())

@total_ordering
class FuzzyString:

    def __init__(self,tekst):
        self.tekst = tekst
    
    def __eq__(self,other):
        return _normalized(self.tekst) == _normalized(other)

    def __lt__(self,other):
        return _normalized(self.tekst) < _normalized(other)        

    def __str__(self):
        return self.tekst
    
    def __repr__(self):
        return repr(self.tekst)

    def __add__(self,other):
        return FuzzyString(self.tekst+other)

    def __contains__(self,substr):
        return _normalized(substr) in _normalized(self.tekst)

if __name__ == "__main__":

    greeting = FuzzyString('Hey TREY!')
    print(greeting == 'hey Trey!')
# True
    print(greeting == 'heyTrey')
# False
    print(greeting)
# 'Hey TREY!'
    print(repr(greeting))
    print(str(greeting))

    apple = FuzzyString("Apple")
    print(apple>"animal")
    print("animal"< apple)
    print(apple < "animal")
    print("animal" > apple)
    print(apple<= "animal")
    print(apple>= "apple")
    # print("animal", apple)
    # print("animal", "animal")
    print(apple <= "animal")
    print("animal" >= apple)
    print(apple != "hello!")

    hello = FuzzyString("heLlO")
    print(str(hello) == "heLlO")
    print(repr(hello) == repr("heLlO"))

    o_word = FuzzyString('Octothorpe')
    print('OCTO' in o_word)
    new_string = o_word + ' (aka hashtag)'
    print(new_string == 'octothorpe (AKA hashtag)')

    ss = FuzzyString('ss')
    print('\u00df' == ss)
# True
    e = FuzzyString('\u00e9')
    print('\u0065\u0301' == e)
# True
    print('\u0301' in e)
# True