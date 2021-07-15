def rectangle_rule(f, p, k=0.5):
    """
    Integra uma função utilizando a Regra dos Retângulos Repetida.

    `f` é a função a ser integrada. `p` é a partição do intervalo de integração;
    espera-se que essa partição tenha subintervalos de igual comprimento.
    `k` é um parâmetro que ajusta o ponto amostral; por padrão, `k=0.5` e o ponto
    amostral fica no meio de cada subintervalo.

    Retorna o valor da integração numérica.
    """

    # Como espera-se que `(x_ip1 - x_i)` seja constante, essa soma pode ser
    # realizada mais eficientemente ao colocar esse termo em evidência
    return sum(
        f((1-k)*x_i + k*x_ip1) * (x_ip1 - x_i)
            for x_i, x_ip1
            in zip(p[0:], p[1:])
    )


def trapezoidal_rule(points):
    """
    Integra uma função utilizando a Regra dos Trapézios Repetida.

    `points` é uma lista com os pontos da função a ser integrada. A partição do
    intervalo de integração é obtida por meio desses pontos. Espera-se que essa
    partição tenha subintervalos de igual comprimento.

    Retorna o valor da integração numérica.
    """

    # Espera-se que `(x_ip1 - x_i)` seja constante.
    # Além disso, `y_ip1` aparece também no próximo termo da soma como `y_i`.
    # Utilizando essas informações, é possível obter uma fórmula explícita para a
    # soma abaixo, e assim calculá-la mais eficientemente.
    return sum(
        (y_i + y_ip1) * (x_ip1 - x_i) / 2.0
            for (x_i, y_i), (x_ip1, y_ip1)
            in zip(points[0::1], points[1::1])
    )


def simpsons_rule(points):
    """
    Integra uma função utilizando a Regra de Simpson Repetida.

    `points` é uma lista com os pontos da função a ser integrada. A partição do
    intervalo de integração é obtida por meio desses pontos. Espera-se que essa
    partição tenha subintervalos de igual comprimento, e que contenha um número
    ímpar de pontos (os pontos excedentes são silenciosamente ignorados).

    Retorna o valor da integração numérica.
    """

    # Espera-se que `(x_ip1 - x_i)` seja constante.
    # Além disso, `y_ip1` e `y_ip2` aparecem também no próximo termo da soma como
    # `y_i` e `y_ip1`, respectivamente.
    # Utilizando essas informações, é possível obter uma fórmula explícita para a
    # soma abaixo, e assim calculá-la mais eficientemente.
    return sum(
        (y_i + 4*y_ip1 + y_ip2) * (x_ip1 - x_i) / 3.0
            for (x_i, y_i), (x_ip1, y_ip1), (_, y_ip2)
            in zip(points[0::2], points[1::2], points[2::2])
    )
