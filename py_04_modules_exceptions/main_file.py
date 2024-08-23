# Module
# Library
# Package

# Built-in: random, math, itertools
# Library: pip3 install colorama
# User defined

# Full call
# import math
# from math import factorial, exp
# from math import *
from math import factorial as f
from colorama import Back, Fore, init, Style
from libraries.my_lib import sum, factorial


init()

print(Back.WHITE + Fore.RED + "Hello")
print(Style.RESET_ALL)
print("Foundation")


print(sum(5 ,6))

sum()
