import random


def __main__():
    from List import List
    my_list = List()  # Creating a new list.
    from Tree import Tree
    my_tree = Tree()

    for i in range(1, 6):
        my_tree.tree_insert(random.randrange(5))

    my_tree.tree_remove(2)

    my_list.add__to("a")
    my_list.add__to("six")
    my_list.add__to("six")

    print(my_list.__str__())


if __name__ == "__main__":
    __main__()
