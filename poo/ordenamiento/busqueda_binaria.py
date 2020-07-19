import random


def busquedaBinaria(lista,comienzo,final,objetivo,contador):
    contador += 1
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]} y contador va en {contador}')
    if comienzo>final:
        return False
    medio = (comienzo+final) // 2   #division enteros

    if lista[medio] == objetivo:
        return True
    elif lista[medio]< objetivo:
        return busquedaBinaria(lista, medio+1 , final, objetivo,contador)
    else:
        return busquedaBinaria(lista,comienzo,medio-1,objetivo,contador)


if __name__ == '__main__':
    tamanoLista = int ( input ('De que tamano es la lista? '))
    objetivo = int( input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0,100) for i in range(tamanoLista)])
    contador = 0
    encontrado = busquedaBinaria(lista,0, len(lista),objetivo,contador)


    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')