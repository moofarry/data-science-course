import sys

def fibonacciRecursivo(n):
    if n == 0 or n==1:
        return 1

    return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

def fibonacciDinamico(n, memo={}):
    if n== 0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacciDinamico(n-1,memo) + fibonacciDinamico(n-2,memo)
        memo[n] = resultado
        return  resultado


if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int ( input('Escoge un numero: '))
    resultado = fibonacciDinamico(n)
    print(resultado)
    #Process finished with exit code -1073741571 (0xC00000FD)