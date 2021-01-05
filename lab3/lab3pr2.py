'''Jonathan Licht
Lab 3 part 2
due 2/10/2020
'''

def area(w,h):
    return w*h

name_file = input('Please enter file name: ')

f = open(name_file, 'r')
text = f.read()
f.close()
split_text = text.split()

total_area = 0
for i in range(0, len(split_text), 2):
    room = area(int(split_text[i]),(int(split_text[i + 1])))
    total_area += room
    
    
print('The calculated area is:', total_area)




