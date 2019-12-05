from collections import defaultdict, Counter
import string

# I want you to write a function that accepts a string and r
# eturns a mapping (a dictionary or dictionary-like structure) 
# that has words as the keys and the number of times each word was seen as the values.

def count_words(wejscie):
    exclude_punc = set(string.punctuation)
    exclude_punc.add("¿")
    exclude_punc.discard("'") 
    wejscie = "".join(ch for ch in wejscie if ch not in exclude_punc)
    wyjscie = defaultdict(int)
    for slowo in wejscie.lower().split():  wyjscie[slowo] +=1
    return wyjscie

# def count_words(wejscie):

#     return Counter(wejscie.lower().split())





wejscie = "?oh what a day what a lovely day?"
wyjscie = count_words(wejscie)
print(wyjscie)
print(count_words("don't stop believing"))
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
# >>> count_words("don't stop believing")
# {"don't": 1, 'stop': 1, 'believing': 1}