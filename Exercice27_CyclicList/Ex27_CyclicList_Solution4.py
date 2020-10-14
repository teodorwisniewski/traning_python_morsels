from collections import UserList
from itertools import cycle
#
# class CyclicList(list):
#
#     def __iter__(self):
#         index = 0
#         while True:
#             yield self[index]
#             index = (index+1) % len(self)


class CyclicList(UserList):

    def __iter__(self):
        return cycle(self.data)