import numpy as np
np.set_printoptions(precision=4, floatmode='maxprec_equal', suppress=True)


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

# Questão 1

# M = np.array([[16.1,   2.8,  2.7,  9.9,  -26.5],
#               [ 1.0,   8.2, -4.9, 15.4,  236.0],
#               [ 8.7, -19.1, -3.2, -6.2, -269.3],
#               [ 8.6,   9.0, 23.8, -6.0, -187.3]], np.float64)
M = np.array([[16.1,   2.8,  2.7,  9.9,  -26.5],
              [ 8.7, -19.1, -3.2, -6.2, -269.3],
              [ 8.6,   9.0, 23.8, -6.0, -187.3],
              [ 1.0,   8.2, -4.9, 15.4,  236.0]], np.float64)
X = np.array([-8.1, 8.2, -5.6, 9.7], np.float64)

gauss_seidel(M, X, 5, 0.001)

# Questão 4

M = np.array([[14.1, -2.8,  9.5, 135.1],
              [-2.6, -4.6,  0.1,  15.4],
              [ 2.1,  6.0, -9.0, -32.0]], np.float64)
X = np.array([7.9, -7.8, 0.2], np.float64)

gauss_seidel(M, X, 5, 0.001)

# Questão 2

M = np.array([[-0.5, -2.3,  1.7,  8.0,  73.4],
              [ 1.8, -2.6, -5.3,  5.9, -32.1],
              [-7.7, -3.9, -7.0,  3.7,   7.3],
              [-3.7,  8.1,  6.7, -1.5, 123.8]], np.float64)
X = np.array([-8.4, 4.9, 9.7, 8], np.float64)

relaxacao(M, X, 6, 0.01)

# Questão 3

M = np.array([[-2.3, -5.4, -9.8, -83.7],
              [-2.7,  6.7, -5.5, -74.8],
              [ 6.8,  1.6,  0.6,  56.2]], np.float64)
X = np.array([8, -1.7, 7.6], np.float64)

relaxacao(M, X, 6, 0.01)
