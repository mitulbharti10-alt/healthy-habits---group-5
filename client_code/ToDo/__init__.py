from ._anvil_designer import ToDoTemplate
from anvil import *
import anvil.server
import anvil.users

class ToDo(ToDoTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # This fills the list when you open the page
    self.refresh_tasks()

  def refresh_tasks(self):
    """Fetch tasks and show them in the RepeatingPanel"""
    # This must match the name of your RepeatingPanel
    self.task_list.items = anvil.server.call('get_tasks')

  def add_button_click(self, **event_args):
    # 1. Get the text from the box you just named 'task_box'
    new_task_text = self.task_box.text

    if new_task_text:
      # 2. Save it to the database
      anvil.server.call('add_task', new_task_text)

      # 3. Clear the box
      self.task_box.text = ""

      # 4. Refresh the list so the new task pops up
      self.refresh_tasks()
    else:
      Notification("Please enter a task name").show()
