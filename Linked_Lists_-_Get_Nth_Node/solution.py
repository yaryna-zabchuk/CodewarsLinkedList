'''Solution for the problem of getting the nth node from the end of a linked list. 
https://www.codewars.com/kata/55befc42bfe4d13ab1000007/train/python'''
from preloaded import Node

def get_nth(node, index):
    if node is None:
        raise ValueError("None linked list should throw error.")
    if not 0 <= index:
        raise ValueError("Invalid index value should throw error.")

    for _ in range(index):
        node = node.next
        if node is None:
            raise ValueError("Invalid index value should throw error.")

    return node
