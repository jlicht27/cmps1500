
def rolldie():
    import random
    num1 = random.randrange(1,6)
    num2 = random.randrange(1,6)
    result = [num1, num2]
    return result


print(rolldie())
