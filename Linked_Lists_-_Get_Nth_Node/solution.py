'''Solution for the problem of getting the nth node from the end of a linked list. '''
from preloaded import Node

def get_nth(node, index):
    if node is None:
        raise ValueError("None linked list should throw error.")
    if not 0 <= index:
        raise ValueError("Invalid index value should throw error.")

    for _ in range(index):
        node = node.next
        if node is None:
            raise ValueError("Invalid index value should throw error.")

    return node

linked_list = Node(1, Node(2, Node(3, None)))
print(get_nth(linked_list, 3))