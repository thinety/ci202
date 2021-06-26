import numpy as np
from lib import interpolation as it
np.set_printoptions(precision=4, floatmode='maxprec_equal', suppress=True)


# Testes

points = np.float64([
                     #[ 86.0, 1552],
                     [ 93.3, 1548],
                     [ 98.9, 1544],
                     [104.4, 1538],
                     #[110.0, 1532],
                    ])
it.polynomial(points)(100)
it.lagrange(points, 100)


# Lista

# Questão 1

points = np.float64([
                     #[4.4, 3.13],
                     #[5.0, 5.57],
                     [5.1, 0.45],
                     [5.6, 3.03],
                     [5.9, 0.07],
                     [6.0, 5.25],
                    ])
it.lagrange(points, 5.66)

# Questão 2

points = np.float64([
                     [1.7, -1.03],
                     [1.9, -2.02],
                     [2.8, -2.79],
                     [3.4,  3.69],
                    ])
it.lagrange(points, 1.95)

# Questão 3

points = np.float64([
                     [1.7,  5.16],
                     [2.1,  3.85],
                     [4.4,  5.41],
                     #[4.8,  5.56],
                     #[5.1,  1.29],
                     #[5.5, -1.22],
                    ])
it.polynomial(points)(1.93)

# Questão 4

points = np.float64([
                     [1.0,  2.03],
                     [1.4, -0.85],
                     [2.3, -2.74],
                    ])
it.polynomial(points)(1.05)

# Questão 5

points = np.float64([
                     [1.1, 0.97],
                     [1.6, 0.96],
                    ])
it.polynomial(points)(1.4)

# Questão 6

points = np.float64([
                     #[1.6,  1.51],
                     #[2.6,  5.54],
                     #[4.4,  0.95],
                     [4.8,  3.74],
                     [5.0, -2.96],
                     #[5.6, -0.38],
                    ])
it.polynomial(points)(4.94)
