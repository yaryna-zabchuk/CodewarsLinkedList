'''Solution for the problem of moving a node from one linked list to another
https://www.codewars.com/kata/55da347204760ba494000038/train/python'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''Move a node from one linked list to another.'''
    if source is None:
        raise ValueError("error should be thrown when source list is empty")

    next_node = source.next
    source.next = dest

    return Context(next_node, source)
