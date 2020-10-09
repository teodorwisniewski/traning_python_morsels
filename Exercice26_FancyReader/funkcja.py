import typing


def funkcja(tekst):
    """

    :return:
    """
    return not tekst[0] == tekst[0].upper()

s = "teksts"
s2 = "Tekst"
s3 = "?tekst"
s4 = "?"

print(funkcja(s))
print(funkcja(s2))
print(funkcja(s3))
print(funkcja(s4))

a = 5
b = 7
b,a = a,b
