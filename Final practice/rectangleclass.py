
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return str('width: ' + str(self.width) + ' ' + 'height: ' + str(self.height))

    def area(self):
        area = self.width * self.height
        return area
    
    def equals(self, other):
        if self.width == other.width:
            if self.height == other.height:
                return True
        return False
        
    def isSquare(self):
        return self.height == self.width

def main():
    rect1 = Rectangle(3,4)
    rect2 = Rectangle(6,6)
    rect3 = Rectangle(3,4)
    print('rect1: ', rect1, 'area: ', rect1.area())
    print('rect2: ', rect2, 'area: ', rect2.area())
    print('rect3: ', rect3, 'area: ', rect3.area())
    a = rect1.equals(rect2)
    if a == True:
        print('rect1 and rect2 are equal')
    else:
        print('rect1 and rect2 are not equal')
    b = rect1.isSquare()
    if b == True:
        print('rect1 is a square')
    else:
        print('rect1 is not a square')








        
