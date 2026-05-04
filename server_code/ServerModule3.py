import anvil.users
import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def add_task(task_text):
  user = anvil.users.get_user()
  if user:
    app_tables.tasks.add_row(title=task_text, done=False, owner=user)

@anvil.server.callable
def get_tasks():
  user = anvil.users.get_user()
  if user:
    return app_tables.tasks.search(owner=user)
  return []
