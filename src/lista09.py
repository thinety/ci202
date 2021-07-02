from lib import interpolation

import numpy
numpy.set_printoptions(precision=4, floatmode='maxprec_equal', suppress=True)


# Testes

points = [
    # [ 0.0,   0.000],
    [ 8.0,  52.032],
    [20.0, 160.450],
    [30.0, 275.961],
    # [45.0, 370.276],
]
interpolation.newton(points)(25.0)

points = [
    # [1.00, 1.0000],
    [1.05, 1.0247],
    [1.10, 1.0488],
    [1.15, 1.0724],
    # [1.20, 1.0954],
]
interpolation.gregory_newton(points)(1.12)


# Lista

# Questão 1

points = [
    [1.1, -2.56],
    [1.2, -2.31],
    [2.8,  0.96],
    [4.0,  3.60],
]
interpolation.newton(points)(1.62)

# Questão 2

points = [
    [1.3, -1.56],
    [2.3, -1.60],
    [3.3, -0.60],
    [4.3,  0.53],
]
interpolation.gregory_newton(points)(3.36)

# Questão 3

points = [
    # [2.2,  2.50],
    [2.7, -5.69],
    [3.0, -3.95],
    [3.2,  3.39],
    [3.7, -3.52],
    # [5.0, -6.72],
    # [6.5, -4.69],
]
interpolation.newton(points)(3.03)
