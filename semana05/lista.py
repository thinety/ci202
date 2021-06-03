import numpy as np


# Questão 1

def gauss(M: np.ndarray, piv):
    m = M.shape[0]

    # triangulação
    for i in range(m):
        if piv:
            # escolha do pivô
            pivot_row = np.argmax(np.abs(M[i:, i])) + i
            M[[i, pivot_row], :] = M[[pivot_row, i], :]

        # zerar elementos abaixo do pivô
        for j in range(i+1, m):
            M[j,:] -= M[j,i]/M[i,i] * M[i,:]

    # retrosubstituição
    x = np.zeros(m)
    for i in reversed(range(m)):
        x[i] = (M[i,-1] - np.sum(M[i, i+1:-1] * x[i+1:])) / M[i,i]

    # imprimir resultados
    with np.printoptions(formatter={'float': '{:12.6f}'.format}):
        print(M)
    for i in range(m):
        print(f'x_{i+1} = {x[i]:12.6f}')

M = np.array([[-8.4, -0.7, -5.9, -8.1, -10.4],
              [-4, -4.2, -6.2, 8.9, 167.5],
              [-1.1, 9.6, 6.2, 4.2, -88.9],
              [-7.6, 0.3, -8.6, -3.9, 42.4]], dtype=np.float64)

gauss(M, False)

# Questão 3

M = np.array([[-3, -1.3, 7.6, -3.5, -69.7],
              [7, -3.8, 5.1, -7.7, 40],
              [4.6, -9.1, 8.7, 6.9, 69.1],
              [3, 5.2, -6.3, -9.7, 3.1]], dtype=np.float64)

gauss(M, True)


# Questão 2

def gauss_jordan(M: np.ndarray):
    m = M.shape[0]

    # diagonalização
    for i in range(m):
        # zerar elementos acima e abaixo do pivô
        for j in range(m):
            if j == i:
                continue

            M[j,:] -= M[j,i]/M[i,i] * M[i,:]

    # imprimir resultados
    with np.printoptions(formatter={'float': '{:12.6f}'.format}):
        print(M)
    for i in range(m):
        x_i = M[i, -1]/M[i,i]
        print(f'x_{i+1} = {x_i:12.6f}')

M = np.array([[-5.1, 7.4, 1.5, -56.5],
              [-0.6, -2.6, 6.8, -37.8],
              [-3.5, 0.1, 9, -71.4]], dtype=np.float64)

gauss_jordan(M)

# Questão 4

M = np.array([[-1.9, 2.7, -0.8, -4.6, 25.6],
              [-2.5, 8.1, 2.2, 3.4, 45.6],
              [-8.3, 8.5, -5.5, 3.8, 165.1],
              [-5.2, -4.5, 4.5, 0.9, -5.1]], dtype=np.float64)

gauss_jordan(M)
