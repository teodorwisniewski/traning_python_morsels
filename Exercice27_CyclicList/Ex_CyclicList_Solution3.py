from typing import Any, Iterable
from itertools import cycle


class CyclicList:
    def __init__(self, data: Iterable):
        self.data = list(data)

    def __iter__(self):
        return cycle(self.data)

    def append(self,val):
        self.data.append(val)

    def pop(self,*args,**kwargs):
        return self.data.pop(*args,**kwargs)

    def __len__(self):
        return len(self.data)
