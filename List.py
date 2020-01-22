# A list of objects.
from typing import Generic, TypeVar

T = TypeVar('T')


def string_helper(node, result):
    if node is None:
        print(result)
        return
    elif isinstance(node.data, str):
        result += node.data + " - > "
    else:
        try:
            result += node.data.__str__() + " - > "
        except AttributeError:
            result += "N/A - > "

    string_helper(node.next, result)


class List(Generic[T]):

    # A Node: Stores data and a pointer to the "next" node in the list.
    class Node(Generic[T]):

        # Node constructor. Pass in data.
        def __init__(self, data: T) -> None:
            self.data = data
            self.next = None

    # List constructor. Initializes tail and head to none.
    def __init__(self):
        self.head = None

    # Points head and tail to item if empty. Or else
    # Adds the item after the head.
    def add__to(self, data: T):
        new_node = List.Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        return self

    def remove_from_head(self):
        if self.head.next is not None:
            self.head = self.head.next

    def __str__(self):
        curr = self.head
        result = ""

        string_helper(curr, result)

        return result




