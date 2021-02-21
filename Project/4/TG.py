import numpy as np

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Graph:
    def __init__(self, n):
        self.graph = np.zeros([n, n])
