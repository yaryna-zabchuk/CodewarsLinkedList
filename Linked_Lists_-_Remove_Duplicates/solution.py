'''Solution for LeetCode problem 83: Remove Duplicates from Sorted List.'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    '''Remove duplicates from a sorted linked list.'''
    if head is None:
        return None

    cur = head
    while cur:
        if cur.next and cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return head
