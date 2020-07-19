#secuencia de enteros
# range(comienzo, fin , pasos)

my_range = range(0, 7,2)
my_other_range = range (0, 8, 2)
print(type(my_range))
print('-----')
x= my_range == my_other_range

for i in my_range:
    print(i)
print('-----')
for i in my_other_range:
    print(i)
print('-----')
print(my_range is my_other_range)
print('-----')

for i in range(0, 101, 2):
    print(i)
print('-----')
for i in range(1, 100, 2):
    print(i)
print('-----')