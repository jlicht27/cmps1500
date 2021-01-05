string = 'qwertyuiop'

def find(s):
    letter = input('Please input character: ')
    if letter in string:
        return s.index(letter)
    else:
        return -1


print(find(string))
