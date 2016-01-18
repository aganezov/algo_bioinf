# -*- coding: utf-8 -*-

###########################################################################
#
#  _      _____  _____ _______
# | |    |_   _|/ ____|__   __|
# | |      | | | (___    | |
# | |      | |  \___ \   | |
# | |____ _| |_ ____) |  | |
# |______|_____|_____/   |_|
#
#
###########################################################################

###
#
# List is a mutable sequence-like data structure
# Complexity of element access O(1)
# Complexity of element change O(1)
# Complexity of element appending O(1) (amortized case)
# Complexity of element deletion O(n)
#
##

# list declaration
a = [1, 2, 3, 4]

# entries in list can be of any type, a not all of them have to be of same color
a = [1, 2, "string", 3, 4]
a = [1, 2, [3, 4], "string", 5, 6, 7]

# accessing list element
# list indexing starts with 0
answer = a[0]  # answer = 0
answer = a[2]  # answer = [3, 4]

# list slicing
# one can obtain a subsequence from original list
# specified subsequence range is inclusive on the left, but non-inclusive on the right
answer = a[0:2]  # answer = [1, 2]
answer = a[1:3]  # answer = [2, [3, 4]]

# one can specify the gap / step for elements to be taken from the range with
answer = a[0:4:2]  # answer = [1, [3, 4]]
answer = a[0:6:3]  # answer = [1, "string"]

# you can access elements from the end of list with negative indexing
answer = a[-1]  # answer = 7
answer = a[-5]  # answer = [3, 4]
answer = a[8:0:-1]  # answer = [7, 6, 5, "string", [3, 4], 2]

# one can omit star / end indices when slicing
answer = a[:2]  # answer = [1, 2]
answer = a[:4:2]  # answer = [1, [3, 4]]

# to change the element at certain position just assign a new value with a specific index
a = [1, 2, 3, 4, 5, 6, 7]
a[2] = 3.5  # a = [1, 2, 3.5, 4, 5, 6, 7]
a[:2] = [2, 1]  # a = [2, 1, 3.5, 4, 5, 6, 7]

# when a list is assigned to several variables, they refer to the same object and changes in that object are reflected in all variables
a = [1, 2, 3, 4]
b = a
a[2] = 2.5
answer = b[2]  # answer = 2.5

# deleting an element by its index
answer = a  # answer = [1, 2.5, 3, 4]
del a[0]
answer = a  # answer = [2.5, 3, 4]

###########################################################################
#
#  _______          _
# |__   __|        | |
#    | |_   _ _ __ | | ___
#    | | | | | '_ \| |/ _ \
#    | | |_| | |_) | |  __/
#    |_|\__,_| .__/|_|\___|
#            | |
#            |_|
#
###########################################################################

###
#
# Tuple is a Immutable sequence-like data structure
# Complexity of element access O(1)
#
##

# tuples correspond to the unchanging sequences of objects
a = (1, "string", [1, 2], 4)

# accessing elements works the same way the list elements accessing works
answer = a[3]  # answer = 4

# you can not reassign a new element to the specific spot in the tuple
# THIS LINE IS A PROGRAMMING ERROR
a[1] = 3

# if a tuple entry itself is mutable (like list), it can be changed internally, while the tuple structure will be intact
answer = a[2]  # answer = [1, 2], a = (1, "string", [1, 2], 4)
a[2][0] = 3
answer = a[2]  # answer = [3, 2], a = (1, "string", [3, 2], 4)

###########################################################################
#  _____  _      _   _
# |  __ \(_)    | | (_)
# | |  | |_  ___| |_ _  ___  _ __   __ _ _ __ _   _
# | |  | | |/ __| __| |/ _ \| '_ \ / _` | '__| | | |
# | |__| | | (__| |_| | (_) | | | | (_| | |  | |_| |
# |_____/|_|\___|\__|_|\___/|_| |_|\__,_|_|   \__, |
#                                              __/ |
#                                             |___/
#
###########################################################################

###
#
# Dictionaries is a mutable key-value data structure
# Complexity of element access O(1) (Amortized O(n))
# Complexity of element setting O(1) (Amortized O(n))
# Complexity of element deletion O(1) (Amortized O(n))
#
##

# Dictionary declaration
# Keys go before ":" character. Any hashable object can be a key
# Values go after ":" character. Any object can be a value
a = {}                              # empty dictionary declaration
a = {1: "1", "2": 2}

# Element setting
a[3] = "3"
answer = a                          # answer = {1: "1", "2": 2, 3: "3"}

# Setting a new value to the already existing key overwrites previously set value
answer = a                          # answer = {1: "1", "2": 2, 3: "3"}
a[3] = 4
answer = a                          # answer = {1: "1", "2": 2, 3: 4}

# Element accessing
answer = a[3]                       # answer = 4

# Element deleting
del a[4]
answer = a                          # answer = {1: "1", "2": 2}


###########################################################################
#
#   _____      _
#  / ____|    | |
# | (___   ___| |_
#  \___ \ / _ \ __|
#  ____) |  __/ |_
# |_____/ \___|\__|
#
#
###########################################################################

###
#
# Dictionaries is a mutable non ordered data structure of unique entries
# Complexity of element addition O(1)
# Complexity of element deletion O(n)
#
##

# Set declaration
a = {1, 2, 3}
a = set()               # empty set declaration. Can not do it with {}, as that is the way to declare empty an empty dictionary

# Element addition
a.add(3)
answer = a                          # answer = {3}
# Adding same element multiple times doesn't result in multiple entries
a.add(3)
answer = a                          # answer = {3}

# Element deletion
a.remove(3)
answer = a                          # answer = {3}
