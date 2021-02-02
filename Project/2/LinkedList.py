class Node:
    data = 0
    Next = None
    def __init__(self, data):
        self.data = data
    
def traverseList(Node):
    while(Node != None):
        print(Node.data, end = " ")
        Node = Node.Next
    
def getLinkedList(List):
    head = Node(List[0])
    temp = head
    for i in range(1, len(List)):
        temp.Next = Node(List[i])
        temp = temp.Next
    return head
