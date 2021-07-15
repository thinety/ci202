from math import sqrt, exp
import numpy as np
from lib import numeric_integration


# Testes

f = lambda x: x**2 - 1.0
p = np.linspace(-1.0, 1.0, 5)
numeric_integration.rectangle_rule(f, p)

points = [(x, f(x)) for x in p]
numeric_integration.trapezoidal_rule(points)
numeric_integration.simpsons_rule(points)

points = [
    (0.0, 1.0000),
    (0.2, 1.2408),
    (0.4, 1.5735),
    (0.6, 2.0333),
    (0.8, 2.6965),
    (1.0, 3.7183),
]
answer = (
    numeric_integration.trapezoidal_rule(points[:2])
    + numeric_integration.simpsons_rule(points[1:])
)


# Lista

# Questão 1

f = lambda x: 9 * sqrt(x)
p = np.linspace(1.5, 3.1, 5)
points = [(x, f(x)) for x in p]
numeric_integration.simpsons_rule(points)

points = [
    (2.7, 1.49),
    (3.2, 1.45),
    (3.7, 0.69),
    (4.2, 0.36),
    (4.7, 2.13),
]
numeric_integration.simpsons_rule(points)

# Questão 2

f = lambda x: 6 * sqrt(x**3)
p = np.linspace(1.0, 3.4, 7)
numeric_integration.rectangle_rule(f, p)

f = lambda x: 6 * sqrt(x**2) + x**-3
p = np.linspace(2.2, 4.0, 7)
numeric_integration.rectangle_rule(f, p)

# Questão 3

f = lambda x: exp(x) - 4 * x**-2
p = np.linspace(3.8, 6.8, 7)
points = [(x, f(x)) for x in p]
numeric_integration.trapezoidal_rule(points)

points = [
    (5.2, 0.87),
    (5.6, 3.60),
    (6.0, 0.86),
    (6.4, 4.03),
    (6.8, 1.16),
    (7.2, 4.63),
    (7.6, 1.00),
]
numeric_integration.trapezoidal_rule(points)
