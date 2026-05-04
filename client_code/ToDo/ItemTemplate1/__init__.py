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
    # Set the 'item' property before initializing components
    self.init_components(**properties)

    # MANUALLY set the values from the database row (self.item)
    # This replaces the Data Binding boxes in the designer
    self.check_box_1.text = self.item['title']
    self.check_box_1.checked = self.item['done']

  def check_box_1_change(self, **event_args):
    # MANUALLY save the data back to the database when clicked
    # This replaces the "Write back" checkbox in the designer
    self.item['done'] = self.check_box_1.checked
