import numpy as np
from lib import linear_systems
np.set_printoptions(precision=4, floatmode='maxprec_equal', suppress=True)


# Questão 1

# M = np.array([
#     [ 8.0, 18.1,  9.4,  -10.1],
#     [13.4,  5.9, -6.5, -103.6],
#     [ 1.9, -4.1, -7.8,  -47.0],
# ])
M = np.array([
    [13.4,  5.9, -6.5, -103.6],
    [ 8.0, 18.1,  9.4,  -10.1],
    [ 1.9, -4.1, -7.8,  -47.0],
])
X = np.array([-3.8, -2.1, 6.2])
linear_systems.gauss_jacobi(M, X, 5, 0.001)

# Questão 2

M = np.array([
    [-6.3, -3.8,  -0.6,  -2.8],
    [ 8.7, 16.5,  -7.4, 124.2],
    [ 9.4, -6.3, -17.4,  68.2],
])
X = np.array([-2.2, 5.5, -7.1])
linear_systems.gauss_seidel(M, X, 5, 0.001)

# Questão 3

A = np.array([
    [-4.4, 8.9,  2.9],
    [-2.5, 0.2, -1.1],
    [ 7.5, 6.1,  5.8],
])
B1 = np.array([-88.6, 10.6, -109.0])
B2 = np.array([ 85.4,  9.6,   19.7])
linear_systems.lu(A, B1, B2)

# Questão 4

M = np.array([
    [-3.3, -5.9, 4.4, -29.8],
    [ 8.4,  1.7, 7.2,  31.3],
    [-6.6, -6.0, 1.0, -40.3],
])
linear_systems.gauss(M)
