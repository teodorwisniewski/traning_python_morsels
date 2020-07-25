import sys
import decimal
import operator

d = {"int": 0,
    "float": 0.0,
    "dict": dict(),
    "set": set(),
    "tuple": tuple(),
    "list": list(),
    "str": "a",
    "unicode": u"a",
    "decimal": decimal.Decimal(0),
    "object": object(),
 }

# Create new dict that can be sorted by size
d_size = {}

for k, v in sorted(d.items()):
    d_size[k]=sys.getsizeof(v)

sorted_x = sorted(d_size.items(), key=lambda kv: kv[1])

print(sorted_x)