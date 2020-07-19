def morral(tamanoMorral, persos, valores, n):
    if n == 0 or tamanoMorral == 0:
        return 0
    

    if pesos[n - 1] > tamanoMorral:
        return morral(tamanoMorral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamanoMorral - pesos[n - 1], persos, valores,n-1)
               , morral(tamanoMorral, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamanoMorral = 10
    n = len(valores)

    resultado = morral(tamanoMorral, pesos, valores, n)
    print(resultado)
