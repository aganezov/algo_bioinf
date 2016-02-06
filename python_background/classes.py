# -*- coding: utf-8 -*-


# Classes in python is a way to represent c composite objects, that can be both treated as a solid entities, but still have an access
#   to the encapsulated information
#
# Classes have methods, which are just regular functions, defined in a scope of a class and having a special first parameter
#   all class methods contain a conventional first parameter "self", that encapsulates all the data about the class instance,
#   the methods has been called from.
#
# Class methods are defined in order to encapsulate any logic, that is class specific.
#   One would use class method instead of a regular function, when additional information about instance fields is required by the
#   method's logic
# Just like any other function, class methods signatures can be created in a way, that accepts variable or fixed number of parameters,
#   as well as have keyword parameters with explicitly specified default values.


# implementing a linked list
# a double-linked list can be created, but a single linked list is created by default:
#                                      "reverse_link" parameter defaults to None

class Node(object):  # the good python practise is to inherit all classes from the base "object"
    def __init__(self, value, forward_link=None, reverse_link=None):
                            # __init__ method is a special class function. It is called when the class instance is created
                            # all methods for any object shall contain "self" argument as first parameter

                            # in the __init__method you specify the fields, that can later be accessed from the instance of the class

        self.value = value                  # create "value" field for the created instance and assign respective parameter
        self.forward_link = forward_link    # create "forward_link" field for the created instance and assign respective parameter
        self.reverse_link = reverse_link    # create "reverse_link" field for the created instance and assign respective parameter

    def print_value(self, greeting="invoked function \"print_value\""):
        print(greeting)
        print("value", self.value)


# creating a forward linked list with 4 entries
#   creating entries from the last to the first, so we can specify the forward link
fourth = Node(value=4, forward_link=None)
third = Node(value=3, forward_link=fourth)
second = Node(value=2, forward_link=third)
first = Node(value=1, forward_link=second)

# with forward-only linked list we can traverse it only once in the forward direction,
# as once we are at a certain location, we have no way to go back or to find out even the previous value
print("Traversing a forward-linked list...")
current = first
while current is not None:
    current.print_value()
    current = current.forward_link
print()


# creating a double-linked list with 4 entries
#   in double-linked list every entry has a link to its predecessor, thus we can traverse list in both ways from any point
fourth = Node(value=4)
third = Node(value=3)
second = Node(value=2)
first = Node(value=1)
# no we specify links between the entries
fourth.reverse_link = third
third.forward_link = fourth

third.reverse_link = second
second.forward_link = third

second.reverse_link = first
first.forward_link = second

# with a double linked list we can traverse if in both directions from ny point
#   we inplement the turn-around traversal, when we go all teh way to the end of the list, and then come all the way back

direction = "forward"
current = first
print("Traversing a double-linked list in a turn-around fashion...")
while current is not None:
    current.print_value(greeting="invoking the function, going {direction}".format(direction=direction))
    if direction == "forward":
        if current.forward_link is None:
            direction = "reverse"
            print("approached lists end")
        else:
            current = current.forward_link
    else:
        current = current.reverse_link




