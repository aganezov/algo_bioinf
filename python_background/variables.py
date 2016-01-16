# -*- coding: utf-8 -*-
__author__ = "Sergey Aganezov"

##########################################################################################
# __        _       _     _
# \ \    / /       (_)     | |   | |
#  \ \  / /_ _ _ __ _  __ _| |__ | | ___  ___
#   \ \/ / _` | '__| |/ _` | '_ \| |/ _ \/ __|
#    \  / (_| | |  | | (_| | |_) | |  __/\__ \
#     \/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
#
##########################################################################################

# Variable are just containers to store data
# You don't have to specify variable type explicitly
# NO semicolons and the end of the line!!!

# integers
a = 1                   # a = 1
c = a + 2               # c = 3
a += 3                  # a = 4

# you can exchange variable values simpler than ever
a = 1                   # a = 1
b = 2                   # b = 2
a, b = b, a             # a = 2, b = 1

# all basic arithmetic is there for you
answer = 2 + 3          # answer = 5
answer = 2 - 3          # answer = -1
answer = 2 * 3          # answer = 6
answer = 5 / 2          # answer = 2.5
answer = 5 // 2         # answer = 1
answer = 5 % 2          # answer = 1
answer = 4 ** 2         # answer = 16


# you can work with long numbers without worrying about overflowing short / int / long basic numbers types
very_large_number = 100 ** 100      # 100 to the power of 100

# arithmetic operations can be written similarly to the math expressions
answer = 5 + 3 - 2 * 4          # answer = 0
answer = (5 + 1 - 2) * 4        # answer = 16


##########################################################################################
#
#  __  __       _______ _    _                           _       _
# |  \/  |   /\|__   __| |  | |                         | |     | |
# | \  / |  /  \  | |  | |__| |      _ __ ___   ___   __| |_   _| | ___
# | |\/| | / /\ \ | |  |  __  |     | '_ ` _ \ / _ \ / _` | | | | |/ _ \
# | |  | |/ ____ \| |  | |  | |     | | | | | | (_) | (_| | |_| | |  __/
# |_|  |_/_/    \_\_|  |_|  |_|     |_| |_| |_|\___/ \__,_|\__,_|_|\___|
#
#
##########################################################################################


# to utilize core or third party module just import it
import math

# to round your division results
answer = math.ceil(5 / 2)       # answer = 3
answer = math.floor(5 / 2)      # answer = 2
answer = math.factorial(5)      # answer = 120
answer = math.exp(3)            # answer =~20.086
answer = math.pow(3, 3)         # answer = 27
answer = math.gcd(12, 16)       # answer = 4
answer = math.log(8, 2)         # answer = 3
answer = math.sqrt(144)         # answer = 12




