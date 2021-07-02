from lib import linear_systems

import numpy
numpy.set_printoptions(precision=6, floatmode='maxprec_equal', suppress=True)


# Testes

M = [
    [ 1.0,  3.0, -2.0,  3.0],
    [ 2.0, -1.0,  1.0, 12.0],
    [ 4.0,  3.0, -5.0,  6.0],
]
linear_systems.cramer(M)

M = [
    [ 1.0,  2.0, -1.0,  0.0,  -4.0],
    [ 0.0, -1.0,  1.0, -1.0,   0.0],
    [-2.0, -1.0,  4.0,  2.0,   7.0],
    [ 4.0,  3.0,  0.0,  1.0, -10.0],
]
linear_systems.gauss(M)

M = [
    [ 1.0, -3.0,  4.0, 1.0],
    [-2.0,  8.0, -6.0, 2.0],
    [ 3.0, -5.0, 15.0, 5.0],
]
linear_systems.gauss_jordan(M)


# Lista

# Questão 1

M = [
    [-8.4, -0.7, -5.9, -8.1, -10.4],
    [-4.0, -4.2, -6.2,  8.9, 167.5],
    [-1.1,  9.6,  6.2,  4.2, -88.9],
    [-7.6,  0.3, -8.6, -3.9,  42.4],
]
linear_systems.gauss(M, False)

# Questão 2

M = [
    [-5.1,  7.4, 1.5, -56.5],
    [-0.6, -2.6, 6.8, -37.8],
    [-3.5,  0.1, 9.0, -71.4],
]
linear_systems.gauss_jordan(M)

# Questão 3

M = [
    [-3.0, -1.3,  7.6, -3.5, -69.7],
    [ 7.0, -3.8,  5.1, -7.7,  40.0],
    [ 4.6, -9.1,  8.7,  6.9,  69.1],
    [ 3.0,  5.2, -6.3, -9.7,   3.1],
]
linear_systems.gauss(M)

# Questão 4

M = [
    [-1.9,  2.7, -0.8, -4.6,  25.6],
    [-2.5,  8.1,  2.2,  3.4,  45.6],
    [-8.3,  8.5, -5.5,  3.8, 165.1],
    [-5.2, -4.5,  4.5,  0.9,  -5.1],
]
linear_systems.gauss_jordan(M)
