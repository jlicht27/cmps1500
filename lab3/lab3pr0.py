'''Jonathan Licht
Lab 3 part 0
due 2/10/2020
'''

def add(string, position):
    result = ''
    if int(position) > len(string):
        result = string
    elif int(position) == len(string):
        result = string + '-'
    elif int(position) == 0:
        result = '-' + string
    else:
        result = string[:position] + '-' + string[position:]
    return result     

def delete(string, position):
    result = ''
    if int(position) >= len(string):
        result = string
    if string[position] == '-':
        result = string[0:position] + string[position + 1:]
    else:
        result = string
    return result

def validDNA(string):
    valid_char = 'ACTG'
    result = True
    for i in string:
        if i not in valid_char:
            result = False
    return result       

def fill(string, n):
    result = ''
    if len(string) < n:
        rest = n - len(string)
        result = string + '-'*rest
    else:
        result = string
    return result   

def score(str1, str2):
    num = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            num += 1
    return num
