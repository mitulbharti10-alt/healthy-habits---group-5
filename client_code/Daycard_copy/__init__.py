from ._anvil_designer import Daycard_copyTemplate
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Daycard_copy(Daycard_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    if self.item:
      self.label_date.text = self.item['date'].day
      self.label_day_name.text = self.item['day'] # This comes from our stats list

  @handle("link_1", "click")
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    def link_1_click(self, **event_args):
      # This uses the data we passes into the card earlier
      if self.item ['active']:
        alert(f"Nice! You logged in on {self.item['date'].strtftime('%A, %b. %d')}")
      else:
        alert(f"No login recorded for {self.item['date'].strtftime('%A, %b, $d')}")
