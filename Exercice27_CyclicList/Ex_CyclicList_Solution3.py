from typing import Any, Iterable
from itertools import cycle


class CyclicList:
    def __init__(self, data: Iterable):
        self.data = list(data)

    def __iter__(self):
        return cycle(self.data)
