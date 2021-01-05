import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def overlap(self, other):
        dist = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        comb_rad = self.radius + other.radius
        if dist >= comb_rad:
            return 'These two circles don\'t overlap'
        else:
            return 'These two circles overlap'



circle1 = Circle(-1,0,2)
circle2 = Circle(3,0,3)

print(circle1.overlap(circle2))

circle3 = Circle(0,0,2)
circle4 = Circle(6,0,3)

print(circle3.overlap(circle4))
