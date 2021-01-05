'''Jonathan Licht
Question 2 on final'''


my_list = ['a', 'b', 'c']
remove = ['b', 'c']

new_list = []
for c in my_list:
    if c not in remove:
        new_list += [c]

my_list = new_list

print(my_list)
