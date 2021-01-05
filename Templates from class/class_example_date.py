class Date:
    """ A blueprint (class) for objects that represent calendar
        days
    """
    
    def __init__(self, m, d, y):
        """ the Date constructor """
        self.month = m
        self.day   = d
        self.year  = y
​
    def __str__(self):
        """ Print the date """
        s = str(self.month) + "/" + str(self.day)  + "/" + str(self.year)
        return s
	 
    def setMonth(self, newm):
        """Sets the month value """
        self.month = newm
        return 
		
    def isLeapYear(self):
        """ Returns true if the year is a Gregorian leap year """
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        return self.year % 4 == 0

    
​
​
​
#usage
d1 = Date(3,30,2011)
print(d1)
d2 = Date(3,30,2011)
d3 = Date(3,4,2015)
​
leap = d1.isLeapYear()
print(leap)
Collapse

















Message #lectures


