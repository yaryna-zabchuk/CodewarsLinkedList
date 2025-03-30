'''Solution for Convert a linked list to a string.'''
from preloaded import Node

def stringify(node):
    '''Convert a linked list to a string.'''
    res = ''
    cur = node
    while cur:
        res += str(cur.data) + ' -> '
        cur = cur.next
    return res + 'None'
