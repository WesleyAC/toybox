class Node(object):
    def __init__(self, coords):
        self.coords = coords

class Edge(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Model(object):
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
