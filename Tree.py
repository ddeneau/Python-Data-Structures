# An implementation of a Tree (BST properties).
from typing import Generic, TypeVar

T = TypeVar('T')  # For placing any objects in our tree.


# Node object to store data in units in the tree. Comparisons are based on the DATA field of each
# node.
class Node(Generic[T]):

    # Constructor initializing a node with data. Left and right pointers are set to "None."
    def __init__(self, data: T):
        self.data = data
        self.left = None
        self.right = None

    # Equals method comparing two nodes based on their DATA only.
    def __eq__(self, other):
        return self.data.__eq__(other.data)

    # For debugging and printing. 
    def __str__(self):
        return "Node: " + self.data.__str__()


# Recursive auxiliary method for adding data to a Tree.
def insert_helper(node, insertion):
    if node.data.__gt__(insertion.data):
        if node.left is None:
            node.left = insertion
            return
        else:
            insert_helper(node.left, insertion)
    elif node.data.__lt__(insertion.data):
        if node.right is None:
            node.right = insertion
            return
        else:
            insert_helper(node.right, insertion)
    elif node.data.__eq__(insertion.data):
        return


# Recursive auxiliary method for adding data to a Tree.
# Base Case occurs when target node is found OR data is NoneType.
# Otherwise, target node may be in left or right subtrees.
def remove_helper(aux_node, removal):
    if aux_node is None:
        return

    if removal < aux_node.data:
        aux_node.left = remove_helper(aux_node.left, removal)
    elif removal > aux_node.data:
        aux_node.right = remove_helper(aux_node.right, removal)
    else:
        if aux_node.right is None:
            return aux_node.left
        elif aux_node.left is None:
            return aux_node.right

        temp_node = aux_node  # Create a temporary node in memory to keep track of target nodes references.
        aux_node = find_minimum(temp_node.right)  # Set target node to be the minimum of its right subtree.
        aux_node.right = remove_minimum_helper(temp_node.right)  # Corrects target references on right side
        aux_node.left = temp_node.left  # Corrects target references on left side.

    return aux_node


def find_minimum(node):
    if node.left is None:
        return node

    return find_minimum(node.left)


def find_maximum(node):
    if node.right is None:
        return node

    return find_maximum(node.right)


def remove_minimum_helper(node):
    if node.left is None:
        return node.right

    node.left = remove_minimum_helper(node.left)


def remove_maximum_helper(node):
    if node.right is None:
        return node.left

    node.right = remove_maximum_helper(node.right)


# A Tree of Nodes. Does not contain duplicates.
def string_aux(aux):
    if aux is None:
        return

    string_aux(aux.left)
    print(aux.__str__())
    string_aux(aux.right)


class Tree:

    def __init__(self):
        self.root = None

    def tree_insert(self, data: T):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            insert_helper(self.root, new_node)

    def tree_remove(self, node):
        remove_helper(self.root, node)

    def __str__(self):
        string_aux(self.root)

    def remove_minimum(self):
        remove_minimum_helper(self.root)

    def remove_maximum(self):
        remove_maximum_helper(self.root)
