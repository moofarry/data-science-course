import random

def busqueLineal(lista,objetivo):
    match = False
    for elemento in lista:  #O(n)
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    tamanoLista = int ( input('Tamano de la lista? '))
    objetivo = int (input('Que numero quieres encontrar? '))

    lista = [random.randint(0,100) for i in range(tamanoLista)]
    print(lista)
    encontrado = busqueLineal(lista,objetivo)

    print(f'el elemento {objetivo},  {"esta" if encontrado else "no esta"} en la lista')