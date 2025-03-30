'''Solution for the problem of inserting a new node into a sorted linked list'''
from preloaded import Node

def sorted_insert(head, data):
    '''Insert a new node with the given data into a sorted linked list.'''
    new_node = Node(data)

    if head is None or head.data >= new_node.data:
        new_node.next = head
        return new_node

    cur = head
    while cur.next is not None and cur.next.data < new_node.data:
        cur = cur.next
    new_node.next = cur.next
    cur.next = new_node
    return head
