'''Jonathan Licht
    Lab 2 part 1
    due Monday 2/3/2020 at 11:59
'''

special_char = '!?.,;:$#_&'
lower_case = 'qwertyuiopasdfghjklzxcvbnm'
upper_case = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
is_valid = False
sc_valid = False
lc_valid = False
uc_valid = False
num_valid = False
space_valid = False
len_valid = False

while is_valid is False:
    password = input('Please enter a password:\n')
    for i in password:
        if i in special_char:
            sc_valid = True
        if i in lower_case:
            lc_valid = True
        if i in upper_case:
            uc_valid = True
        if i in numbers:
            num_valid = True
        if ' ' not in password:
            space_valid = True
        if len(password) >= 8 and len(password) <= 20:
            len_valid = True
    if sc_valid and lc_valid and uc_valid and num_valid and space_valid and len_valid:
        is_valid = True
    else:
        sc_valid = lc_valid = uc_valid = num_valid = space_valid = len_valid = False



print('Password accepted')
