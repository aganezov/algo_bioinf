# -*- coding: utf-8 -*-

# Python standard library contains a number of very useful modules
#   that you can utilize during the majority of algorithm programming activities

##############################################################################
#
# We start with the basic built in function of the python, that provides one with indexations over iterable elements
#   If in C / C++ / Java you usually used ``for`` loop with index variable, in python standard ``for`` loop works as an iterator
#   While one can use the for loop over the indexes, there is a better way to write a pythonic code, while preserving the indexing routine
#
# Using the function ``enumerate``, one can preserve the standard ``for`` loop iteration and also obtain indexes of every entry
#   remember that python indexation starts with 0
#
#############################################################################
print("Obtaining indexes os each value during the iteration with ``enumerate`` function")
for cnt, entry in enumerate([1, 2, 3, 4]):
    print("index:", cnt, "entry:", entry)
print()
#############################################################################
#
# We are going to start with ``itertools`` module, which, as it can derived from its name, provides
#   one with some pre-implemented functions, classes, etc that are in one way or another are responsible for the iteration
#
#############################################################################

# import the module itself
import itertools

# usually the main object to process with classes / functions from itertools modules is some sort of collection

#############################################################################
#
# let us start with combinations of elements from some iterable container
#       amount of elements in each supplied tuple can vary. To change it specify the respective ``r`` function parameter
#       on every step of the iteration tuples of length ``r`` are yielded
#
#############################################################################
print("All combinations of length 2 from [1, 2, 3, 4]. Entry repeats are not allowed")
for entry in itertools.combinations([1, 2, 3, 4], r=2):  # this will yield all possible combinations of two elements from collection
    print(entry)
print()
#############################################################################
#
# As you might have noticed, there are no repeats of the same initial collection entry in the produced combination
#       If such combination is desired one can achieve it by using a slightly different function
#
#############################################################################
print("All combinations of length 2 from [1, 2, 3, 4]. Entry repeats are allowed")
for entry in itertools.combinations_with_replacement([1, 2, 3, 4], r=2):
    print(entry)
print()
#############################################################################
#
# If one wants to iterate items in a certain collection in an infinite cycle, ``itertools`` got you covered
#
#############################################################################
print("Infinite cycle over collection [1, 2, 3, 4]. Infinite is too long for your life, so we will stop at 10th entry")
cnt = 0
for entry in itertools.cycle([1, 2, 3, 4]):
    print(entry)
    cnt += 1
    if cnt > 10:
        break
print()

#############################################################################
#
# Is one looks for permutations, rather than combinations, there is a designated function in ``itertools`` package
#   length of permutations can be specified by ``r`` parameter. By default ``r`` equals to the length of supplied collection
#
#############################################################################
print("Getting all permutation instead of combinations form [1, 2, 3, 4]. Length of each obtained permutation equals to 3")
for entry in itertools.permutations(iterable=[1, 2, 3, 4], r=3):
    print(entry)
print()

#############################################################################
#
# There is also a way to obtain a cartesian product of the supplied iterable with itself.
#
#############################################################################
print("Getting all entries in cartesian product of [1, 2, 3, 4] with itself")
for entry in itertools.product([1, 2, 3, 4]):
    print(entry)
print()

#############################################################################
#
# Repeats of the entries are allowed, though by default are forbidden
#   with ``repeat`` parameter one ca specify the maximum number of repeats of collections entries in the cartesian product values
#
#############################################################################

print("Getting all entries in cartesian product of [1, 2, 3, 4] with itself. Number of entry repeats is restricted by ``repeat`` = 2")
for entry in itertools.product([1, 2, 3, 4], repeat=2):
    print(entry)
print()

#############################################################################
#
# Whenever one want to iterate over several iterable collections at the same time, builtin ``zip`` function shall be utilized
#   supplied with a list of iterable collection on each step zip yields a tuple of elements at current step in each of the supplied entry
#   iteration is stopped when the shortest supplied collection is exhausted
#
#############################################################################
print("Using builtin ``zip`` function to simultaneously iterate multiple collections. ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5])")
for entry in zip([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5]):
    print(entry)
print()

#############################################################################
#
# If one wants to sue the ``zip`` functionality, but wants to iterate with respect to the longest collections
#   itertools module has a function ``zip_longest``, that provides ``zip`` like functionality, but stops iterating when the longest
#   supplied collection is exhausted. When  shorted collection is exhausted, entries, that would have belongs to it are substituted with
#       None
#
#############################################################################
print("Using ``zip_longest`` function to simultaneously iterate multiple collections. ([1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5])")
for entry in itertools.zip_longest([1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5]):
    print(entry)
print()
