import anvil.users
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_tasks():
  # This fetches the tasks for the logged-in user
  user = anvil.users.get_user()
  if user:
    return app_tables.tasks.client_writable().search(author=user, done=False)
  return []

@anvil.server.callable
def add_task(text, category, due_date): # Added 'due_date' here
  user = anvil.users.get_user()
  if user:
    # This saves the title, category, author, and due date all at once
    app_tables.tasks.add_row(
      title=text, 
      done=False, 
      author=user, 
      category=category,
      due_date=due_date # Added this line to save to the table
    )
