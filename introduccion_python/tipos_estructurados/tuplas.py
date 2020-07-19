#se cuencia inmutables de objetos
my_tuple = ()
type(my_tuple)
my_tuple = (1, 'dos', True)
#print(my_tuple[1])

my_tuple1= (1)
print(type(my_tuple1))
my_tuple1= (1,)
print(type(my_tuple1))

#reaccinando
my_other_tuple = (2,3,4)
my_tuple1 += my_other_tuple
print(my_tuple1)

#reempaquetar

x,y,z = my_other_tuple
print(x,'\n')

def coordenadas():
    return (5,4)

x,y= coordenadas()
print(x,y)