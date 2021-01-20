class Node:
  data = 0
  Next = None
  def __init__(self, data):
    self.data = data
    
def traverseList(Node):
  while(Node != None):
    print(Node.data, end = " ")
    Node = Node.Next
    
