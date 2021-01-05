'''Jonathan Licht
    lab 1 part 1
    due monday Feb 17 2020
'''


def look_up(d):                          #input a name and prints major
    name = input('Enter a name: \n') 
    if name in d.keys():
        print(d.get(name))
    else:
        print('Not found.\n')

def add(d):                              #Lets user add a name and major to dictionary
    name_input = input('Enter a name: \n')
    major_input = input('Enter a major: \n')
    if name_input not in d.keys():
        d[name_input] = major_input
    else:
        print('A person with this name already exists in the system.\n')


def change(d):                          #lets user change major of a student
    name_input = input('Enter a name: \n')
    if name_input in d.keys():
        new_major = input('Enter the new major: \n')
        d[name_input] = new_major
    else:
        print('That name is not found.\n')

def delete(d):                          #lets user delete a major from the dictionary
    remove_input = input('Enter a name: \n')
    if remove_input in d.keys():
        del d[remove_input]
    else:
        print('That name is not found.\n')

def display(d):                         #lets user see students and what there majors are
    for key,value in d.items():
        print(key, 'is a wizard in', value)

def get_menu_choice():
    numbers = '123456'
    print('Majors of College Students')
    print('---------------------------')
    print('1. Look up a student\'s major')
    print('2. Add a new major')
    print('3. Change a major')
    print('4. Delete a student')
    print('5. Display all students')
    print('6. Quit the program')
    print()
    list_input = input('Enter your choice: \n')
    while list_input not in numbers:
        list_input = input('Enter a valid choice: \n')
    return list_input



## The main part of your program
majors = {}
choice = 0

while choice != '6':

    choice = get_menu_choice()

    if choice == '1':
        look_up(majors)
    elif choice == '2':
        add(majors)
    elif choice == '3':
        change(majors)
    elif choice == '4':
        delete(majors)
    elif choice == '5':
        display(majors)











    
    
