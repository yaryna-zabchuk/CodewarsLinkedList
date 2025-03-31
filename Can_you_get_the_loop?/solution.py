'''Solution for the problem "Can you get the loop?" on Codewars.
https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python'''

def loop_size(node):
    '''Find the size of the loop in a linked list.'''
    visit = {}
    counter = 0

    while node not in visit:
        visit[node] = counter
        counter += 1
        node = node.next

    return counter - visit[node]
