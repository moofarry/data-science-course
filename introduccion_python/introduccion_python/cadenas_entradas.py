#CADENAS
print('123')
print('123' * 3)
print('123' + '456')
print('hip' * 3 + ' ' + 'hurra')
print(f'{"hip" * 3} hurra')

# string
my_str = 'cadena'#Se declara una cadena
len(my_str)
#Acceder a un elemento en particular
my_str[0]
my_str[1]
my_str[2]
#my_str[comienzo:final:pasos]
print(my_str[2:])
print(my_str[:3])

print(my_str[:-2]) #tomo todos ,menos los ultimos 2
print(my_str[::2]) # para hacer saltos de 2 en 2
print("\n")
#ENTRADAS

nombre= input('cual es tu nombre? : ')
print(f'tu nombre es {nombre}')
print((type(nombre)))


numero= int(input('Escribe un numero. '))
print((type(numero)))

#genera un proigrama donde reciba el nombre de usuario y le de un saludo y nos diga la longitud de la cadena