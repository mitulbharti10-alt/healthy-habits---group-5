from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def add_button_click(self, **event_args):
    # 1. Get the text from the box
    new_task_text = self.task_box.text

  if new_task_text:
    # 2. Call the server to save it to the database
    anvil.server.call('add_task', new_task_text)

    # 3. Clear the input box so you can type the next one
    self.task_box.text = ""

    # 4. THE MAGIC LINE: This refreshes the list so the new task appears
    self.task_list.items = anvil.server.call('get_tasks')
)


