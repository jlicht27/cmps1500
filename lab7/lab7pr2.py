'''Jonathan Licht
Lab 7 part 2'''


from milclock import *


class MilClock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        if self.hours < 10:
            if self.minutes < 10:
                return '0' + str(self.hours) + ':' + '0' + str(self.minutes)
            else:
                return '0' + str(self.hours) + ':' + str(self.minutes)
        if self.minutes < 10:
            return str(self.hours) + ':' + '0' + str(self.minutes)
        else:
            return str(self.hours) + ':' + str(self.minutes)

    def addOne(self):
        if self.minutes == 59:
            if self.hours == 23:
                self.hours = 0
                self.minutes = 0
            else:
                self.minutes = 0
                self.hours += 1
        else:
            self.minutes += 1
        
def addMinutes(clock, n):
    ''' add n minutes to the clock '''

    for x in range(n):
        clock.addOne()
        
hallClock = MilClock(5,0)
print('We wake up at', hallClock)
addMinutes(hallClock, 30)
print('We get up at', hallClock)
addMinutes(hallClock, 40)
print('We are sleepy again by', hallClock)



wristWatch = MilClock(23,0)
print('Last tram leaves at', wristWatch)
addMinutes(wristWatch,59)
print('Today ends at', wristWatch)
wristWatch.addOne()
print('Tomorrow starts at', wristWatch)
