"""
utilities to assist with pure functional data structure manipulation
"""


def remove_item(lst, index):
    """
    returns a new list equal to the given list with the item at the given index
    removed
    """

    # In the simple case, making a copy of the list and `del`ing the item is
    # much faster but I suspect if the items are complex datastructures
    # themselves, this is more efficient.
    return lst[:index] + lst[index + 1:]


def change_item(lst, index, change):
    """
    returns a new list equal to the given list with the item at the given index
    changed by the callable passed in
    """

    # In the simple case, making a copy of the list and changing the item is
    # much faster but I suspect if the items are complex datastructures
    # themselves, this is more efficient.
    return lst[:index] + [change(lst[index])] + lst[index + 1:]
