#metodos para lista, append, pop, remove, insert

my_list = [1, 2, 3, 4, 5]

print(my_list[2:])

my_list.append(6) #agrega al final
my_list[0] = 'cero'
print(my_list)

my_list.pop() #elimina el ultimo elemento

for element in my_list:
    print(element)

a = [1, 2, 3]
b = a #dos nombres apunta al mismo lugar de memoria
print( id(a),id(b))
print('-----------')

#problema con mutables
c= [a,b]
print(c)
a.append('NUEVO')
print(c)
print(c)#CLONACION DE LISTAS
# casi siempre es mejor clonar una lista

a = [1, 2, 3]
b=a
print(id(a),id(b))
c = list(a) #genera diferentes objetos en memoria

print(id(a),id(b), id(c))

d = a[::] #forma pro de clonar

print('\n List comprehension')
#list comprehension

my_list = list(range(100))
print(my_list)

double = [i*2 for i in my_list]
print(double)

pares = [i for i in my_list if i%2==0]
print(pares)

"""Listas

append: Añade un elemento al final de una lista

sintaxis: lista.append(‘hola’)
clear: Elimina todos los elementos de la lista.

sintaxis: lista.clear()
copy: hace un retorno de los elementos de una lista.

sintaxis: nueva_lista = lista.copy()
count: retorna el numero de elementos de un valor especifico.

sintaxis: list = [1,2,5,1,53,5,3,4,5]; list.count(5) => returned 3
extend: Agrega los elementos de una lista al final de la lista actual.

sintaxis: nueva_lista.extend(list)
index: Devuelve el indice del primer elemento con el valor esfecificado.

sintaxis: list.index(5) => returned 2
insert: Agrega un elemento en una posición especifica.

sintaxis: list.insert(4, 4) => [1,2,5,1,4,53…]
pop: Elimina un elemento de una posición especifica (si no le pasamos nada por parametros, elimina el ultimo elemento de la lista).

sintaxis: list.pop(0) => [2,5,1,4,53…]
remove: Elimina los elementos de un valor espefico.

sintaxis: list.remove(5) => [2,1,4,53,3,4]
reverse: Invierte el orden de la lista

sintaxis: list.reverse() => [4,3,53,4,1,2]
sort: Ordena la lista.

sintaxis: list.sort() => [1,2,3,4,4,53]"""