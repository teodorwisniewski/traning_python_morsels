import pytest
from itertools import islice
#from Exercice27_CyclicList.Ex import CyclicList
from Exercice27_CyclicList.Ex_CyclicList_Solution3 import CyclicList
from Exercice27_CyclicList.Ex27_CyclicList_Solution4 import  CyclicList


def test_base_problem():
    my_list = CyclicList([1, 2, 3])
    for i, n in enumerate(my_list):
        print(n)
        if i > 8:
            break
    assert list(islice(my_list, 5)) == [1, 2, 3, 1, 2]
    
    
def test_base_problem_idependent_lists():
    numbers = CyclicList([1, 2, 3, 4])
    i1 = iter(numbers)
    i2 = iter(numbers)
    assert next(i1) == 1
    assert next(i1) == 2
    assert next(i2) == 1
    assert next(i2) == 2


# bonus 1 tests

def test_append_append_pop():
    my_list = CyclicList([1, 2, 3])
    my_list.append(4)
    assert my_list.pop() == 4
    assert len(my_list) == 3
    assert my_list.pop(0) == 1
    assert len(my_list) == 2
