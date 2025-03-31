'''Solution for Codewars problem: Linked Lists - Push & Build One Two Three
https://www.codewars.com/kata/582c5382f000e535100001a7/train/python'''
from preloaded import Node

def push(head, data):
    '''Push a new node with data to the front of the linked list.'''
    new_node = Node(data, head)
    return new_node

def build_one_two_three():
    '''Build a linked list with the values 1, 2, and 3.'''
    head = Node(3)
    head = push(head, 2)
    head = push(head, 1)
    return head
