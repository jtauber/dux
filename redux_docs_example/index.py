from ..dux import Store

from .reducers import todo_app

store = Store(todo_app)
