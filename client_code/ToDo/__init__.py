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
    # Load existing tasks when the app opens
    self.refresh_tasks()

  def refresh_tasks(self):
    # This calls the 'get_tasks' function from your Server Module
    self.task_list.items = anvil.server.call('get_tasks')

  def add_btn_click(self, **event_args):
    # 1. Get the text AND the category
    new_task = self.new_task_box.text
    category = self.category_box.selected_value

    # 2. Only run if there is actually text in the box
    if new_task:
      # 3. Call the server and send BOTH pieces of data
      anvil.server.call('add_task', new_task, category)

      # 4. Clear the text box
      self.new_task_box.text = ""

      # 5. Refresh the list to show the new item
      self.refresh_tasks()

  def settings_btn_click(self, **event_args):
    # Navigate to your Settings page
    open_form('Settings')