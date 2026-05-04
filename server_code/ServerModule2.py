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
  # 1. Find out who is logged in
  user = anvil.users.get_user()
  if user:
    # 2. Only return tasks where the 'author' column matches this user
    return app_tables.tasks.client_writable().search(author=user, done=False)
  else:
    return []

@anvil.server.callable
def add_task(text):
  user = anvil.users.get_user()
  if user:
    # 3. Save the user along with the task
    app_tables.tasks.add_row(title=text, done=False, author=user)

  

