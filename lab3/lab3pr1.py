'''Jonathan Licht
lab 3 part 1
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


options = ''
str1 = input('Please enter the first \'biological\' string: \n')
str2 = input('Please enter the second \'biological\' string: \n')
while options != 'q':
    print('String 1:', str1)
    print('String 2:', str2)
    options = input('Select one of the following commands:\n\'a\' to add an indel\n\'d\' to delete an indel\n\'s\' to score the present alignment\n\'q\' to quit the program\n')
    if options == 'a':
        input1 = input('Work on which string (1 or 2):')
        input2 = input('Enter the position of the indel:')
        if input1 == '1':
            str1 = add(str1,int(input2))
            print('Here\'s the result:', str1)
        if input1 == '2':
            str2 = add(str2,int(input2))
            print('Here\'s the result:', str2)
    if options == 'd':
        input1 = input('Work on which string (1 or 2):')
        input2 = input('Enter the position of the indel:')
        if input1 == '1':
            str1 = delete(str1,int(input2))
            print('Here\'s the result:', str1)
        if input1 == '2':
            str2 = delete(str2,int(input2))
            print('Here\'s the result:', str2)
    if options == 's':
        print('There are', (score(str1,str2)), 'matches')

print('Bye!')











    


