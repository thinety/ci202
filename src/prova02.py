from math import cos, exp
from lib import root_finding as rf


# Questão 1

def f(x):
    return -16*cos(-2*x) + 13*x**2 - 267.69

rf.bisection(f, 2, 12, 1, 6)

# Questão 2

def f(x):
    return 19*x**-3 - 4*x**3 + 93.79
def f_prime(x):
    return -57*x**-4 - 12*x**2

rf.newton_raphson(f, f_prime, 2, 0.0001, 0.0001, 5)

# Questão 3

def f(x):
    return 13*exp(2*x) - 15*x**-1 - 1913.62

# 5 iterações no método da secante significa calcular até x_6
# já que começamos com tanto x_0 como x_1
rf.secant(f, 2, 3, 0.01, 0.01, 6)
