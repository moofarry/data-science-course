
import numpy as np



def tirarAgujas(numAgujas):

    adentroCirculo = 0

    for _ in range(numAgujas):
        x = np.random.random() * np.random.choice([-1, 1])
        y = np.random.random() * np.random.choice([-1, 1])
        #print(x, y)

        distanciaDesdeCentro = np.sqrt(x ** 2 + y ** 2)

        if distanciaDesdeCentro <= 1:
            adentroCirculo += 1

    return (4 * adentroCirculo) / numAgujas


def estimacion(numAgujas, numIntentos):
    estimados = []

    for _ in range(numIntentos):
        estimacionPi = tirarAgujas(numAgujas)
        estimados.append(estimacionPi)
        #print(f'Estimados: {estimados}')

    meanEstimada = np.mean(estimados)
    sigma = np.std(estimados)
    print(f' IntentoNum= {numIntentos} Estd= {round(meanEstimada, 5 )}, sigma= {round(sigma, 5)}, agujas= {numAgujas}')

    return (meanEstimada, sigma)

def estimarPI(precision, numIntentos):
    numAgujas = 5
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(numAgujas,numIntentos)
        numAgujas *= 2

    return media

if __name__ == '__main__':


   estimarPI(0.01, 10)



