# Definicion

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self,otherPerson):
        return f'Hello {otherPerson}, my name is  {self.name}.'


#uso
john = Person('John', 35)
valentina = Person('Valentina', 25)

john.greet(valentina)
