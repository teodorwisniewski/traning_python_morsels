# CyclicList
from typing import Iterable, Any


class CyclicListIterator:

    def __init__(self, liste: Iterable):
        self.liste = liste
        self.index = 0

    def __next__(self):
        while True:
            if self.index >= len(self.liste):
                self.index = 0
            value = self.liste[self.index]
            self.index += 1
            return value

    def __iter__(self):
        self.index = 0
        return self


class CyclicList:

    def __init__(self, liste: Iterable):
        self.liste = list(liste)

    def __iter__(self):
        return CyclicListIterator(self.liste)

