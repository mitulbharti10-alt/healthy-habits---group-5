import anvil.users
import anvil.server
from anvil.tables import app_tables

# --- Profile Management ---

@anvil.server.callable
def update_user_profile(new_username, new_email, new_img):
  user = anvil.users.get_user()
  if user:
    # Updates username, email, and the 'picture' Media column in your Users table
    user.update(username=new_username, email=new_email, picture=new_img)
    return True
  return False

# --- To-Do List Management ---

@anvil.server.callable
def add_task(task_text):
  user = anvil.users.get_user()
  if user:
    # Adds a new row to your 'tasks' table linked to the logged-in user
    app_tables.tasks.add_row(
      title=task_text, 
      done=False, 
      owner=user
    )

@anvil.server.callable
def get_tasks():
  user = anvil.users.get_user()
  if user:
    # Returns only the tasks that belong to the current user
    return app_tables.tasks.search(owner=user)
