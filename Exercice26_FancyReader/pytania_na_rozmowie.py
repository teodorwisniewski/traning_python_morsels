
t = ["a"]
tab = list(t)
tab *= 5
print(tab)
tab[0] = tab[0]*5
print(tab)
t2 = list(t)*5
t2[0] = list(t2[0])*2
print(t2)
a = ["greg"]


def fun1():
    b = a*2
    print(b)


def fun2():
    global a
    a *=2
    print(a)

fun1()
fun2()