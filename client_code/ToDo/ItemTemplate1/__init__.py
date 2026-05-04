from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users

class ItemTemplate1(ItemTemplate1Template):
  def refresh_tasks(self):
    self.repeating_panel_1.items = anvil.server.call('get_tasks')
