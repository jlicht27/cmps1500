


def remove(x,s):
    if s == '':
        return s
    else:
        if s[0] == x:
            return remove(x, s[1:])
        else:
            return s[0] + remove(x, s[1:])

print(remove('t', 'wait a minute'))
