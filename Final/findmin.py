

def min(L):
    minimum = L[0]
    for i in L:
        if i < minimum:
            minimum = i
    return minimum




a = [5,9,12,16,3]
print(min(a))

'''

minimum element:
    minimum = the first element of the list
    for every element in the list L:
        if that element < the present minimum:
            that number = the new minimum
    return the minimum element
'''
