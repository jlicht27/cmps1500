'''Jonathan Licht
lab 6 part 3'''

def use_mergesort(inputfile, outputfile):
    f = open(inputfile, 'r')                 
    contents = f.readlines()                
    for j in range(len(contents)):          
        contents[j] = int(contents[j])      
    sorted_contents = merge_sort(contents)
    f.close
    g = open(outputfile, 'w')
    for i in range(len(sorted_contents)):
        sorted_contents[i] = str(sorted_contents[i])
        g.write(sorted_contents[i])
        g.write('\n')
    g.close

import time

def analyze_mergesort(inputfile, outputfile):
    t0 = time.time()
    f = open(inputfile, 'r')                 
    contents = f.readlines()
    t1 = time.time()
    for j in range(len(contents)):          
        contents[j] = int(contents[j])      
    sorted_contents = merge_sort(contents)
    f.close
    t2 = time.time()
    g = open(outputfile, 'w')
    for i in range(len(sorted_contents)):
        sorted_contents[i] = str(sorted_contents[i])
        g.write(sorted_contents[i])
        g.write('\n')
    g.close
    t3 = time.time()
    read_time = t1 - t0
    sort_time = t2 - t1
    write_time = t3 - t2
    total_time = t3 - t0
    print('It took', round(read_time,6), 'seconds to input', len(sorted_contents), 'values from file', inputfile)
    print('It took', round(sort_time,6), 'seconds to sort', len(sorted_contents), 'values using merge sort')
    print('It took', round(write_time,6), 'seconds to output', len(sorted_contents), 'sorted values to file', outputfile)
    total_string = 'Total time the program took is' + ' ' + str(round(total_time, 6)) + ' ' + 'seconds'
    return total_string
      
def merge_sort(aList):
    """
    Merge sort recursively divide the list into half, sort both halves
    and then merge the two sorted lists into one.
    """
    # If the aList is size 0 or 1, it's already sorted.
    if len( aList ) <= 1:
        return aList
    else:
        mid = len(aList)//2
        # Recursively sort the left and right halves
        left = merge_sort( aList[ :mid ] )
        right = merge_sort( aList[mid:] )
        
        # Merge the two (each sorted) parts back together
        return merge( left, right )
                            
def merge(left, right):
    """
    Merge to sorted list, left and right, into one sorted list.
    """
    aList = []
    lt = 0
    rt = 0
    # Repeatedly move the smallest of left and right to the new list
    while lt < len(left) and rt < len(right):
        if left[lt] < right[rt]:
            aList.append(left[lt])
            lt += 1
        else:
            aList.append(right[rt])
            rt += 1
    # There will only be elements left in one of the original two lists.
    # Append the remains of left (lt..end) on to the new list.
    while lt < len(left):
        aList.append( left[ lt ] )
        lt += 1   
    # Append the remains of right (rt..end) on to the new list.
    while rt < len( right ):
        aList.append( right[ rt ] )
        rt += 1
    return aList

def use_selection(inputfile, outputfile):
    f = open(inputfile, 'r')                 
    contents = f.readlines()                
    for j in range(len(contents)):          
        contents[j] = int(contents[j])      
    sorted_contents = selection_sort(contents)
    f.close
    g = open(outputfile, 'w')
    for i in range(len(sorted_contents)):
        sorted_contents[i] = str(sorted_contents[i])
        g.write(sorted_contents[i])
        g.write('\n')
    g.close

def selection_sort( aList ):
  """Sorts a list in ascending order using the selection sort algorithm.
  """
  n = len( aList )
  for i in range( n - 1 ):
    
      
    # Find the minimum element in the unsorted portion of the list
    
    smallNdx = i # assume the ith element is the smallest.
    
    # Determine if any other element contains a smaller value.
    for j in range( i + 1, n ):
      if aList[ j ] < aList[ smallNdx ] :
        smallNdx = j

    # Swap the ith value and smallNdx value  
                      
    tmp = aList[ i ]
    aList[ i ] = aList[ smallNdx ]
    aList[ smallNdx ] = tmp

  return aList

def analyze_selection(inputfile,outputfile):
    t4 = time.time()
    f = open(inputfile, 'r')                 
    contents = f.readlines()
    t5 = time.time()
    for j in range(len(contents)):          
        contents[j] = int(contents[j])      
    sorted_contents = selection_sort(contents)
    f.close
    t6 = time.time()
    g = open(outputfile, 'w')
    for i in range(len(sorted_contents)):
        sorted_contents[i] = str(sorted_contents[i])
        g.write(sorted_contents[i])
        g.write('\n')
    g.close
    t7 = time.time()
    read_time = t5 - t4
    sort_time = t6 - t5
    write_time = t7 - t6
    total_time = t7 - t4
    print('It took', round(read_time,6), 'seconds to input', len(sorted_contents), 'values from file', inputfile)
    print('It took', round(sort_time,6), 'seconds to sort', len(sorted_contents), 'values using selection sort')
    print('It took', round(write_time,6), 'seconds to output', len(sorted_contents), 'sorted values to file', outputfile)
    total_string = 'Total time the program took is' + ' ' + str(round(total_time, 6)) + ' ' + 'seconds'
    return total_string
    

