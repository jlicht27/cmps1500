def eat(x):
    x[1] = 9
    x[3] = 11

def prob3():
    food = [4,5,6,7]
    eat(food)
    print('food =', food)

prob3()
