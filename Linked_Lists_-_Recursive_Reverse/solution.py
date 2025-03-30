'''Solution for reversing a linked list using recursion'''

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    '''Reverse a linked list using recursion.'''
    if head is None or head.next is None:
        return head

    hew_head = reverse(head.next)
    head.next.next = head
    head.next = None

    return hew_head
