from math import sin, cos, exp, log
from lib import root_finding as rf


# Questão 1

def f(x):
    return 7*sin(2*x) + 7*x**-2 - 2*exp(-2*x) + 322.95
def g(x):
    return -0.5*log(3.5*sin(2*x) + 3.5*x**-2 + 161.475)

rf.linear_iteration(g, -2, 4)

# Questão 2

def f(x):
    return - 5*x**-0.5 - 17*exp(x) + 857.13
def f_prime(x):
    return 2.5*x**-1.5 - 17*exp(x)

rf.mixed(f, f_prime, 3, 9, 9)

# Questão 3

def f(x):
    return 13*log(x**-2) - 17*exp(2*x) + 25192.37

rf.secant(f, 3, 4, 0.01, 10)

# Questão 4

def f(x):
    return 11*cos(3*x) - 19*sin(3*x) + log(x) - 5.05
def g(x):
    return exp(19*sin(3*x) - 11*cos(3*x) + 5.05)

rf.linear_iteration(g, 0, 4)

# Questão 5

def f(x):
    return 15*x**-0.5 + 20*x**-2 - 23.43
def f_prime(x):
    return -7.5*x**-1.5 - 40*x**-3

rf.newton_raphson(f, f_prime, 1)

# Questão 6

def f(x):
    return x**2 + 14*cos(2*x) - 10.69
def f_prime(x):
    return 2*x - 28*sin(2*x)

rf.mixed(f, f_prime, -4, -1, -4)

# Questão 7

def f(x):
    return 14*x**3 - x**-1 - 1391.12

rf.secant(f, 4, 5)

# Questão 8

def f(x):
    return -11*exp(x) - 8*x**-1 + 393.85
def f_prime(x):
    return -11*exp(x) + 8*x**-2

rf.newton_raphson(f, f_prime, 3)
