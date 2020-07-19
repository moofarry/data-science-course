my_dict = {
    'david' : 35,
    'erika' : 32,
    'jaime' : 50,
}

my_dict['david']
my_dict.get('juan', 111) #sino existe me pasa el valor 111
my_dict['jaime'] = 20 #modificar un sisas
my_dict['pedro'] = 70 #agregar

del my_dict['jaime'] #eliminar

for llaves in my_dict.keys():
    print(llaves)

for valor in my_dict.values():
    print(valor)


for llave, valor in my_dict.items():
    print( llave , valor)

print('---')
existe = 'david' in my_dict #verifica si existe una lalve en dict
print(existe)
existe = 'jorge' in my_dict
print(existe)

print('--------------')

#dict_variable = {key:valuefor (key,value) in dictonary.items()}

d_elements = {
  'element1': 1,
  'element2': 2,
  'element3': 3,
  'element4': 4,
  'element5': 5,
}

d_elements_double = {k:v*2 for k,v in d_elements.items()}

print(d_elements)
print(d_elements_double)