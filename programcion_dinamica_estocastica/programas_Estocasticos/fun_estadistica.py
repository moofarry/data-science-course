import random
import  numpy as np

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)
    acumulador = 0
    for x in X:
        acumulador += (x-mu)**2
    return acumulador /len(X)

def desviacionEstandar(X):
    return np.sqrt(varianza(X))

if __name__ == '__main__':

    X = [random.randint(9,12) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacionEstandar(X)

    print(f'Arreglo X: {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviacion Estandar = {sigma}')
sáb.,  4 de jul. de 2020 03:29:40 a. m.
