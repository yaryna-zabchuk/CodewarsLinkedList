'''Solution for problem Swap Nodes in Pairs.'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    if head.next is None:
        return head

    first = head
    second = head.next

    first.next = swap_pairs(second.next)
    second.next = first

    return second


# def swap_pairs(head):
#     counter = 0
#     cur = head
#     prev = Node(head)

#     while cur:
#         counter += 1
#         next = cur.next

#         if counter % 2 and next:
#             if prev:
#                 prev.next = next
#             next.next = cur
#             cur.next = next.next
#             if counter == 1:
#                 head = next

#         prev = cur
#         cur = cur.next

#     return head

def stringify(node):
    '''Convert a linked list to a string'''
    res = ''
    cur = node

    while cur:
        res += str(cur.data) + ' -> '
        cur = cur.next

    return res + 'None'

ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(stringify(ll))
ll = swap_pairs(ll)
print(stringify(ll))
