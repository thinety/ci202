import numpy as np


# Cramer

def cramer(A: np.ndarray, B: np.ndarray):
    n = A.shape[1]
    D = np.linalg.det(A)

    for i in range(n):
        A_i = np.copy(A)
        A_i[:, [i]] = B
        D_i = np.linalg.det(A_i)
        x_i = D_i/D

        # i começa em 0, mas a convenção em matemática é começar em 1
        print(f'x_{i+1} = {x_i}')

A = np.array([[1,3,-2],
              [2,-1,1],
              [4,3,-5]], dtype=np.float32)
B = np.array([[3],
              [12],
              [6]], dtype=np.float32)

cramer(A, B)


# Gauss

def gauss(M: np.ndarray):
    m = M.shape[0]

    # triangulação
    for i in range(m):
        # escolha do pivô
        pivot_row = np.argmax(np.abs(M[i:, i])) + i
        M[[i, pivot_row], :] = M[[pivot_row, i], :]

        # zerar elementos abaixo do pivô
        for j in range(i+1, m):
            M[j,:] -= M[j,i]/M[i,i] * M[i,:]

    # retrosubstituição
    x = np.zeros(m)
    for i in reversed(range(m)):
        x[i] = (M[i,-1] - np.sum(M[i, i+1:-1] * x[i+1:])) / M[i,i]

    # imprimir resultados
    for i in range(m):
        print(f'x_{i+1} = {x[i]}')

M = np.array([[1, 2, -1, 0, -4],
              [0, -1, 1, -1, 0],
              [-2, -1, 4, 2, 7],
              [4, 3, 0, 1, -10]], dtype=np.float32)

gauss(M)

# Gauss-Jordan

def gauss_jordan(M: np.ndarray):
    m = M.shape[0]

    # diagonalização
    for i in range(m):
        # zerar elementos acima e abaixo do pivô
        for j in range(m):
            if j == i:
                continue

            M[j,:] -= M[j,i]/M[i,i] * M[i,:]

    # normalização
    for i in range(m):
        M[i, :] /= M[i,i]

    # imprimir resultados
    for i in range(m):
        print(f'x_{i+1} = {M[i,-1]}')

M = np.array([[1, -3, 4, 1],
              [-2, 8, -6, 2],
              [3, -5, 15, 5]], dtype=np.float32)

gauss_jordan(M)

