#raiz cuadrada por enumeracion exahustiva
objetivo = int (input('Escoge un numero entero: '))

respuesta=0

while respuesta**2 < objetivo:
    respuesta +=1
    print(respuesta)

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')