'''Jonathan Licht
lab lab 6 part 0
due monday 3/16/2020'''

def is_sorted(lst):
    if len(lst) == 1:
            return True
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            result = True
        else:
            result = False
            break
    return result

def is_file_sorted(filename):
    f = open(filename, 'r')
    contents = f.readlines()
    for j in range(len(contents)):
        contents[j] = int(contents[j])
    f.close()
    fileSort = is_sorted(contents)
    return fileSort



#print(is_file_sorted('testfile.txt'))


my_list = []

print(is_sorted(my_list))
