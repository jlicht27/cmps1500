def request():
    num = int(input('Please input an integer: '))
    while num <= 1 or num >= 10:
        num = int(input('Please input an integer: '))
    return num


print(request())
