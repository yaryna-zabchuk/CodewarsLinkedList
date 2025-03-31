'''Solution for problem Swap Nodes in Pairs.
https://www.codewars.com/kata/59c6f43c2963ecf6bf002252/train/python'''

class Node:
    '''Node class for linked list.'''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    '''Swap nodes in pairs in a linked list.'''
    if head.next is None:
        return head

    first = head
    second = head.next

    first.next = swap_pairs(second.next)
    second.next = first

    return second
