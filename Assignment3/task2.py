#Math Module

from math import *

# Square root
def sqRootFn(n):
    return sqrt(n)

# Logarithm
def lgFn(n):
    return log(n)

# Sine
def sinFn(n):
    return sin(n)
input = int(input('Enter a number: '))
print('Square root:', sqRootFn(input))
print('Logarithm:', lgFn(input))
print('Sine:', sinFn(input))

