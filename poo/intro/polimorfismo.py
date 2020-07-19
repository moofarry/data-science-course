class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    # Definimos el método avanzar.
    def avanza(self):
        print('Ando caminando')


# Ciclista extiende de Persona
class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)


    # Para aplicar polimorfismo en el método de la superclase
    # simplemente definimos su comportamiento y nombrando el método.
    def avanza(self):
        print('Ando moviendome en mi bicicleta')


def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    main()