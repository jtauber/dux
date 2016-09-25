#!/usr/bin/env python3

## Pure list manipulation based on Dan Abramov's egghead.io videos

from utils import remove_item, change_item


def add_counter(lst):
    return [*lst, 0]


def remove_counter(lst, index):
    return remove_item(lst, index)


def increment_counter(lst, index):
    return change_item(lst, index, lambda item: item + 1)


initial = []
assert add_counter(initial) == [0]
assert initial == []

initial = [0, 10, 20]
assert remove_counter(initial, 1) == [0, 20]
assert initial == [0, 10, 20]

initial = [0, 10, 20]
assert increment_counter(initial, 1) == [0, 11, 20]
assert initial == [0, 10, 20]

print("All tests passed.")
