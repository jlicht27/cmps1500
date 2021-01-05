

def create2DArray(height,width):
    h_list = []
    w_list = []
    for i in range(height):
        for j in range(width):
            w_list += [i*j]
        h_list += [w_list]
        w_list = []
    return h_list


    
def addOne(anArray):
    for i in anArray:
        for j in range(len(i)):
            i[j] += 1
    return anArray


myArray = create2DArray(3,5)

print(myArray)

addOne(myArray)

print(myArray)

