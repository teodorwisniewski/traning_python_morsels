

class FuzzyString:

    def __init__(self,tekst):

        self.tekst = tekst
    
    def __repr__(self):
        return repr(self.tekst)

    def __str__(self):
        return self.tekst   

    def __lt__(self,other):
        return str(self).lower() < other.lower()

    def __le__(self,other):
        return str(self).lower() <= other.lower()

    def __eq__(self,other):
        return str(self).lower() == other.lower()

    def __ne__(self,other):
        return str(self).lower() != other.lower()

    def __gt__(self,other):
        return str(self).lower() > other.lower()  

    def __ge__(self,other):
        return str(self).lower() >= other.lower()    

    def __contains__(self, substring):
        if substring.lower() in self.tekst.lower():
            return True
        else:
            return False

    def __add__(self, other):
        self.tekst += other.lower()
        return self


if __name__ == "__main__":

    greeting = FuzzyString('Hey TREY!')
    print(greeting == 'hey Trey!')
# True
    print(greeting == 'heyTrey')
# False
    print(greeting)
# 'Hey TREY!'
    repr(greeting)
    str(greeting)

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