from ._anvil_designer import ToDoTemplate
from anvil import *
import anvil.server
import anvil.users

class ToDo(ToDoTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Refresh the list as soon as the page opens
    self.refresh_tasks()

  def refresh_tasks(self):
    """This clears the error: AttributeError: 'ToDo' object has no attribute 'refresh_tasks'"""
    # 1. Get the latest tasks from your server module
    my_tasks = anvil.server.call('get_tasks')
    # 2. Assign them to your RepeatingPanel (check the name matches repeating_panel_1)
    self.task_list.items = my_tasks

  def add_btn_click(self, **event_args):
    """This method is called when the 'Add' button is clicked"""
    print("Button was clicked!") # Confirms the button is working
    task_name = self.new_task_box.text

    if task_name:
      # Save the task to the database
      anvil.server.call('add_task', task_name)
      # Clear the input box
      self.new_task_box.text = "" 
      # Refresh the display so the new task shows up immediately
      self.refresh_tasks()
