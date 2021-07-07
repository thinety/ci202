from math import cos, log
from lib import curve_adjustment

import numpy
numpy.set_printoptions(precision=4, floatmode='maxprec_equal', suppress=True)


# Testes

points = [
    (0.0, 0.0),
    (1.0, 1.0),
    (2.0, 1.0),
    (3.0, 4.0),
    (4.0, 4.0),
]
functions = [
    lambda x: 1,
    lambda x: x,
]
curve_adjustment.min_square(points, functions)(5)

points = [
    (0.0, 1.00),
    (1.5, 1.57),
    (3.0, 2.00),
    (4.5, 4.30),
    (6.0, 7.00),
]
functions = [
    lambda x: x,
    lambda x: cos(x),
]
curve_adjustment.min_square(points, functions)(6.5)


# Lista

# Questão 1

points = [
    (1.3, -3.47),
    (2.3, -0.34),
    (3.3, -2.00),
    (4.3, -0.52),
]
functions = [
    lambda x: 1,
    lambda x: x,
    lambda x: x**2,
]
curve_adjustment.min_square(points, functions)

# Questão 2

points = [
    (1.3, -1.64),
    (1.5, -1.31),
    (1.7, -2.20),
]
functions = [
    lambda x: 1,
    lambda x: log(x**1.6),
]
curve_adjustment.min_square(points, functions)

# Questão 3

points = [
    (1.7,  1.97),
    (2.5,  0.87),
    (3.3, -1.34),
    (4.1,  3.89),
]
functions = [
    lambda x: 1,
    lambda x: x,
    lambda x: x**2,
]
curve_adjustment.min_square(points, functions)
