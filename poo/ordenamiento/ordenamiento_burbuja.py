import random


def burbuja(lista):

    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


if __name__ == '__main__':
    tamanoLista = int(input('De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamanoLista)]
    print(lista)

    listaOrdenada = burbuja(lista)
    print(listaOrdenada)
