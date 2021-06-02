from copy import deepcopy
from numpy.linalg import det


# Cramer

def replace_column(A, B, n):
    A = deepcopy(A)

    for i in range(len(A)):
        A[i][n] = B[i][0]

    return A

def cramer(A, B):
    D = det(A)
    for i in range(len(A)):
        A_i = replace_column(A, B, i)
        D_i = det(A_i)

        # i começa em 0, mas a convenção em matemática é começar em 1
        print(f'x_{i+1} = {D_i/D :.6f}')

A = [[1,3,-2],
     [2,-1,1],
     [4,3,-5]]
B = [[3],
     [12],
     [6]]

cramer(A, B)


# Gauss

def gauss():
    pass


# Gauss-Jordan

def gauss_jordan():
    pass
