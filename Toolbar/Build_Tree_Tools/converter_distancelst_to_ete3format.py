from ete3 import Tree, TextFace, NodeStyle, TreeStyle
class Node:
    def __init__(self, label, depth):
        self.label = label
        self.depth = depth
        self.links = []

    def is_terminal(self):
        return len(self.links) == 0

    # if you have children, get their representation
    # if you don't have children, just the label
    def __str__(self):
        if self.is_terminal():
            return "%s:%.3f" % (self.label, self.depth)
        else:
            segments = []
            for link in self.links:
                child = link.to_node
                segments.append(str(child) if child.is_terminal() else "%s:%.3f"%(child, self.depth - child.depth))

            return "(" + ",".join(segments) + ")"

class Link:
    def __init__(self, to_node):
        self.to_node = to_node     #from bottom to root

class TTree:
    def __init__(self):
        self.nodes = []

    def is_node(self, label):
        for node in self.nodes:
            if node.label == label:
                return True
        return False

    def get_node(self, label):
        for node in self.nodes:
            if node.label == label:
                return node
        print("ERROR: Node with given label not found")
        return False


    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, node, depth=0):
        #print(" " * depth + node.label)
        for link in node.links:
            self._traverse(link.to_node, depth + 1)

    def convert(self):
        return str(self.root)

    # procedure:
    # - look at the 1st and 3rd element, are they in the terminal nodes?
    #   - no: then create a new terminal node and add it to the terminal nodes list
    #   - yes: connect them and remove this element from the terminal nodes list
    def build_tree(self, tree_input):
        for parent, child1, weight, child2 in tree_input:
            new_node = Node(parent,weight)
            self.nodes.append(new_node)
            for child in [child1, child2]:
                if not self.is_node(child):
                    child_node = Node(child, weight)
                    self.nodes.append(child_node)
                    new_node.links.append(Link(child_node))
                else:
                    child_node = self.get_node(child)
                    new_node.links.append(Link(child_node))
            self.root = new_node

def prepare_tree(input):
    tree = TTree()
    tree.build_tree(input)
    tree.traverse()
    a=tree.convert()
    return a

input=[('fb', 'f', 0.5, 'b'),
('da', 'd', 4.0, 'a'),
('gfb', 'g', 6.25, 'fb'),
('dagfb', 'da', 8.25, 'gfb'),
('cdagfb', 'c', 14.5, 'dagfb'),
('ecdagfb', 'e', 17.0, 'cdagfb')]

