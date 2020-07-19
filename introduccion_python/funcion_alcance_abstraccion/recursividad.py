def factorial(n):
    """
    Calcula el factorial de n.
    :param n: un entero >0
    :return: n!
    """
    print(f'El numero elegido es {n}')

    if n == 1:
        return 1

    return n * factorial(n-1)

n = int(input('Escribe un entero: '))
print('El factorial de ', n , ' es ', factorial(n))
