## based on reducers.js from http://redux.js.org/docs/basics/Reducers.html


from ..dux import combine_reducers

from .actions import (
    ADD_TODO, TOGGLE_TODO, SET_VISIBILITY_FILTER,
    SHOW_ALL, SHOW_COMPLETED, SHOW_ACTIVE,
)


def visibility_filter(state, action):
    if state is None:
        state = SHOW_ALL
    if action.get("type") == SET_VISIBILITY_FILTER:
        return action["filter"]
    else:
        return state


def todos(state, action):
    if state is None:
        state = []
    if action.get("type") == ADD_TODO:
        return [*state, {
            "text": action["text"],
            "completed": False
        }]
    elif action.get("type") == TOGGLE_TODO:
        return [
            item if item["id"] != action["id"]
                else {**item, "completed": not item["completed"]}
            for item in state
        ]
    else:
        return state


todo_app = combine_reducers({
    "visibilityFilter": visibility_filter,
    "todos": todos,
})
