from ._anvil_designer import ToDo_copyTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class ToDo_copy(ToDo_copyTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.refresh_tasks()

  def refresh_tasks(self):
    self.task_list.items = anvil.server.call("get_tasks")

  def add_btn_click(self, **event_args):
    # 1. Get the text, the category, AND the due date
    new_task = self.new_task_box.text
    category = self.category_box.selected_value
    due_date = self.due_date_picker.date  # Make sure your DatePicker is named this!

    # 2. Only run if there is text in the box
    if new_task:
      # 3. Call the server and send ALL THREE pieces of data
      anvil.server.call("add_task", new_task, category, due_date)

      # 4. Clear the inputs for the next task
      self.new_task_box.text = ""
      self.due_date_picker.date = None

      # 5. Refresh the list
      self.refresh_tasks()

  def settings_btn_click(self, **event_args):
    open_form("Settings")
