from ._anvil_designer import ToDoTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ToDo(ToDoTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
def __init__(self, **properties):
  self.init_components(**properties)
  # Fill your list with data from the server
  self.task_list.items = anvil.server.call('get_tasks')

  def add_btn_click(self, **event_args):
    # 1. Grab what the user typed
    new_task = self.new_task_box.text

    if new_task:
      # 2. Send it to the server to save in the database
      anvil.server.call('add_task', new_task)

      # 3. Clear the box so they can type again
      self.new_task_box.text = ""

      # 4. Refresh the list to show the new task
      self.refresh_tasks()
