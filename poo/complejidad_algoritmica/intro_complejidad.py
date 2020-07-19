import time

def factorial(n):
    respusta = 1
    while n>1:
        respusta *= n
        n -= 1
    return respusta

def factorialRecursivo(n):
    if n == 1:
        return  1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorialRecursivo(n)
    final = time.time()
    print(final - comienzo)