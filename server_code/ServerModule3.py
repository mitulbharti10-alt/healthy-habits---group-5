import anvil.users
import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def add_task(task_text):
  user = anvil.users.get_user()
  if user:
    # Adds the task and links it to the logged-in user
    app_tables.tasks.add_row(title=task_text, done=False, owner=user)

@anvil.server.callable
def get_tasks():
  user = anvil.users.get_user()
  if user:
    # 'client_writable' is required so that clicking the CheckBox 
    # on your screen actually updates the 'done' column in the table.
    return app_tables.tasks.client_writable(owner=user).search()
  else:
    return []
