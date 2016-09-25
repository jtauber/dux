"""
basic implementation of Redux-style store, action and combine_reducers function
"""


class Action:

    def __init__(self, action_type, **data):
        """
        creates an action of the given type and data payload
        """
        self.type = action_type
        self.data = data


class Store:

    def __init__(self, reducer):
        """
        initializes a new store that will use the given reducer
        """
        self._reducer = reducer
        self._state = None
        self._listeners = []
        self.dispatch(Action(None))

    @property
    def state(self):
        """
        returns the stored state
        """
        return self._state

    def dispatch(self, action):
        """
        dispatches the given action to trigger a state change then inform the
        subscribed listeners
        """
        self._state = self._reducer(self._state, action)
        for listener in self._listeners:
            listener()

    def subscribe(self, listener):
        """
        subscribes the given listener and returns a no-arg callable which can
        be called later to unsubscribe the listener
        """

        self._listeners.append(listener)

        def unsubscribe():
            self._listeners.remove(listener)

        return unsubscribe


def combine_reducers(reducers):
    """
    takes a dict mapping state keys to the reducers responsible for them and
    return a single reducer that will delegate appropriately
    """
    def reducer(state, action):
        return {
            key: value(state.get(key) if state else None, action)
            for key, value in reducers.items()
        }
    return reducer
