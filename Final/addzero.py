

def addZero(L):
    for i in L:
        for j in L[1:]:
            if i + j == 0:
                return True
    return False



a = [-1,4,6,-5,2,-10]


print(addZero(a))


'''
add to zero:
    for every element in the list:
        for every element in the list to the right of the current element:
            if the current element + any other element = zero:
                return True
    if nothing adds to zero return False

'''
