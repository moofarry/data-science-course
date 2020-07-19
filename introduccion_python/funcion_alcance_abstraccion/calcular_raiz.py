


def calcularRaiz(num, algoritmo):

    if algoritmo == 0:
        print('\nEscogiste metodo "Aproximacion"')
        paso = epsilon ** 2
        respuesta0 = 0.0

        while abs(respuesta0 ** 2 - num) >= epsilon and respuesta0 <= num:
            respuesta0 += paso
        if abs(respuesta0 ** 2 - num) >= epsilon:
            print(f'No se encontro la raiz cuadrada  {num}')
        else:
            print(f'La raiz cuadrada de {num} es {respuesta0}')

    elif algoritmo == 1:
        print('\nEscogiste metodo "Enumeracion"')
        respuesta1 = 0

        while respuesta1 ** 2 < num:
            respuesta1 += 1

        if respuesta1 ** 2 == num:
            print(f'La raiz cuadrada de {num} es {respuesta1}')
        else:
            print(f'{num} no tiene una raiz cuadrada exacta')

    elif algoritmo == 2:
        print('\nEscogiste metodo "Binaria"')

        bajo = 0.0
        alto = max(1.0, num)
        respuesta2 = (alto + bajo) / 2

        while abs(respuesta2 ** 2 - num) >= epsilon:
            if respuesta2 ** 2 < num:
                bajo = respuesta2
            else:
                alto = respuesta2
            respuesta2 = (alto + bajo) / 2

        print(f'La raiz cuadrada de {num} es {respuesta2}')

    else:
        print('\nOpcion no valida\n')

def menu():
    print('\nAlgoritmos para calcular raices cuadradas, escoge un metodo segun su indicador')
    print('0. Aproximacion')
    print('1. Enumeracion')
    print('2. Binaria\n')
    algoritmo = int(input('Escoge un metodo: '))
    num = int(input('Escoge un numero: '))

    return algoritmo, num


epsilon = 0.01
algoritmo, num = menu()
calcularRaiz(num, algoritmo)
