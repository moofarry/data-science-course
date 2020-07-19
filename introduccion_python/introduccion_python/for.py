iter('cadena')  # cadena
iter(['a', 'b', 'c'])  # lista
iter(('a', 'b', 'c'))  # tupla
iter({'a', 'b', 'c'})  # conjunto
iter({'a': 1, 'b': 2, 'c': 3})  # diccionario

print('------------')

meses = {
    'enero': 'january',
    'febrero': 'february',
    'marzo': 'march',
    'abril': 'april',
    'mayo': 'may',

}

estudiantes = {
    'mexico':10,
    'colombia':15,
    'puerto_rico':4,
}

arr=[1,2,3]

acc= iter(arr)
print(next(acc))
print(next(acc))
print(next(acc))


for mes in meses.keys():
    print(f'------')
    print(mes)

for mes in meses.values():
    print(f'------')
    print(mes)

for ex in estudiantes.keys():
    print(ex)
for ex in estudiantes.values():
    print(ex)
for ex in estudiantes.items():
    print(ex)
