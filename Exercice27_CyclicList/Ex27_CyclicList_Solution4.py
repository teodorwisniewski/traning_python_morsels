from collections import UserList

class CyclicList(list):

    def __iter__(self):
        index = 0
        while True:
            yield self[index]
            index = (index+1) % len(self)