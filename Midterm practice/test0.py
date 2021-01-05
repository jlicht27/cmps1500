def fortyTwo():
    print('42')

def Main():
    n = int(input('Please input an integer: '))
    counter = 0
    while counter != n:
        fortyTwo()
        counter += 1


Main()
