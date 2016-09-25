#!/usr/bin/env python3

## Todo list reducer version 2 based on Dan Abramov's egghead.io videos


from dux import Action, Store, combine_reducers
from utils import append_item, update


def todo(state, action):
    if action.type == "ADD_TODO":
        return update(action.data, {"completed": False})
    elif action.type == "TOGGLE_TODO":
        if state["id"] != action.data["id"]:
            return state
        else:
            return update(state, {"completed": not state["completed"]})
    else:
        return state


def todos(state, action):
    if state is None:
        state = []
    if action.type == "ADD_TODO":
        return append_item(state, todo(None, action))
    elif action.type == "TOGGLE_TODO":
        return [todo(item, action) for item in state]
    else:
        return state


def visibility_filter(state, action):
    if state is None:
        state = "SHOW_ALL"
    if action.type == "SET_VISIBILITY_FILTER":
        return action.data["filter"]
    else:
        return state


todo_app = combine_reducers({
    "todos": todos,
    "visibilityFilter": visibility_filter,
})


store = Store(todo_app)

print(store.state)

store.dispatch(Action("ADD_TODO", id=0, text="Learn Redux"))
print(store.state)

store.dispatch(Action("ADD_TODO", id=1, text="Go Shopping"))
print(store.state)

store.dispatch(Action("TOGGLE_TODO", id=0))
print(store.state)

store.dispatch(Action("SET_VISIBILITY_FILTER", filter="SHOW_COMPLETED"))
print(store.state)
