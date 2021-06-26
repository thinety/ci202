def bisection(f, a, b, max_size, max_i):
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


def false_position(f, a, b, max_size, max_i):
    print(f'i = 0, a = {a:.6f}, b = {b:.6f}')
    i = 0
    while True:
        i += 1
        x_i = (a*f(b) - b*f(a))/(f(b) - f(a))
        if f(a) * f(x_i) > 0:
            a = x_i
        else:
            b = x_i

        print(f'i = {i}, a = {a:.6f}, b = {b:.6f}')

        if (b-a) < max_size:
            break
        if i == max_i:
            break


def linear_iteration(g, x_0, i):
    print(f'x_0 = {x_0:.6f}')

    x_i = x_0
    for i in range(1, i+1):
        x_i = g(x_i)

        print(f'x_{i} = {x_i:.6f}')


def newton_raphson(f, f_prime, x_0, max_diff = 0.0001, max_err = 0.0001, max_i = 5):
    print(f'x_0 = {x_0:.6f}')

    i = 0
    x_i = x_0
    while True:
        i += 1
        x_im1 = x_i
        x_i = x_i - f(x_i)/f_prime(x_i)

        print(f'x_{i} = {x_i:.6f}')

        if abs(x_i - x_im1) < max_diff:
            break
        if abs(f(x_i)) < max_err:
            break
        if i == max_i:
            break


def secant(f, x_0, x_1, max_diff = 0.0001, max_err = 0.0001, max_i = 6):
    print(f'x_0 = {x_0:.6f}')
    print(f'x_1 = {x_1:.6f}')

    i = 1
    x_im1, x_i = x_0, x_1
    while True:
        i += 1
        x_im1, x_i = x_i, (x_im1*f(x_i) - x_i*f(x_im1))/(f(x_i) - f(x_im1))

        print(f'x_{i} = {x_i:.6f}')

        if abs(x_i - x_im1) < max_diff:
            break
        if abs(f(x_i)) < max_err:
            break
        if i == max_i:
            break


def mixed(f, f_prime, a, b, x_0, max_err = 0.0001, max_i = 5):
    print(f'x_0 = {x_0:.6f}')

    i = 0
    x_i_F = x_0
    while True:
        i += 1

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

        print(f'x_{i}^N = {x_i_N:.6f}')
        print(f'x_{i}^F = {x_i_F:.6f}')

        if abs(x_i_F - x_i_N) < max_err:
            break
        if i == max_i:
            break

    root = (x_i_F + x_i_N) / 2
    print(f'raiz: {root:.6f}')
