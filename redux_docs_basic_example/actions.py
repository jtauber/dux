## based on actions.js from http://redux.js.org/docs/basics/Actions.html

# action types

ADD_TODO = "ADD_TODO"
TOGGLE_TODO = "TOGGLE_TODO"
SET_VISIBILITY_FILTER = "SET_VISIBILITY_FILTER"

# other constants

SHOW_ALL = "SHOW_ALL"
SHOW_COMPLETED = "SHOW_COMPLETED"
SHOW_ACTIVE = "SHOW_ACTIVE"


# action creators

def add_todo(text):
    return {"type": ADD_TODO, "text": text}

def toggle_todo(index):
    return {"type": TOGGLE_TODO, "index": index}

def set_visibility_filter(filter):
    return {"type": SET_VISIBILITY_FILTER, "filter": filter}
