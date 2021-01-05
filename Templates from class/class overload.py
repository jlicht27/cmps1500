from sys import *
​
class Rational:
    def __init__(self, n, d):
      if d == 0:
         print("Invalid Denominator!")
         sys.exit()  # import sys for this to work (ugly!)
      else:
         self.numerator = n
         self.denominator = d
​
    def __str__ (self):
        return str(self.numerator) + "/" + str(self.denominator)
​
    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator
​
    def __add__(self, other):
        newDenominator = self.denominator*other.denominator
        newNumerator = self.numerator*other.denominator + self.denominator*other.numerator
        return Rational(newNumerator, newDenominator)
    def __lt__(self, other):
        newNumerator1 = self.numerator*other.denominator
        newNumerator2 = other.numerator*self.denominator
        if newNumerator1 < newNumerator2:
            return True
        else:
            return False
    def __gt__(self, other):
        newNumerator1 = self.numerator*other.denominator
        newNumerator2 = other.numerator*self.denominator
        if newNumerator1 > newNumerator2:
            return True
        else:
            return False
        
​
​myNum1.__lt__(myNum2)
​
'''Create overloaded functions for > , < ,and + '''
​
​
myNum1 = Rational(1, 3)
myNum2 = Rational(2, 6)
​
if(myNum1 == myNum2):
    print("do something")
            
