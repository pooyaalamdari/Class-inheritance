class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return f'Point: ({self.x},{self.y})'

    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x,
                     self.y + otherPoint.y)

#self
p1 = Point(-5,10)
#otherPoint
p2 = Point(15,20)

#self.x = -5 and otherPoint.x = 15
#self.y = 10 and otherPoint.y = 20

#print(self + otherpoint)
print(p1 + p2)
