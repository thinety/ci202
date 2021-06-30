import numpy as _np
from . import linear_systems as _ls


def polynomial(points):
    """
    """

    n = points.shape[0]

    M = _np.array([[points[i,0]**j for j in range(n)] + [points[i,1]] for i in range(n)])
    A = _ls.gauss(M)

    def f(x):
        X = _np.array([x**i for i in range(n)])
        s = _np.sum(A*X)
        return s

    return f


def lagrange(points, x):
    """
    """

    n = points.shape[0]

    P_nm1 = 0
    for i in range(n):

        L_i = 1
        for j in range(n):
            if j == i:
                continue
            L_i *= (x - points[j,0]) / (points[i,0] - points[j,0])

        P_nm1 += points[i,1] * L_i

    return P_nm1
