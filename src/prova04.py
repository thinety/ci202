from lib import interpolation, curve_adjustment, numeric_integration

import numpy
numpy.set_printoptions(precision=4, floatmode='maxprec_equal', suppress=True)


# Questão 1

points = [
    (1.5, -2.81),
    (2.1, -0.30),
    (2.7,  2.17),
    # (3.0, -0.70),
]
interpolation.lagrange(points)(1.69)

# Questão 2

points = [
    (1.1,  1.05),
    (1.7, -1.84),
    (2.1,  0.01),
]
interpolation.newton(points)(1.34)

# Questão 3

points = [
    (1.1, -1.19),
    (1.7,  3.62),
    (2.3, -3.52),
    (2.9,  0.66),
]
functions = [
    lambda x: 1,
    lambda x: x,
    lambda x: x**2,
]
curve_adjustment.min_square(points, functions)

# Questão 4

points = [
    (1.0, 3.25),
    (1.8, 3.18),
    (2.6, 2.19),
    (3.4, 2.37),
    (4.2, 5.48),
    (5.0, 4.68),
    (5.8, 3.36),
]
numeric_integration.simpsons_rule(points)
