import numpy as _np


def cramer(M):
    """
    Resolve um sistema linear pela regra de Cramer.

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).

    Retorna o vetor solução.
    """

    M = _np.array(M)
    n = M.shape[0]
    A = M[:,:-1]
    B = M[:,-1]

    D = _np.linalg.det(A)
    X = _np.zeros(n)
    for i in range(n):
        A_i = _np.copy(A)
        A_i[:,i] = B
        D_i = _np.linalg.det(A_i)
        X[i] = D_i/D

    return X


def gauss(M, piv=True):
    """
    Resolve um sistema linear por eliminação de Gauss.

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).

    `piv` é um booleano que indica se a escolha do melhor pivô
    deve ser realizada em cada passo da triangulação.

    Retorna o vetor solução.
    """

    M = _np.array(M)
    n = M.shape[0]

    # triangulação
    for i in range(n):
        if piv:
            # escolha do pivô
            pivot_row = _np.argmax(_np.abs(M[i:,i])) + i
            M[[i, pivot_row], :] = M[[pivot_row, i], :]

        # zerar elementos abaixo do pivô
        for j in range(i+1, n):
            M[j,:] -= M[j,i]/M[i,i] * M[i,:]

    # retrosubstituição
    X = _np.zeros(n)
    for i in reversed(range(n)):
        X[i] = (M[i,-1] - _np.sum(M[i,i+1:-1] * X[i+1:])) / M[i,i]

    return X


def gauss_jordan(M):
    """
    Resolve um sistema linear pelo método de Gauss-Jordan.

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).

    Retorna o vetor solução.
    """

    M = _np.array(M)
    n = M.shape[0]

    # diagonalização
    for i in range(n):
        # zerar elementos acima e abaixo do pivô
        for j in range(n):
            if j == i:
                continue

            M[j,:] -= M[j,i]/M[i,i] * M[i,:]

    # solução
    X = _np.zeros(n)
    for i in range(n):
        X[i] = M[i,-1] / M[i,i]

    return X


def lu(A, *Bs):
    """
    Resolve `k` sistemas lineares por fatoração LU.

    `A` é a matriz dos coeficientes (`n x n`), e os outros
    `k` parâmetros são os vetores dos termos contantes.

    Retorna os `k` vetores solução.
    """

    A = _np.array(A)
    n = A.shape[0]

    L = _np.diagonal(n)
    U = _np.copy(A)

    # fatoração LU
    for i in range(n):
        for j in range(i+1, n):
            m_ji = U[j,i]/U[i,i]
            L[j,i] = m_ji
            U[j,:] -= m_ji * U[i,:]

    Xs = []
    for B in Bs:
        B = _np.array(B)

        Y = _np.zeros(n)
        for i in range(n):
            Y[i] = (B[i] - _np.sum(L[i,:i] * Y[:i])) / L[i,i]

        X = _np.zeros(n)
        for i in reversed(range(n)):
            X[i] = (Y[i] - _np.sum(U[i,i+1:] * X[i+1:])) / U[i,i]

        Xs.append(X)

    return tuple(Xs)


def gauss_jacobi(M, X, max_i, max_err):
    """
    Resolve um sistema linear pelo método de Gauss-Jacobi

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).
    `X` é o vetor com as aproximações iniciais.

    É necesssário verificar as condições de convergência previamente
    (sistema deve estar na forma diagonalmente dominante).
    """

    M = _np.array(M)
    n = M.shape[0]
    A = M[:,:-1]
    B = M[:,-1].reshape((n,1))
    X = _np.array(X).reshape((n,1))

    D = _np.diagonal(n) * A
    I = _np.tril(A, k=-1)
    S = _np.triu(A, k=1)

    D_inv = _np.linalg.inv(D)
    J = -D_inv@(I+S)
    E = D_inv@B

    i = 0
    X_prev = _np.zeros(n).reshape((n,1))
    while True:
        i += 1
        X_prev[:] = X
        X[:] = J@X + E

        if i == max_i:
            break
        if _np.max(_np.abs(X-X_prev)) < max_err:
            break


def gauss_seidel(M, X, max_i, max_err):
    """
    Resolve um sistema linear pelo método de Gauss-Seidel

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).
    `X` é o vetor com as aproximações iniciais.

    É necesssário verificar as condições de convergência previamente
    (sistema deve satisfazer o critério de Sassenfeld).
    """

    M = _np.array(M)
    n = M.shape[0]
    A = M[:,:-1]
    B = M[:,-1].reshape((n,1))
    X = _np.array(X).reshape((n,1))

    D = _np.diagonal(n) * A
    I = _np.tril(A, k=-1)
    S = _np.triu(A, k=1)

    D_plus_I_inv = _np.linalg.inv(D+I)
    G = -D_plus_I_inv@S
    F = D_plus_I_inv@B

    i = 0
    X_prev = _np.zeros(n).reshape((n,1))
    while True:
        i += 1
        X_prev[:] = X
        X[:] = G@X + F

        if i == max_i:
            break
        if _np.max(_np.abs(X-X_prev)) < max_err:
            break


def relaxation(M, X, max_i, max_err):
    """
    Resolve um sistema linear pelo método da relaxação

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).
    `X` é o vetor com as aproximações iniciais.
    """

    M = _np.array(M)
    n = M.shape[0]
    A = M[:,:-1]
    B = M[:,-1].reshape((n,1))
    X = _np.array(X).reshape((n,1))

    i = 0
    R = A@X - B
    while True:
        i += 1

        r = _np.argmax(_np.abs(R))
        x = _np.argmax(_np.abs(A[r]))
        X[x] = (B[r] + A[r,x]*X[x] - A[r]@X) / A[r,x]

        R = A@X - B

        if i == max_i:
            break
        if _np.max(_np.abs(R)) < max_err:
            break
