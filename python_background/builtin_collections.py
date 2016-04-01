from collections import namedtuple

#
# namedtuple
#
#   simple way to create tuple like object with class behaviour
#
print("Standard tuple")
point = (1, 2, 3, 4)
print(point)
print(point[0])
print(point[1])

print("\n")
print("Named tuple")
Point = namedtuple('Point', ['x', 'y', 'z', 'z2'])
b = Point(x=1, y=2, z=3, z2=4)
print("named tuple", b)
print("field access", b.x)

#
# deque
#

# ------
print()
from collections import deque
d = deque()
print("Empty deque", d)

d = deque('acgt')
print("Deque with values", d)
d.appendleft('g')
d.append('g')
print("Deque after appending / appending to left values", d)
d.pop()
d.popleft()
print("Deque after popping / popping from left values", d)


#
# Counter
#
# ------
print()
from collections import Counter

print("Counter object, that goes through the iterable and counts the number of each distinct elements")
c = Counter('acgtgtcgctgatcgctagtcgatcg'.upper())
print("Counter", c)
print("Counter element access", c['C'])

c = Counter({'c': 7, 'g': 15})
print("Counter from dict", c)

print("Accessing most common element", c.most_common(3))

c['C'] = 0
print("Most common element access after manual element count setting", c.most_common(3))











#
# OrderedDict
#
from collections import OrderedDict
print()
d = {1: 1, 2: 2, 4: 4, 3: 3}
print("Ordered dict that preserves the order of added elements", d)


od = OrderedDict()
od[1] = 1
od[2] = 2
od[4] = 4
od[3] = 3
print("Ordered dict with elements manually set up during program execution", od)




#
# defaultdict
#
print()
from collections import defaultdict
print("Default dict allows to treat entries of non existing key, as if the specified data structure was there already")
our_dict = defaultdict(list)
our_dict["1"].append(1)
print(our_dict)



