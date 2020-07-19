# Creamos la clase Rectangulo
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


# La clase Cuadrado extiende de Rectangulo, esto significa
# que todas las propiedades y métodos de Rectangulo
# las heredara Cuadrado.
class Cuadrado(Rectangulo):

    # Inicia una instacia de Cuadrado, pero las propiedades
    # de Rectangulo las inicializa con super().__init__(params)
    def __init__(self, lado):
        super().__init__(lado, lado)



if __name__ == '__main__':
    rectangulo = Rectangulo(3,4)
    print(f'El area del rectangulo es {rectangulo.area()}')

    cuadrado = Cuadrado(5)
    print(f'El area del cuadrado es {cuadrado.area()}')