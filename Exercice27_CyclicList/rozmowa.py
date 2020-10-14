

zmienna = 5

def first_fun():
    a = zmienna +3
    print(zmienna)

def second_func():
    global zmienna
    zmienna += 5
    print(zmienna)


first_fun()
second_func()