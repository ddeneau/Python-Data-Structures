# An implementation of a Tree data structure
from typing import Generic, TypeVar

T = TypeVar('T')  # For Generics


# The basic unit of a Tree.
class Node(Generic[T]):

    def __init__(self, data: T):
        self.data = data
        self.left = None
        self.right = None


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
def remove_helper(aux_node, removal):
    if aux_node.data is removal:
        if aux_node.right is None:
            aux_node.data = aux_node.left.data
            aux_node.left = aux_node.left.right
        elif aux_node.left is None:
            aux_node.data = aux_node.right.data
            aux_node.right = aux_node.right.right
        else:
            aux_node.right = aux_node.right.right
            aux_node.left = aux_node.left.right
        return
    else:
        if aux_node.left is None:
            remove_helper(aux_node.right, removal)
        else:
            remove_helper(aux_node.left, removal)


# A Tree of Nodes. Does not contain duplicates.
class Tree:

    def __init__(self):
        self.root = None

    def tree_insert(self, data: T):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            insert_helper(self.root, new_node)

    def tree_remove(self, data: T):
        remove_helper(self.root, data)
