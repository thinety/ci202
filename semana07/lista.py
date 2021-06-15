import numpy as np
np.set_printoptions(precision=6, floatmode='maxprec_equal', suppress=True)


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

M = np.array([[10, 2,  1,  7],
              [ 1, 5,  1, -8],
              [ 2, 3, 10,  6]], np.float64)
X = np.array([0, 0, 0], np.float64)

gauss_seidel(M, X, 10, 0.02)


def relaxacao(M, X, max_i, max_err):
    """
    Resolve um sistema linear pelo método da relaxação

    `M` é a matriz expandida do sistema (formato `(n,n+1)`).
    `X` é o vetor com as aproximações iniciais, que é
    modificado durante o algoritmo.
    """

    n = M.shape[0]
    A = M[:,:-1]
    B = M[:,-1].reshape((n,1))
    X = X.reshape((n,1))

    i = 0
    R = A@X - B
    while True:
        i += 1

        r = np.argmax(np.abs(R))
        x = np.argmax(np.abs(A[r]))
        X[x] = (B[r] + A[r,x]*X[x] - A[r]@X) / A[r,x]

        R = A@X - B

        if i == max_i:
            break
        if np.max(np.abs(R)) < max_err:
            break

M = np.array([[10,   2,  1,  7],
              [ 1, -15,  1, 32],
              [ 2,   3, 10,  6]], np.float64)
X = np.array([0, 0, 0], np.float64)

relaxacao(M, X, 10, 0.1)


# Lista
