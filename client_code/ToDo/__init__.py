from ._anvil_designer import ToDoTemplate
from anvil import *
import anvil.server

class ToDo(ToDoTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.refresh_tasks()

  def refresh_tasks(self):
    self.task_list.items = anvil.server.call('get_tasks')

  def add_btn_click(self, **event_args):
    # 1. Get the text, the category, AND the due date
    new_task = self.new_task_box.text
    category = self.category_box.selected_value

    # 2. Only run if there is text in the box
    if new_task:
      # 3. Call the server and send ALL THREE pieces of data
      anvil.server.call('add_task', new_task, category)

      # 4. Clear the inputs for the next task
      self.new_task_box.text = ""

      # 5. Refresh the list
      self.refresh_tasks()

  def settings_btn_click(self, **event_args):
    open_form('Settings')
