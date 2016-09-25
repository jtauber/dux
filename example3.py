#!/usr/bin/env python3

## Pure dictionary manipulation based on Dan Abramov's egghead.io videos


def toggle_todo(todo):
    return {**todo, "completed": not todo["completed"]}


initial = {
    "id": 0,
    "text": "Learn Redux",
    "completed": False,
}

assert toggle_todo(initial) == {
    "id": 0,
    "text": "Learn Redux",
    "completed": True,
}
assert initial == {
    "id": 0,
    "text": "Learn Redux",
    "completed": False,
}

print("All tests passed.")
