from ._anvil_designer import ToDoTemplate
from anvil import *
import anvil.server
import anvil.users

class ToDo(ToDoTemplate):
  def add_btn_click(self, **event_args):
    anvil.server.call('add_task', self.new_task_box.text)
    self.new_task_box.text = "" # Clear the box
    self.refresh_tasks() # Refresh the display

