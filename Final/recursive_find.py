
        
def find(first_node, data):
    if first_node == None:
        return None
    else:
        if first_node.data == data:
            return first_node.data
        else:
            return find(first_node.next, data)
    
