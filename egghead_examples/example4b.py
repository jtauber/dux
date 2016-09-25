#!/usr/bin/env python3

## Todo list reducer version 2 based on Dan Abramov's egghead.io videos


from dux import Store


def todo(state, action):
    if action.get("type") == "ADD_TODO":
        return {
            "id": action["id"],
            "text": action["text"],
            "completed": False
        }
    elif action.get("type") == "TOGGLE_TODO":
        if state["id"] != action["id"]:
            return state
        else:
            return {**state, "completed": not state["completed"]}
    else:
        return state


def todos(state, action):
    if state is None:
        state = []
    if action.get("type") == "ADD_TODO":
        return [*state, todo(None, action)]
    elif action.get("type") == "TOGGLE_TODO":
        return [todo(item, action) for item in state]
    else:
        return state


before = []
action = {"type": "ADD_TODO", "id": 0, "text": "Learn Redux"}
after = [
    {
        "id": 0,
        "text": "Learn Redux",
        "completed": False,
    }
]
assert todos(before, action) == after
assert before == []

before = [
    {
        "id": 0,
        "text": "Learn Redux",
        "completed": False,
    },
    {
        "id": 1,
        "text": "Go shopping",
        "completed": False,
    },
]
action = {"type": "TOGGLE_TODO", "id": 1}
after = [
    {
        "id": 0,
        "text": "Learn Redux",
        "completed": False,
    },
    {
        "id": 1,
        "text": "Go shopping",
        "completed": True,
    },
]
assert todos(before, action) == after
assert before == [
    {
        "id": 0,
        "text": "Learn Redux",
        "completed": False,
    },
    {
        "id": 1,
        "text": "Go shopping",
        "completed": False,
    },
]

print("All tests passed.")
