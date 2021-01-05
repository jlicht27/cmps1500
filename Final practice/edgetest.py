

graph = {'a': ['b', 'c'],
         'b': ['a', 'c', 'e'],
         'c': ['a', 'b', 'd'],
         'd': ['a', 'b', 'c', 'e'],
         'e': ['b', 'd']
}


def isEdge(G,x,y):
    if y in graph[x]:
        return True
    else:
        return False

print(isEdge(graph, 'a', 'e'))
    
    
