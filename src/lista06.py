import numpy as np
from lib import linear_systems
np.set_printoptions(precision=6, floatmode='maxprec_equal', suppress=True)


# Testes

A = np.array([
    [ 25.0,  5.0, 1.0],
    [ 64.0,  8.0, 1.0],
    [144.0, 12.0, 1.0],
])
B1 = np.array([1.0, 0.0, 0.0])
B2 = np.array([0.0, 1.0, 0.0])
B3 = np.array([0.0, 0.0, 1.0])
linear_systems.lu(A, B1, B2, B3)

M = np.array([
    [10.0, 2.0,  1.0,  7.0],
    [ 1.0, 5.0,  1.0, -8.0],
    [ 2.0, 3.0, 10.0,  6.0],
])
X = np.array([0.0, 0.0, 0.0])
linear_systems.gauss_jacobi(M, X, 10, 0.02)


# Lista

# Questão 1

A = np.array([
    [-4.2,  2.4,  9.9, -2.5],
    [ 9.2,  7.5,  8.0, -9.5],
    [ 1.2,  0.5, -4.3,  5.8],
    [-5.7, -3.1, -6.6, -4.9],
])
B1 = np.array([14.1, -4.2, 18.0, -12.4])
B2 = np.array([59.5, 99.2, -6.0, -77.1])
linear_systems.lu(A, B1, B2)

# Questão 2

A = np.array([
    [-6.1, -5.4, -3.7],
    [ 2.2, -3.6, -8.0],
    [ 3.6,  0.4, -5.0],
])
B1 = np.array([-28.9,   2.7, 25.7])
B2 = np.array([-93.2, -45.3,  0.7])
linear_systems.lu(A, B1, B2)

# Questão 3

# M = np.array([
#     [-3.9, -9.8,   8.2, -23.5,  67.3],
#     [22.4, -9.4,  -9.1,  -2.6, -48.9],
#     [ 8.4, 15.3,  -5.2,  -1.5, 118.6],
#     [ 3.9, -7.6, -15.1,   1.9, -49.7],
# ])
M = np.array([
    [22.4, -9.4,  -9.1,  -2.6, -48.9],
    [ 8.4, 15.3,  -5.2,  -1.5, 118.6],
    [ 3.9, -7.6, -15.1,   1.9, -49.7],
    [-3.9, -9.8,   8.2, -23.5,  67.3],
])
X = np.array([-0.4, 7.0, -1.1, -6.1])
linear_systems.gauss_jacobi(M, X, 5, 0.001)

# Questão 4

M = np.array([
    [-5.5,   3.6, -1.3,  19.6],
    [-6.8, -14.4,  6.7, 207.5],
    [-3.6,   8.0, 12.4, -34.2],
])
X = np.array([-9.9, -9.5, 0.5])
linear_systems.gauss_jacobi(M, X, 5, 0.001)
