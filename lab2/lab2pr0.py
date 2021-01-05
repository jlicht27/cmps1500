'''Jonathan Licht
   Lab 2 part 0
   Due Monday 2/3/20 at 11:59 p.m.
'''

password = input('Please enter a phrase: ')
punc = '.,?!;:"'

result = password[0]
result1 = ''

for i in range(len(password)):
    if password[i] == ' ' and i != len(password) - 1:
        result = result + password[i + 1]
        if i == 0:
            result = result + password[i]
    if password[i] in punc:
        result += password[i]
        

for i in result:
    if i == 'o':
        result1 += '0'
    elif i == 'a':
        result1 += '@'
    elif i == 'l':
        result1 += '1'
    else:
        result1 += i


        

print(result1)
