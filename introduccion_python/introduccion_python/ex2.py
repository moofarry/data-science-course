usuario_1 = str(input('Ingrese usuario 1: '))
edad_1= int(input('Ingrese edad del usuario 1: '))
usuario_2 = str(input('Ingrese usuario 2: '))
edad_2= int(input('Ingrese edad del usuario 2: '))

if edad_1 > edad_2:
    print(f'{usuario_1} es mayor que {usuario_2}')
elif edad_2 > edad_1:
    print(f'{usuario_2} es mayor que {usuario_1}')
else:
    print('Los dos usuarios tienen la misma edad')