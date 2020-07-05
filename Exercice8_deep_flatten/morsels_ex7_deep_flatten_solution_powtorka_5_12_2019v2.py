from pprint import pprint
# import collections

def deep_flatten(iteratorek):

    for i in iteratorek:
        if hasattr(i, "__iter__") and type(i) != str:
            yield from deep_flatten(i)
        else:
            yield i
# def deep_flatten(iteratorek):
#     flattended = collections.deque()
#     items = list(iteratorek)
#     while items:
#         # pprint(items)
#         el = items.pop()
#         if isinstance(el,(tuple, list)):
#             items.extend(el)
#         else:
#             flattended.appendleft(el)
#             # pprint(flattended)
#     return flattended
    

if __name__ == "__main__":
    pprint( list(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]) ))
    pprint( list(deep_flatten([[1, [2, 3]], 4, 5])) )

    numbers_and_words = enumerate(['lime', 'pear', 'jujube'])
    for cos in deep_flatten(numbers_and_words):
        pprint(cos)
    pprint( list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']])) )