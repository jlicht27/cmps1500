'''Jonathan Licht
'''

majors = {'Harry': 'Computer Science','Hermoine': 'Mathematics', 'Ron': 'English'}

def look_up(d):                          #input a name and prints major
    name = input('Enter a name: ') 
    if name in d.keys():
        print(d.get(name))
    else:
        print('Not found.')

def add(d):                              #Lets user add a name and major to dictionary
    name_input = input('Enter a name: ')
    major_input = input('Enter a major: ')
    if name_input not in d.keys():
        d[name_input] = major_input
    else:
        print('A person with this name already exists in the system.')


def change(d):                          #lets user change major of a student
    name_input = input('Enter a name: ')
    if name_input in d.keys():
        new_major = input('Enter the new major: ')
        d[name_input] = new_major
    else:
        print('That name is not found.')

def delete(d):                          #lets user delete a major from the dictionary
    remove_input = input('Enter a name: ')
    if remove_input in d.keys():
        del d[remove_input]
    else:
        print('That name is not found.')


        
