from typing import Iterable, Any


class CyclicList:

    def __init__(self,data: Iterable):
        self.data = list(data)

    def __iter__(self) -> Any:
        self.index = 0
        while True:
            yield self.data[self.index]
            self.index = (self.index + 1) % len(self.data)
