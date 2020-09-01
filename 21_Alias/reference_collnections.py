
import ctypes

my_list = [1,2,3]
second_list = my_list
third_list = my_list

fouth_list = [my_list,3,2]

class SomeStuff:

    def __init__(self, tableau=None):
        self.tableau = tableau

some_obj = SomeStuff(tableau=my_list)
some_obj.tableau.append("blabla")

my_list_adress = id(my_list)

ref_count = ctypes.c_long.from_address(my_list_adress).value

print(my_list,fouth_list,some_obj.tableau)

print(f"REference count for my list is: {ref_count}")
del my_list,second_list,third_list,fouth_list
print(f"REference count for my list is: {ctypes.c_long.from_address(my_list_adress).value}")
