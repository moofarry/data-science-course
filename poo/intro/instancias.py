class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, coordinate2):
        x_diff = (self.x - coordinate2.x) ** 2
        y_diff = (self.y - coordinate2.y) ** 2

        return (x_diff + y_diff) ** 0.5

if __name__ == '__main__':
    axis1 = Coordinate(3, 30)
    axis2 = Coordinate(4, 40)

    print("asd")
    print(axis1.distance(axis2))
    print(isinstance(axis1,Coordinate)) #si una instancia pertenece a uan clase
