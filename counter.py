
import collections
from itertools import zip_longest 

capitals = ['Warsaw', 'London', 'Paris', 'Paris', 'Moscow']

capitals2 = ['Berlin', 'Prague', 'Minsk', 'Helsinki', ]

how_many = collections.Counter(capitals)

print(how_many.most_common(1), end ="\n\n")

for index, how_many in enumerate(how_many):
    print(index, how_many)


for x in capitals:
    print(x)

print("\n")

for capitals, capitals2 in zip_longest(capitals, capitals2):
    print(capitals, capitals2)
