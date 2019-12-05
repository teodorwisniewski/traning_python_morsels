
s = 'Siemano ludziska i inne stwory'
zmienne = s.split(" ")

# * operator can be used to unpack an iterable into the arguments in the function call
# wyslanie do printa wszystkich argumentow jak oddzielne zmeinne
print(*zmienne)

tablica= []
for i in range (2): tablica.append([0]*2)

tablica[0][1] = 1

print(tablica)