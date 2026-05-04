import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_tasks():
  # '.search()' fetches the rows. 
  # '.client_writable()' allows the app to update the 'done' checkbox.
  return app_tables.tasks.client_writable().search()

@anvil.server.callable
def add_task(text):
  # This is the function your 'Add' button calls to save a new row.
  app_tables.tasks.add_row(title=text, done=False)

