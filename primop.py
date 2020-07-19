from sys import stdin


def is_number_prime(input):


    try:
        entero = int(input)
        pass
    except ValueError:
        print("NO_ES_PRIMO")


    if int(input) <= 1:
        return print("NO_ES_PRIMO")
    elif int(input) == 2:
        return print("PRIMO")
    else:
        for i in range(2, int(input)):
            if int(input) % i == 0:
                return print("NO_ES_PRIMO")
        return print("PRIMO")



# tener cuidado en python con los newlines

numero = input("el numero: ")
is_number_prime(numero)