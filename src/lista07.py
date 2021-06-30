import numpy as np
from lib import linear_systems
np.set_printoptions(precision=4, floatmode='maxprec_equal', suppress=True)


# Testes

M = np.array([
    [10.0, 2.0,  1.0,  7.0],
    [ 1.0, 5.0,  1.0, -8.0],
    [ 2.0, 3.0, 10.0,  6.0],
])
X = np.array([0.0, 0.0, 0.0])
linear_systems.gauss_seidel(M, X, 10, 0.02)

M = np.array([
    [10.0,   2.0,  1.0,  7.0],
    [ 1.0, -15.0,  1.0, 32.0],
    [ 2.0,   3.0, 10.0,  6.0],
])
X = np.array([0.0, 0.0, 0.0])
linear_systems.relaxation(M, X, 10, 0.1)


# Lista

# Questão 1

# M = np.array([
#     [16.1,   2.8,  2.7,  9.9,  -26.5],
#     [ 1.0,   8.2, -4.9, 15.4,  236.0],
#     [ 8.7, -19.1, -3.2, -6.2, -269.3],
#     [ 8.6,   9.0, 23.8, -6.0, -187.3],
# ])
M = np.array([
    [16.1,   2.8,  2.7,  9.9,  -26.5],
    [ 8.7, -19.1, -3.2, -6.2, -269.3],
    [ 8.6,   9.0, 23.8, -6.0, -187.3],
    [ 1.0,   8.2, -4.9, 15.4,  236.0],
])
X = np.array([-8.1, 8.2, -5.6, 9.7])
linear_systems.gauss_seidel(M, X, 5, 0.001)

# Questão 2

M = np.array([
    [-0.5, -2.3,  1.7,  8.0,  73.4],
    [ 1.8, -2.6, -5.3,  5.9, -32.1],
    [-7.7, -3.9, -7.0,  3.7,   7.3],
    [-3.7,  8.1,  6.7, -1.5, 123.8],
])
X = np.array([-8.4, 4.9, 9.7, 8.0])
linear_systems.relaxation(M, X, 6, 0.01)

# Questão 3

M = np.array([
    [-2.3, -5.4, -9.8, -83.7],
    [-2.7,  6.7, -5.5, -74.8],
    [ 6.8,  1.6,  0.6,  56.2],
])
X = np.array([8.0, -1.7, 7.6])
linear_systems.relaxation(M, X, 6, 0.01)

# Questão 4

M = np.array([
    [14.1, -2.8,  9.5, 135.1],
    [-2.6, -4.6,  0.1,  15.4],
    [ 2.1,  6.0, -9.0, -32.0],
])
X = np.array([7.9, -7.8, 0.2])
linear_systems.gauss_seidel(M, X, 5, 0.001)
