import numpy as np
np.set_printoptions(precision=6, floatmode='maxprec_equal', suppress=True)


def cramer(M):
    """
    Resolve um sistema linear pela regra de Cramer.

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).

    Retorna o vetor solução.
    """

    n = M.shape[0]
    A = M[:,:-1]
    B = M[:,-1]

    D = np.linalg.det(A)
    X = np.zeros(n)
    for i in range(n):
        A_i = np.copy(A)
        A_i[:,i] = B
        D_i = np.linalg.det(A_i)
        X[i] = D_i/D

    return X

M = np.array([[ 1, 3,-2, 3],
              [ 2,-1, 1,12],
              [ 4, 3,-5, 6]], np.float64)

cramer(M)


def gauss(M, piv=True):
    """
    Resolve um sistema linear por eliminação de Gauss.

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).
    Ela é modificada durante o algoritmo.

    `piv` é um booleano que indica se a escolha do melhor pivô
    deve ser realizada em cada passo da triangulação.

    Retorna o vetor solução.
    """

    n = M.shape[0]

    # triangulação
    for i in range(n):
        if piv:
            # escolha do pivô
            pivot_row = np.argmax(np.abs(M[i:,i])) + i
            M[[i, pivot_row], :] = M[[pivot_row, i], :]

        # zerar elementos abaixo do pivô
        for j in range(i+1, n):
            M[j,:] -= M[j,i]/M[i,i] * M[i,:]

    # retrosubstituição
    X = np.zeros(n)
    for i in reversed(range(n)):
        X[i] = (M[i,-1] - np.sum(M[i,i+1:-1] * X[i+1:])) / M[i,i]

    return X

M = np.array([[ 1,  2, -1,  0,  -4],
              [ 0, -1,  1, -1,   0],
              [-2, -1,  4,  2,   7],
              [ 4,  3,  0,  1, -10]], np.float64)

gauss(M)


def gauss_jordan(M):
    """
    Resolve um sistema linear pelo método de Gauss-Jordan.

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).
    Ela é modificada durante o algoritmo.

    Retorna o vetor solução.
    """

    n = M.shape[0]

    # diagonalização
    for i in range(n):
        # zerar elementos acima e abaixo do pivô
        for j in range(n):
            if j == i:
                continue

            M[j,:] -= M[j,i]/M[i,i] * M[i,:]

    # solução
    X = np.zeros(n)
    for i in range(n):
        X[i] = M[i,-1] / M[i,i]

    return X

M = np.array([[ 1, -3,  4, 1],
              [-2,  8, -6, 2],
              [ 3, -5, 15, 5]], np.float64)

gauss_jordan(M)


# Lista

# Questão 1

M = np.array([[-8.4, -0.7, -5.9, -8.1, -10.4],
              [-4.0, -4.2, -6.2,  8.9, 167.5],
              [-1.1,  9.6,  6.2,  4.2, -88.9],
              [-7.6,  0.3, -8.6, -3.9,  42.4]], np.float64)

gauss(M, False)

# Questão 3

M = np.array([[-3.0, -1.3,  7.6, -3.5, -69.7],
              [ 7.0, -3.8,  5.1, -7.7,  40.0],
              [ 4.6, -9.1,  8.7,  6.9,  69.1],
              [ 3.0,  5.2, -6.3, -9.7,   3.1]], np.float64)

gauss(M)

# Questão 2

M = np.array([[-5.1,  7.4, 1.5, -56.5],
              [-0.6, -2.6, 6.8, -37.8],
              [-3.5,  0.1, 9.0, -71.4]], np.float64)

gauss_jordan(M)

# Questão 4

M = np.array([[-1.9,  2.7, -0.8, -4.6,  25.6],
              [-2.5,  8.1,  2.2,  3.4,  45.6],
              [-8.3,  8.5, -5.5,  3.8, 165.1],
              [-5.2, -4.5,  4.5,  0.9,  -5.1]], np.float64)

gauss_jordan(M)
