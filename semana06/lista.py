import numpy as np
np.set_printoptions(precision=6, floatmode='maxprec_equal', suppress=True)


def lu(A, *Bs):
    """
    Resolve `k` sistemas lineares por fatoração LU.

    `A` é a matriz dos coeficientes (`n x n`), e os outros
    `k` parâmetros são os vetores dos termos contantes.

    Retorna os `k` vetores solução.
    """

    n = A.shape[0]

    L = np.eye(n)
    U = np.copy(A)

    # fatoração LU
    for i in range(n):
        for j in range(i+1, n):
            m_ji = U[j,i]/U[i,i]
            L[j,i] = m_ji
            U[j,:] -= m_ji * U[i,:]

    Xs = []
    for B in Bs:
        Y = np.zeros(n)
        for i in range(n):
            Y[i] = (B[i] - np.sum(L[i,:i] * Y[:i])) / L[i,i]

        X = np.zeros(n)
        for i in reversed(range(n)):
            X[i] = (Y[i] - np.sum(U[i,i+1:] * X[i+1:])) / U[i,i]

        Xs.append(X)

    return tuple(Xs)


A = np.array([[ 25,  5, 1],
              [ 64,  8, 1],
              [144, 12, 1]], np.float64)
B1 = np.array([1, 0, 0], np.float64)
B2 = np.array([0, 1, 0], np.float64)
B3 = np.array([0, 0, 1], np.float64)

lu(A, B1, B2, B3)


def gauss_jacobi(M, X, max_i, max_err):
    """
    Resolve um sistema linear pelo método de Gauss-Jacobi

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).
    `X` é o vetor com as aproximações iniciais, que é
    modificado durante o algoritmo.
    """

    n = M.shape[0]
    A = M[:,:-1]
    B = M[:,-1].reshape((n,1))
    X = X.reshape((n,1))

    D = np.eye(n)*A
    I = np.tri(n, k=-1)*A
    S = np.transpose(np.tri(n, k=-1))*A

    D_inv = np.linalg.inv(D)
    J = -D_inv@(I+S)
    E = D_inv@B

    i = 0
    X_prev = np.zeros((n,1))
    while True:
        i += 1
        X_prev[:] = X
        X[:] = J@X + E

        if i == max_i:
            break
        if np.max(np.abs(X-X_prev)) < max_err:
            break

M = np.array([[10, 2,  1,  7],
              [ 1, 5,  1, -8],
              [ 2, 3, 10,  6]], np.float64)
X = np.array([0, 0, 0], np.float64)

gauss_jacobi(M, X, 10, 0.02)


# Lista

# Questão 1

A = np.array([[-4.2,  2.4,  9.9, -2.5],
              [ 9.2,  7.5,  8.0, -9.5],
              [ 1.2,  0.5, -4.3,  5.8],
              [-5.7, -3.1, -6.6, -4.9]], np.float64)
B1 = np.array([14.1, -4.2, 18, -12.4], np.float64)
B2 = np.array([59.5, 99.2, -6, -77.1], np.float64)

lu(A, B1, B2)

# Questão 2

A = np.array([[-6.1, -5.4, -3.7],
              [ 2.2, -3.6, -8.0],
              [ 3.6,  0.4, -5.0]], np.float64)
B1 = np.array([-28.9,   2.7, 25.7], np.float64)
B2 = np.array([-93.2, -45.3,  0.7], np.float64)

lu(A, B1, B2)

# Questão 3

# M = np.array([[-3.9, -9.8,   8.2, -23.5,  67.3],
#               [22.4, -9.4,  -9.1,  -2.6, -48.9],
#               [ 8.4, 15.3,  -5.2,  -1.5, 118.6],
#               [ 3.9, -7.6, -15.1,   1.9, -49.7]], np.float64)
M = np.array([[22.4, -9.4,  -9.1,  -2.6, -48.9],
              [ 8.4, 15.3,  -5.2,  -1.5, 118.6],
              [ 3.9, -7.6, -15.1,   1.9, -49.7],
              [-3.9, -9.8,   8.2, -23.5,  67.3]], np.float64)
X = np.array([-0.4, 7, -1.1, -6.1], np.float64)

gauss_jacobi(M, X, 5, 0.001)

# Questão 4

M = np.array([[-5.5,   3.6, -1.3,  19.6],
              [-6.8, -14.4,  6.7, 207.5],
              [-3.6,   8.0, 12.4, -34.2]], np.float64)
X = np.array([-9.9, -9.5, 0.5], np.float64)

gauss_jacobi(M, X, 5, 0.001)
