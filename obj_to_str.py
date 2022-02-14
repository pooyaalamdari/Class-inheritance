class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return f'Point ({self.x}, {self.y})'

p = Point(7,6)
#if we run p as result we get this
#<__main__.Point object at 0x10d197c10>
print(p)

p2 = Point(-1,4)
print(p2)
