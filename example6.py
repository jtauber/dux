#!/usr/bin/env python3

## Todo list reducer version 2 based on Dan Abramov's egghead.io videos


from dux import Store, combine_reducers
from utils import append_item, update


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
            return update(state, {"completed": not state["completed"]})
    else:
        return state


def todos(state, action):
    if state is None:
        state = []
    if action.get("type") == "ADD_TODO":
        return append_item(state, todo(None, action))
    elif action.get("type") == "TOGGLE_TODO":
        return [todo(item, action) for item in state]
    else:
        return state


def visibility_filter(state, action):
    if state is None:
        state = "SHOW_ALL"
    if action.get("type") == "SET_VISIBILITY_FILTER":
        return action["filter"]
    else:
        return state


todo_app = combine_reducers({
    "todos": todos,
    "visibilityFilter": visibility_filter,
})


store = Store(todo_app)

print(store.state)

store.dispatch({"type": "ADD_TODO", "id": 0, "text": "Learn Redux"})
print(store.state)

store.dispatch({"type": "ADD_TODO", "id":1, "text": "Go Shopping"})
print(store.state)

store.dispatch({"type": "TOGGLE_TODO", "id":0})
print(store.state)

store.dispatch({"type": "SET_VISIBILITY_FILTER", "filter": "SHOW_COMPLETED"})
print(store.state)
