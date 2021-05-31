from math import cos, exp


# Questão 1

def bissecao(f, a, b, max_size, max_i):
    print(f'i = 0, a = {a:.6f}, b = {b:.6f}')

    i = 0
    while True:
        i += 1

        x_i = (a+b)/2
        if f(a) * f(x_i) > 0:
            a = x_i
        else:
            b = x_i

        print(f'i = {i}, a = {a:.6f}, b = {b:.6f}')

        if (b-a) < max_size:
            break
        if i == max_i:
            break

def f(x):
    return -16*cos(-2*x) + 13*x**2 - 267.69

bissecao(f, 2, 12, 1, 6)


# Questão 2

def newton_raphson(f, f_prime, x_0, max_diff, max_err, max_i):
    print(f'x_0 = {x_0:.6f}')

    i = 0
    x_i = x_0
    while True:
        i += 1

        x_im1 = x_i # x_{i-1}
        x_i = x_i - f(x_i)/f_prime(x_i)

        print(f'x_{i} = {x_i:.6f}')

        if abs(x_i - x_im1) < max_diff:
            break
        if abs(f(x_i)) < max_err:
            break
        if i == max_i:
            break

def f(x):
    return 19*x**-3 - 4*x**3 + 93.79
def f_prime(x):
    return -57*x**-4 - 12*x**2

newton_raphson(f, f_prime, 2, 0.0001, 0.0001, 5)


# Questão 3

def secante(f, x_0, x_1, max_diff, max_err, max_i):
    print(f'x_0 = {x_0:.6f}')
    print(f'x_1 = {x_1:.6f}')

    i = 1
    x_im1, x_i = x_0, x_1
    while True:
        i +=1

        # assignment feito em tuple para não precisar de variável temporária
        x_im1, x_i = x_i, x_i - f(x_i) * (x_i-x_im1)/(f(x_i)-f(x_im1))

        print(f'x_{i} = {x_i:.6f}')

        if abs(x_i - x_im1) < max_diff:
            break
        if abs(f(x_i)) < max_err:
            break
        if i == max_i:
            break

def f(x):
    return 13*exp(2*x) - 15*x**-1 - 1913.62

# 5 iterações no método da secante significa calcular até x_6
# já que começamos com tanto x_0 como x_1
secante(f, 2, 3, 0.01, 0.01, 6)
