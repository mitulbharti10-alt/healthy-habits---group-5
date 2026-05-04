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
  def __init__(self, **properties):
    self.init_components(**properties)

    # Fill the row with data
    self.check_box_1.text = self.item['title']
    self.check_box_1.checked = self.item['done']

    def check_box_1_change(self, **event_args):
    # 1. Update the database row
      self.item['done'] = self.check_box_1.checked

    # 2. Refresh the list safely
    # If the task is checked, tell the panel to reload the items
    if self.check_box_1.checked:
      # This re-calls the server function to filter out the 'done' task
      self.parent.items = anvil.server.call('get_tasks')

