from math import exp, sin, cos, log
from lib import root_finding


# Questão 1

# exemplo
def f(x):
    return x**3 - 9*x + 3
for i in range(-3, 3):
    f(i), i

# a)
def f(x):
    return 7*exp(2*x) - 6*sin(-2*x) - 36.49
for i in range(-4, 6):
    f(i), i

# b)
def f(x):
    return -17*x**2 + 9*x**2 + 48.43
for i in range(-11, 0):
    f(i), i

# c)
def f(x):
    return 10*log(x**-3) + 17*x**-1 + 39.93
for i in range(1, 12):
    f(i), i

# d)
def f(x):
    return 15*x**2 - 5*x - 180.35
for i in range(-8, 0):
    f(i), i

# e)
def f(x):
    return 11*x**3 + 11*cos(-2*x) + 617.18
for i in range(-5, 5):
    f(i), i

# Questão 2

def f(x):
    return -17*exp(-x) + 4*cos(x) + 7.39
root_finding.bisection(f, -10, 4, 1, 5)

# Questão 3

def f(x):
    return -3*sin(-x) + 13*exp(x) - 1631.38
root_finding.bisection(f, 0, 8, 1, 5)

# Questão 4

def f(x):
    return -7*log(x**-2) + 14*x**-1 - 22.39
root_finding.false_position(f, 2, 23, 0.1, 5)

# Questão 5

def f(x):
    return -4*x**3 + 18*x**2 - 509.98
root_finding.false_position(f, -14, 3, 1, 5)
