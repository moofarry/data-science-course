
import random
def orde_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0and lista[posicion_actual-1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual = posicion_actual - 1

        lista[posicion_actual] = valor_actual

    return lista

if __name__=='__main__':
    tamano_de_lista =int(input('Cual va ser el tamano de la lista?: '))
    lista_desordenada = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista_desordenada)
    lista_ordenada = orde_por_insercion(lista_desordenada)
    print(lista_ordenada)