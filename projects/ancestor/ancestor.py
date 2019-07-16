# import sys
# sys.path.append("../graph")

# from graph import Graph

def __init__(self):
    self.vertices = {}

def add_vertex(self, vertex):
    """
    Add a vertex to the graph.
    """
    if vertex not in self.vertices:
        self.vertices[vertex] = set()

def add_edge(self, v1, v2):
    """
    Add a directed edge to the graph.
    """
    if v1 not in self.vertices:
        self.add_vertex(v1)
    
    if v2 not in self.vertices:
        self.add_vertex(v2)

    self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
    pass
