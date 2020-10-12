# CyclicList
from typing import Iterable, Any


def CyclicList(liste: Iterable) ->Any:
    index = 0
    while True:
        if index >= len(liste):
            index = 0
        yield liste[index]
        index += 1


