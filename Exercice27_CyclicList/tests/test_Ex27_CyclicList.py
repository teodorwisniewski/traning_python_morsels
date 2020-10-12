import pytest
from itertools import islice
from Exercice27_CyclicList.Ex27_CyclicList import CyclicList


def test_base_problem():
    my_list = CyclicList([1, 2, 3])
    for i, n in enumerate(my_list):
        print(n)
        if i > 8:
            break
    assert list(islice(my_list, 5)) == [1, 2, 3, 1, 2]
