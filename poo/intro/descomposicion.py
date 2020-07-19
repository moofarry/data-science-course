class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'standby'
        self._motor = Motor(cylinders=4)

    def speedUp(self, type='slowly'):
        if type == 'quick':
            self._motor.injectGasoline(10)
            self._motor.temperature(90)
        else:
            self.motor.injectGasoline(3)
            self._motor.temperature(50)
        self._state = 'movement'


class Motor:

    def __init__(self, cylinders, type='combustion'):
        self.type = type
        self.cylinders = cylinders
        self.temperature = 0

    def injectGasoline(self, quantity):
        pass
