base = int(input('Insira uma base (entre 2 e 9): '))

while True:
    number = int(input('Insira um número inteiro positivo para converter: '))

    digits = []
    aux = number
    while aux > 0:
        digits.append(aux % base)
        aux = aux // base

    number_string = ''.join(str(digit) for digit in reversed(digits))

    print(f'{number}_10 = {number_string}_{base}')
