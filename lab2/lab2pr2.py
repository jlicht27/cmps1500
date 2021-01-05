'''Jonathan Licht
    lab 2 part 2
    due Moday 2 at 11:59
'''

password_list = []
censored_list = []

password = 'anything'

while password != '':
    password = input('Please enter a password (press [enter] to finish): ')
    password_list.append(password)
    censored_list.append(len(password) * '*')
    password_list[0:-1]
    censored_list[0:-1]

print(password_list[0:-1])
print(censored_list[0:-1])


