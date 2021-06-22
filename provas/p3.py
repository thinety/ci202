import numpy as np
np.set_printoptions(precision=4, floatmode='maxprec_equal', suppress=True)


# Questão 1

def gauss_jacobi(M, X, max_i, max_err):
    """
    Resolve um sistema linear pelo método de Gauss-Jacobi

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).
    `X` é o vetor com as aproximações iniciais, que é
    modificado durante o algoritmo.

    É necesssário verificar as condições de convergência previamente
    (sistema deve estar na forma diagonalmente dominante).
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

# M = np.array([[ 8.0, 18.1,  9.4,  -10.1],
#               [13.4,  5.9, -6.5, -103.6],
#               [ 1.9, -4.1, -7.8,  -47.0]], np.float64)
M = np.array([[13.4,  5.9, -6.5, -103.6],
              [ 8.0, 18.1,  9.4,  -10.1],
              [ 1.9, -4.1, -7.8,  -47.0]], np.float64)
X = np.array([-3.8, -2.1, 6.2], np.float64)

gauss_jacobi(M, X, 5, 0.001)


# Questão 2

def gauss_seidel(M, X, max_i, max_err):
    """
    Resolve um sistema linear pelo método de Gauss-Seidel

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).
    `X` é o vetor com as aproximações iniciais, que é
    modificado durante o algoritmo.

    É necesssário verificar as condições de convergência previamente
    (sistema deve satisfazer o critério de Sassenfeld).
    """

    n = M.shape[0]
    A = M[:,:-1]
    B = M[:,-1].reshape((n,1))
    X = X.reshape((n,1))

    D = np.eye(n)*A
    I = np.tri(n, k=-1)*A
    S = np.transpose(np.tri(n, k=-1))*A

    D_plus_I_inv = np.linalg.inv(D+I)
    G = -D_plus_I_inv@S
    F = D_plus_I_inv@B

    i = 0
    X_prev = np.zeros((n,1))
    while True:
        i += 1
        X_prev[:] = X
        X[:] = G@X + F

        if i == max_i:
            break
        if np.max(np.abs(X-X_prev)) < max_err:
            break

M = np.array([[-6.3, -3.8,  -0.6,  -2.8],
              [ 8.7, 16.5,  -7.4, 124.2],
              [ 9.4, -6.3, -17.4,  68.2]], np.float64)
X = np.array([-2.2, 5.5, -7.1], np.float64)

gauss_seidel(M, X, 5, 0.001)


# Questão 3

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


A = np.array([[-4.4, 8.9,  2.9],
              [-2.5, 0.2, -1.1],
              [ 7.5, 6.1,  5.8]], np.float64)
B1 = np.array([-88.6, 10.6, -109.0], np.float64)
B2 = np.array([ 85.4,  9.6,   19.7], np.float64)

lu(A, B1, B2)


# Questão 4

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

M = np.array([[-3.3, -5.9, 4.4, -29.8],
              [ 8.4,  1.7, 7.2,  31.3],
              [-6.6, -6.0, 1.0, -40.3]], np.float64)

gauss(M)
