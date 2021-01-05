def dog(x):
    print('in dog, x is', x)
    y = cat(x - 1) + cat(x + 2)
    print('in dog, y is', y)
    return y
def cat(y):
    print('in cat, y is', y)
    x = rat(y*2) + 3
    print('in cat, x is', x)
    return x
def rat(x):
    print('in rat, x is', x)
    return 2 * x
print('in main')
y = dog(3)
print('in main, y is', y)
    
