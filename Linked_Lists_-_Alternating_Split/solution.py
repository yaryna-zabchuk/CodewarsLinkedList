'''Solution for the problem "Linked Lists - Alternating Split" on Codewars.
https://www.codewars.com/kata/55dd5386575839a74f0000a9/train/python'''

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    '''Split a linked list into two lists, one with even 
    indexed nodes and the other with odd indexed nodes.'''

    if head is None:
        raise ValueError("splitting a None list should throw an error.")
    if head.next is None:
        raise ValueError("splitting a single node list should throw an error.")
    if head.next.next is None:
        return Context(Node(head.data), Node(head.next.data))

    def split_helper(node):
        if node is None:
            return None

        res = cur = Node(node.data)
        node = node.next.next

        while node:
            cur.next = Node(node.data)
            cur = cur.next
            if node.next:
                node = node.next.next
            else:
                break

        return res

    first = split_helper(head)
    second = split_helper(head.next)

    return Context(first, second)
