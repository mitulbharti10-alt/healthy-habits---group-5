import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users 

@anvil.server.callable
def get_tasks():
  # This fetches the tasks for the logged-in user
  user = anvil.users.get_user()
  if user:
    return app_tables.tasks.client_writable().search(author=user, done=False)
  return []

@anvil.server.callable
def add_task(text, category):
  # This saves the new task with its category
  user = anvil.users.get_user()
  if user:
    app_tables.tasks.add_row(
      title=text, 
      done=False, 
      author=user, 
      category=category
    )