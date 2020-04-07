import random
from Tree import Tree
from List import List


def __main__():
    my_list = List()  # Creating a new list.
    my_tree = Tree()

    for i in range(1, 20):
        entry = random.randrange(20)
        my_tree.tree_insert(entry)

        if i is 10:
            remove = entry

    my_list.add__to("a")
    my_list.add__to("six")
    my_list.add__to("six")

    print(my_list.__str__())
    print(my_tree.__str__())

    my_tree.tree_remove(remove)
    print("AFTER REMOVAL OF " + str(remove))
    print(my_tree.__str__())


if __name__ == "__main__":
    __main__()
