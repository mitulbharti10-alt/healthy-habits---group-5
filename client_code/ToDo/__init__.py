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
    # Set up the components
    self.init_components(**properties)

    # Load existing tasks when the app opens
    self.refresh_tasks()

  def refresh_tasks(self):
    # This calls the 'get_tasks' function from your Server Module
    self.task_list.items = anvil.server.call('get_tasks')

  def add_btn_click(self, **event_args):
    # 1. Get the text from your box
    new_task = self.new_task_box.text

    if new_task:
      # 2. Call the 'add_task' function from your Server Module
      anvil.server.call('add_task', new_task)

      # 3. Clear the box
      self.new_task_box.text = ""

      # 4. Refresh the list to show the new task
      self.refresh_tasks()