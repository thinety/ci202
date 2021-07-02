import numpy as _np
from . import linear_systems as _ls


def polynomial(points):
    """
    """

    points = _np.array(points)
    X = points[:,0]
    Y = points[:,1]
    n = points.shape[0]

    M = _np.array([[X[i]**j for j in range(n)] + [Y[i]] for i in range(n)])
    A = _ls.gauss(M)

    def f(x):
        X = _np.array([x**i for i in range(n)])
        return _np.sum(A*X)

    return f


def lagrange(points):
    """
    """

    points = _np.array(points)
    X = points[:,0]
    Y = points[:,1]
    n = points.shape[0]

    def f(x):
        P_nm1 = 0
        for i in range(n):
            L_i = 1
            for j in range(n):
                if j == i:
                    continue
                L_i *= (x - X[j]) / (X[i] - X[j])
            P_nm1 += Y[i] * L_i
        return P_nm1

    return f


def newton(points):
    """
    """

    points = _np.array(points)
    X = points[:,0]
    Y = points[:,1]
    n = points.shape[0]

    A = _np.zeros(n)
    O_i = Y
    A[0] = O_i[0]
    for i in range(1, n):
        O_i = _np.array([(O_i[j+1] - O_i[j]) / (X[j+i] - X[j]) for j in range(n-i)])
        A[i] = O_i[0]

    def f(x):
        P_nm1 = 0
        for i in range(n):
            N_i = 1
            for j in range(i):
                N_i *= (x - X[j])
            P_nm1 += A[i] * N_i
        return P_nm1

    return f


def gregory_newton(points):
    """
    """

    points = _np.array(points)
    X = points[:,0]
    Y = points[:,1]
    n = points.shape[0]
    h = X[1] - X[0]

    A = _np.zeros(n)
    O_i = Y
    A[0] = O_i[0]
    for i in range(1, n):
        O_i = _np.array([O_i[j+1] - O_i[j] for j in range(n-i)])
        A[i] = O_i[0]

    def f(x):
        P_nm1 = 0
        for i in range(n):
            N_i = 1
            for j in range(i):
                N_i *= (x - X[j])
            P_nm1 += A[i]/(_np.math.factorial(i) * h**i) * N_i
        return P_nm1

    return f
