class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

#build first product from factory
#point1 -> x = 5, y = 10
point1 = Point(5, 10)
#build seccond product from factory
#point2 -> x = 1, y = 2
point2 = Point(1, 2)

print(point1.getX())
print(point2.getX())
