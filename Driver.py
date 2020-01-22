from sympy import Integer


def __main__():
    from List import List
    my_list = List()  # Creating a new list.

    my_list.add__to("a")
    my_list.add__to("six")
    my_list.add__to("six")

    print(my_list.__str__())


if __name__ == "__main__":
    __main__()
