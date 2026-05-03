from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def check_box_1_change(self, **event_args):
    """Saves the 'Done' status when you click the checkmark"""
    self.refresh_data_bindings()
