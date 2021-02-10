"""
node = Node(d)
head = getLinkedList(L)
traverseList(L)
tail = getTail(node)
traverseList(L2)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None
    
def traverseList(node):
    while(node != None):
        print(node.data, end = " ")
        node = node.Next
    
def getLinkedList(List):
    head = Node(List[0])
    temp = head
    for i in range(1, len(List)):
        temp.Next = Node(List[i])
        temp = temp.Next
    return head

def getTail(node):
    while(node.Next != None):
        node = node.Next
    return node

def traverseList2(node):
    Set = set()
    while(node != None and node not in Set):
        print(node.data, end = " ")
        Set.add(node)
        node = node.Next
