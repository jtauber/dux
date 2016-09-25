"""
utilities to assist with pure functional data structure manipulation
"""


def append_item(lst, item):
    """
    returns a new list equal to the given list with the item appended
    """
    return lst + [item]


def remove_item(lst, index):
    """
    returns a new list equal to the given list with the item at the given index
    removed
    """
    return lst[:index] + lst[index + 1:]


def change_item(lst, index, change):
    """
    returns a new list equal to the given list with the item at the given index
    changed by the callable passed in
    """
    return lst[:index] + [change(lst[index])] + lst[index + 1:]
