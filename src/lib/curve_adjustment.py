from . import linear_systems as _ls


def min_square(points, functions):
    """
    """

    X = [x for (x, _) in points]
    Y = [y for (_, y) in points]
    n = len(points)

    F = functions
    m = len(F)

    M = [[sum(F[j](X[k]) * F[i](X[k]) for k in range(n)) for j in range(m)] + [sum(Y[k] * F[i](X[k]) for k in range(n))] for i in range(m)]
    A = _ls.gauss(M)

    def f(x):
        X = [F[i](x) for i in range(m)]
        return sum(a*x for (a,x) in zip(A,X))

    return f
