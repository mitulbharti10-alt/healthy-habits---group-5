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
    self.init_components(**properties)
    # This loads the existing tasks when the app opens
    self.refresh_tasks()

  def refresh_tasks(self):
    # This fills the repeating panel
    self.task_list.items = anvil.server.call('get_tasks')

  def add_btn_click(self, **event_args):
    # 1. Grab what the user typed
    new_task = self.new_task_box.text

    if new_task:
      # 2. Send it to the server to save
      anvil.server.call('add_task', new_task)

      # 3. Clear the box
      self.new_task_box.text = ""

      # 4. Refresh the list
      self.refresh_tasks()