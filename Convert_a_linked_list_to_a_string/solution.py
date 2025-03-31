'''Solution for Convert a linked list to a string.
https://www.codewars.com/kata/582c297e56373f0426000098/train/python'''

from preloaded import Node

def stringify(node):
    '''Convert a linked list to a string.'''
    res = ''
    cur = node

    while cur:
        res += str(cur.data) + ' -> '
        cur = cur.next

    return res + 'None'
