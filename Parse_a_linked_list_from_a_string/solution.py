'''Solution for the problem of parsing a linked list from a string
https://www.codewars.com/kata/582c5382f000e535100001a7/train/python'''
from preloaded import Node

def linked_list_from_string(s):
    '''Convert a string to a linked list.'''
    if s == 'None':
        return None

    s = list(map(int, s.split(' -> ')[:-1]))
    head = cur = Node(s.pop(0))

    for data in s:
        next = Node(data)
        cur.next = next
        cur = next

    return head
