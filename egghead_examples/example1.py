#!/usr/bin/env python3

## Basic counter based on Dan Abramov's egghead.io videos


from dux import Store


def counter(state, action):
    if state is None:
        state = 0
    if action.get("type") == "INCREMENT":
        return state + 1
    elif action.get("type") == "DECREMENT":
        return state - 1
    else:
        return state

def log():
    print(store.state)

store = Store(counter)

stop_logging = store.subscribe(log)
log()

store.dispatch({"type": "INCREMENT"})
stop_logging()
store.dispatch({"type": "INCREMENT"})
