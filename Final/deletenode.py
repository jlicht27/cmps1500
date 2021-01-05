

def delete(delete_node):
    if delete_node.prev == None:
        delete_node.next.prev = None
    else:
        if delete_node.next == None:
            delete_node.prev.next = None
        else:
            delete_node.next.prev = delete_node.prev
            delete_node.prev.next = delete_node.next
