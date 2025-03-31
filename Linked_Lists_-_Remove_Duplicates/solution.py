'''Solution for LeetCode problem 83: Remove Duplicates from Sorted List.
https://www.codewars.com/kata/55d9f257d60c5fd98d00001b/train/python'''

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
