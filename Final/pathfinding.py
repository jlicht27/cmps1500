

grid = {'a': ['b', 'f'],
        'b': ['a', 'c', 'g'],
        'c': ['b', 'd'],
        'd': ['c', 'e'],
        'e': ['d'],
        'f': ['a', 'g', 'h'],
        'g': ['b', 'f', 'i'],
        'h': ['f', 'i'],
        'i': ['g', 'h', 'j'],
        'j': ['i', 'k'],
        'k': ['j', 'l', 'm'],
        'l': ['k', 'n'],
        'm': ['k', 'n', 'q'],
        'n': ['l', 'm'],
        'o': ['p'],
        'p': ['o', 'q'],
        'q': ['m', 'p', 'r'],
        'r': ['n', 'q']
}




def findPath(G,start,end):
    if end in G[start]:                 #base case
        return end  
    else:                               #recursive case         
        for i in G[start]:
            return [start] + [findPath(G,i,end)]
        
print(findPath(grid,'e','r'))

'''It throws up a recursion error, not sure how to change this
into finding only the shortest path. I know BFS has to be involved
in some way.'''
