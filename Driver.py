import random
from Tree import Tree
from List import List


def __main__():
    my_list = List()  # Creating a new list.
    my_tree = Tree()

    for i in range(1, 20):
        my_tree.tree_insert(random.randrange(20))

    my_list.add__to("a")
    my_list.add__to("six")
    my_list.add__to("six")

    print(my_list.__str__())
    print(my_tree.__str__())

    my_tree.tree_remove(2)


if __name__ == "__main__":
    __main__()
