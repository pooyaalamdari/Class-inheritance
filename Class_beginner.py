class Point():
    def getX(self):
        return self.x

#build first product from factory
point1 = Point()
#build seccond product from factory
point2 = Point()

# point1 -> [x=5]
point1.x = 5
#point2 -> [x=10]
point2.x = 10

print(point1.getX())

#point1 -> self
#getX -> return self.x -> return point1.x -> 5

print(point2.getX())
