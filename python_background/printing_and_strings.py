# -*- coding: utf-8 -*-

##############################################################################
#
# In python the function the outputs anything is a builtin ``print`` function
#   While for some specific objects, like files, there might exists another way to output values to desired location
#   ``print`` function works in 99.99% cases.
#
#   Print function intakes variable number of arguments. All positional arguments are to be printed out.
#   Positional arguments, such as ``sep``, ``end``, ``file`` can alter the behaviour of a print function, though preserving the mein flow
#
##############################################################################

# ``sep`` parameter specifies what will be put in between all the positional arguments supplied to the print function
# by default ``sep`` parameter equals to `` `` (space).
print("Multiple", "strings", "entries", "with", "``:``", "separator", sep=" : ")
# ``end`` parameter specifies what will be put at the end of the produces output
print("Multiple", "strings", "entries", "with", "``ENDING``", "suffix", end="  ENDING")

##############################################################################
#
# In python whenever a ``print`` function is invoked on some object, what actually happens is this:
#   print(a) -> print(str(a)) -> print(a.__str__())
#
# For predefined objects, such as integers, lists, tuples, etc __str__ function is predefined and works as expected
#
##############################################################################

print()
print("Printing a list", [1, 2, 3, 4])
print("Printing a tuple", (1, 2, 3, 4))
print("Printing a dictionary", {1: 1, 2: 2, 3: 3})
print("Printing a set", {1, 2, 3})


# For custom objects, which do not specify __str__ function explicitly there is a default behaviour, that, granted, works,
#   but not very useful


class BasicObject:
    pass


print()
print("Not a very useful string representation of an object", BasicObject())


# One can alter this behaviour by providing an implementation of an __str_ method for a custom object
class SmarterObject:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Smarter object with value:" + str(self.value)


print("A useful string representation of an object: ``", SmarterObject(5), "``")

##############################################################################
#
# String and printing go hand and hand, as in Python3 string are the ultimate objects, that are printed out
#
# Sometimes one wishes to print out a list of entries in a certain collection, but default python representation of a collection
#   is not ideal (i.e. separating comas are not required)
#
##############################################################################

print()
print("Printing a list by unpacking entries", end=": ")
print(*[1, 2, 3, 4])  # by using asterisk we unpack the list collections, and for the print this looks like ``print(1, 2, 3, 4)`` invocation

print("Printing a tuple by unpacking entries", end=": ")
print(*(1, 2, 3), sep="::")  # as you can see, you can specify special separators, and suffixes if you want

# Another way to obtain a string wot work with as a result is to use a builtin string functionality
#   that is a ``join`` method. Join method intakes an iterable of objects and joins them together in a single large string
#   where the separator is the initial string, a join method is called from. The only caveat is that entries in supplied collection
#   have to be of type ``str``
# this method shall be utilized when a collection is of a large size, and thus many-many iteration are required to compose the resulting
#   string

print()
print("Printing a large string composed by joining a collection of smaller strings:", " ".join(['1', '2', '3', '4']))

# if the entries in the collection are not of type ``str``
# one can work with it by creating a new list / generator entries in which are of type str

print("Printing a large string composed by joining a collection of objects (list comprehension):", " ".join([str(x) for x in [1, 2, 3, 4]]))
print("Printing a large string composed by joining a collection of objects (generator comprehension):", " ".join(str(x) for x in [1, 2, 3, 4]))
print("Printing a large string composed by joining a collection of objects (``map`` with ``str``):", " ".join(map(str, [1, 2, 3, 4])))

# one need to remember that in Python 3 list first creates a full new list, thus taking twice as much space, as original data did
# if only a single usage is expected, or the stringify option is easy (i.e. simply calling ``str`` on entries in our case)
#   generator expression are preferable, as that don't consume any additional space and each value is evaluated only when caled
#   thus not computing time is wasted

##############################################################################
#
# Strings in python have a list of useful predefine functions, that proved to be useful
#   in various processing pipelines. Bioinformatics is no different, especially taking into account the fact, that
#   a lot of processing and computing is done on strings.
#
##############################################################################

# to check is a given string starts with a specific substring one can use the ``startswith`` method
string = "ACGTACGT"
print()
print("String", string, "starts with ACGT:", string.startswith("ACGT"))
print("String", string, "starts with AGCT:", string.startswith("AGCT"))

# similar logic applies when a question, whether string ends with a specific substring, is raised
string = "ACGTACGT"
print("String", string, "ends with ACGT:", string.endswith("ACGT"))
print("String", string, "ends with AGCT:", string.endswith("AGCT"))

# if one wishes to find out, whether a string contains a substring in it or not, following methods can be utilized:
#   string.find(substring) -> returns an index of the first occurrence of the specified substring and -1 otherwise
#   string.index(substring) -> returns an index of the first occurrence of the specified substring and raises a ValueError otherwise
print("First occurrence of 'CGT' in 'ACGTACGT' is at position:", "ACGTACGT".find("CGT"))
print("First occurrence of 'CGT' in 'ACGTACGT' is at position:", "ACGTACGT".index("CGT"))
print("String 'ACGTACGT' doesn't contain a substring 'AAT', thus its index by ``find`` is:", "ACGTACGT".find("AAT"))

# if one wishes to find entries of a given substring in some larger string but starting from the right, such methods as
#   rfind
#   rindex
# will do the trick. Behaviour is the same as in cases of find and index described previously.

#####
#####
#
# strings in python have also a built in capacity to transform supplied strings into new object
# this can be of great use whenever som manipulation with the string are required

# to convert a given string to a lower case one needs to invoke ``lower`` method
a = "ACGT"
b = a.lower()
print()
print("String a:", a, "String b, that is 'a' converted to lower case:", b)
# same logic applies to the upper method
a = "acgt"
b = a.upper()
print("String a:", a, "String b, that is 'a' converted to upper case", b)

# one can substitute any given substring to a new value using the replace method, that returns a new copy of the supplied string
#   where desired substring has been substituted
a = "ACGTACGT"
b = a.replace("T", "U")
print("String a:", a, "String b, that is 'a' where 'T' has been replaced by 'U'", b)

# to split a long string into a list of shorter substrings one shall use the builtin method ``split``
#   by default the splitting character is " " (space), by a custom argument can be specified instead of " "
# important note: splitting character / substrings is omitted from the result
a = "ACGT ACGT ACGT"
print("String a:", a, "Substrings of 'a', that were obtained by splitting 'a' with default splitting character, that is space:", a.split())
a = "ACGT:ACGT:ACGT"
print("String a:", a, "Substrings of 'a', that were obtained by splitting 'a' with custom splitting character ':'", a.split(":"))
# one can specify multiple splitting characters / substrings
a = "ACGT:ACGT ACGT"
print("String a:", a, "Substrings of 'a', that were obtained by splitting 'a' with custom splitting characters (':', ' ')", a.split([":", ' ']))
