# -*- coding: utf-8 -*-

# A function is a way for one to isolate a specific logic, that processes provided data, and returns something (None by default)
# In python one doesn't have to explicitly specify the type of the function parameters as well the type of the returned value
#   that being said, python a strongly typed programming language. It just happens, that it is dynamically typed.

# function is specified with a specific "def" keyword


# simplest function that takes a pair of arguments and output their sum
def summing_function(argument1, argument2):
    print("invoked \"summing_function\"", "argument1 :", argument1, "argument2 :", argument2)
    return argument1 + argument2

# function are invoked by their name and respective arguments
print("result", summing_function(1, 2))
# one can also specify the argument and explicitly provide names of respective parameters
print("result", summing_function(argument1=1, argument2=2))
# this approach allows one not to worry about the order of the arguments, and explicitly say which parameter shall be
print("result", summing_function(argument2=1, argument1=2))
# it is important to note, that if one specifies any parameters explicitly by their names, no arguments with name specificaiton
#   can be done following them


# in order to specify the function, that can accept variable amount of arguments, one should use the "*" sign
# all the arguments, that come before the parameter with an asterisks sign are mandatory for the function
#   while everything beyond that point is optional, and if provided will be encapsulated in the parameter marked with the asterisks sign
# it is an established convention to name a parameter for a optional variable number of parameters by "args"
def summing_function_var(argument1 ,argument2, *args):
    print("invoked \"summing_function_var\"", "argument1 :", argument1, "argument2 :", argument2,
          "additional arguments sequence :", args)
    result = argument1 + argument2
    for argument in args:
        result += argument
    return result


# function that is written to accept variable number of arguments can be called with no optional argument what so ever
print("result", summing_function_var(1, 2))
# if you provide any number of optional arguments, they will be encapsulated in the parameter marked with the asterisks sign
#   3, 4, 5 are optional argument in the following function call
print("result", summing_function_var(1, 2, 3, 4, 5))


# every function can have a list of parameters that are not just optional, but also have a default value
# this is particularly usefull when a parameter is utilized in the function logic and is mandatory for it, but the majority os use cases
#   require just a single value for such parameter
def summing_function_default(argument1, argument2, greeting="invoked \"summing_function_default\""):
    print(greeting)
    return argument1 + argument2

# for functions with pre defaulted parameters can be invoked without explicitly providing such parameters, but still utilizing them
print("result", summing_function_default(1, 2))
# when its required one can specify the pre defaulted parameter, thus altering the behaviour of the function
print("result", summing_function_default(1, 2, greeting="New greeting"))


# any combination of aforementioned approaches is possible and thus allows for a very flexible function behaviours
def sophisticated_function_1(argument1, *args, first_greeting="first_greeting", second_greeting="second greeting"):
    print(first_greeting)
    print(second_greeting)
    result = argument1
    for argument in args:
        result += argument
    return result

# and variable invocation of a complex function signature are possible
# one can design a function suiting his or her needs and then use different signatures, when invoking it,
#   thus altering the desired behaviour
print("result", sophisticated_function_1(1))
print("result", sophisticated_function_1(1, 2, 3, 4))
print("result", sophisticated_function_1(1, second_greeting="new second greeting"))
print("result", sophisticated_function_1(1, 2, 3, first_greeting="new first greeting"))


############################################################################################
#
# Functions can be defined inside other functions, just for the purpose of code readability
#
############################################################################################

# defining an outer function
def function1(argument1, argument2):

    # internal logic, that is reused multiple times inside the outer function
    def function2(argument):
        return argument + 2

    new_argument1 = function2(argument1)        # invoking separated function logic
    new_argument2 = function2(argument2)        # invoking AGAIN separated function logic
    return new_argument1 + new_argument2

