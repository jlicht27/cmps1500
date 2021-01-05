'''Jonathan Licht
Lab 6 part 1
'''
def is_sorted(lst):
    if len(lst) == 1:                           #1
            return True                         #1
    for i in range(len(lst) - 1):               #N
        if lst[i] <= lst[i + 1]:                 #1
            result = True                       #1
        else:                                   #1
            result = False                      #1
            break                               #1
    return result                               #1

                                                #complexity for is_sorted is linear O(N)


def is_file_sorted(filename):
    f = open(filename, 'r')                     #1
    contents = f.readlines()                    #1
    for j in range(len(contents)):              #N
        contents[j] = int(contents[j])          #1
    f.close()                                   #1
    fileSort = is_sorted(contents)              #N
    return fileSort                             #1

                                                #complexity for is_file_sorted is linear O(N)

file_name = input('Please enter file name: ')                               #1
file_test = is_file_sorted(file_name)                                       #N
if file_test == False:                                                      #1
    print('Looks like', file_name, 'needs to be sorted')                    #1
if file_test == True:                                                       #1
    print('Congratulations! The file', file_name, 'is nicely sorted!')      #1


'''Since both functions are linear, the whole file is linear because when
two linear functions are added together, the result is another linear
function
example:
(2n + 4n = 6n)'''

