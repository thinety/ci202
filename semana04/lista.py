from math import sin, cos, exp, log


# Questão 1

def iteracao_linear(g, x_0, i):
    print(f'x_0 = {x_0:.6f}')

    x_i = x_0
    for i in range(1, i+1):
        x_i = g(x_i)

        print(f'x_{i} = {x_i:.6f}')

def f(x):
    return 7*sin(2*x) + 7*x**-2 - 2*exp(-2*x) + 322.95
def g(x):
    return -0.5*log(3.5*sin(2*x) + 3.5*x**-2 + 161.475)

iteracao_linear(g, -2, 4)

# Questão 4

def f(x):
    return 11*cos(3*x) - 19*sin(3*x) + log(x) - 5.05
def g(x):
    return exp(19*sin(3*x) - 11*cos(3*x) + 5.05)

iteracao_linear(g, 0, 4)


# Questão 5

def newton_raphson(f, f_prime, x_0, max_diff = 0.0001, max_err = 0.0001, max_i = 5):
    print(f'x_0 = {x_0:.6f}')

    x_i = x_0
    i = 0
    while True:
        x_im1 = x_i
        x_i = x_i - f(x_i)/f_prime(x_i)
        i += 1

        print(f'x_{i} = {x_i:.6f}')

        if abs(x_i - x_im1) < max_diff:
            break
        if abs(f(x_i)) < max_err:
            break
        if i == max_i:
            break

def f(x):
    return 15*x**-0.5 + 20*x**-2 - 23.43
def f_prime(x):
    return -7.5*x**-1.5 - 40*x**-3

newton_raphson(f, f_prime, 1)

# Questão 8

def f(x):
    return -11*exp(x) - 8*x**-1 + 393.85
def f_prime(x):
    return -11*exp(x) + 8*x**-2

newton_raphson(f, f_prime, 3)


# Questão 3

def secante(f, x_0, x_1, max_diff = 0.0001, max_err = 0.0001, max_i = 6):
    print(f'x_0 = {x_0:.6f}')
    print(f'x_1 = {x_1:.6f}')

    x_im1, x_i = x_0, x_1
    i = 1
    while True:
        x_im1, x_i = x_i, (x_im1*f(x_i) - x_i*f(x_im1))/(f(x_i) - f(x_im1))
        i += 1

        print(f'x_{i} = {x_i:.6f}')

        if abs(x_i - x_im1) < max_diff:
            break
        if abs(f(x_i)) < max_err:
            break
        if i == max_i:
            break

def f(x):
    return 13*log(x**-2) - 17*exp(2*x) + 25192.37

secante(f, 3, 4, 0.01, 10)

# Questão 7

def f(x):
    return 14*x**3 - x**-1 - 1391.12

secante(f, 4, 5)


# Questão 2

def misto(f, f_prime, a, b, x_0, max_err = 0.0001, max_i = 5):
    print(f'x_0 = {x_0:.6f}')

    x_i_F = x_0
    i = 0
    while True:
        x_i_N = x_i_F - f(x_i_F)/f_prime(x_i_F)

        if f(a) * f(x_i_N) > 0:
            a = x_i_N
        else:
            b = x_i_N

        x_i_F = (a*f(b) - b*f(a))/(f(b) - f(a))

        if f(a) * f(x_i_F) > 0:
            a = x_i_F
        else:
            b = x_i_F

        i += 1

        print(f'x_{i}^N = {x_i_N:.6f}')
        print(f'x_{i}^F = {x_i_F:.6f}')

        if abs(x_i_F - x_i_N) < max_err:
            break
        if i == max_i:
            break

    root = (x_i_F + x_i_N) / 2
    print(f'raiz: {root:.6f}')

def f(x):
    return - 5*x**-0.5 - 17*exp(x) + 857.13
def f_prime(x):
    return 2.5*x**-1.5 - 17*exp(x)

misto(f, f_prime, 3, 9, 9)

# Questão 6

def f(x):
    return x**2 + 14*cos(2*x) - 10.69
def f_prime(x):
    return 2*x - 28*sin(2*x)

misto(f, f_prime, -4, -1, -4)
